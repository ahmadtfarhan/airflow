# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from __future__ import annotations

from unittest import mock

import pytest

from airflow.models import Connection
from airflow.providers.apache.tinkerpop.hooks.gremlin import GremlinHook


class TestGremlinHook:
    @pytest.mark.parametrize(
        "host, port, expected_uri",
        [
            ("host", None, "ws://host:443/gremlin"),
            ("myhost", 1234, "ws://myhost:1234/gremlin"),
            ("localhost", 8888, "ws://localhost:8888/gremlin"),
        ],
    )
    def test_get_uri(self, host, port, expected_uri):
        """
        Test that get_uri builds the expected URI from the connection.
        """
        conn = Connection(conn_id="gremlin_default", host=host, port=port)
        with mock.patch.dict("os.environ", AIRFLOW_CONN_GREMLIN_DEFAULT=conn.get_uri()):
            gremlin_hook = GremlinHook()
            uri = gremlin_hook.get_uri(conn)

            assert uri == expected_uri

    @mock.patch("airflow.providers.apache.tinkerpop.hooks.gremlin.Client")
    def test_get_conn(self, mock_client):
        """
        Test that get_conn() retrieves the connection and creates a client correctly.
        """
        hook = GremlinHook()
        conn = Connection(
            conn_type="gremlin",
            conn_id="gremlin_default",
            host="host",
            port=1234,
            schema="mydb",
            login="login",
            password="mypassword",
        )
        hook.get_connection = lambda conn_id: conn

        hook.get_conn()
        expected_uri = "wss://host:1234/"
        expected_username = "/dbs/login/colls/mydb"

        mock_client.assert_called_once()

        call_args = mock_client.call_args.kwargs
        assert call_args["url"] == expected_uri
        assert call_args["traversal_source"] == hook.traversal_source
        assert call_args["username"] == expected_username
        assert call_args["password"] == "mypassword"

    @pytest.mark.parametrize(
        "side_effect, expected_exception, expected_result",
        [
            (None, None, ["dummy_result"]),
            (Exception("Test error"), Exception, None),
        ],
    )
    @mock.patch("airflow.providers.apache.tinkerpop.hooks.gremlin.Client")
    def test_run(self, mock_client, side_effect, expected_exception, expected_result):
        """
        Test that run() returns the expected result or propagates an exception.
        """
        instance = mock_client.return_value

        if side_effect is None:
            instance.submit.return_value.all.return_value.result.return_value = expected_result
        else:
            instance.submit.return_value.all.return_value.result.side_effect = side_effect

        hook = GremlinHook()
        hook.client = instance
        query = "g.V().limit(1)"
        if expected_exception:
            with pytest.raises(expected_exception, match="Test error"):
                hook.run(query)
        else:
            result = hook.run(query)
            assert result == expected_result

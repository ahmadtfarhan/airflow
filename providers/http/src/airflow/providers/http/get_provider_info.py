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

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-http",
        "name": "Hypertext Transfer Protocol (HTTP)",
        "description": "`Hypertext Transfer Protocol (HTTP) <https://www.w3.org/Protocols/>`__\n",
        "integrations": [
            {
                "integration-name": "Hypertext Transfer Protocol (HTTP)",
                "external-doc-url": "https://www.w3.org/Protocols/",
                "how-to-guide": ["/docs/apache-airflow-providers-http/operators.rst"],
                "logo": "/docs/integration-logos/HTTP.png",
                "tags": ["protocol"],
            }
        ],
        "operators": [
            {
                "integration-name": "Hypertext Transfer Protocol (HTTP)",
                "python-modules": ["airflow.providers.http.operators.http"],
            }
        ],
        "sensors": [
            {
                "integration-name": "Hypertext Transfer Protocol (HTTP)",
                "python-modules": ["airflow.providers.http.sensors.http"],
            }
        ],
        "hooks": [
            {
                "integration-name": "Hypertext Transfer Protocol (HTTP)",
                "python-modules": ["airflow.providers.http.hooks.http"],
            }
        ],
        "triggers": [
            {
                "integration-name": "Hypertext Transfer Protocol (HTTP)",
                "python-modules": ["airflow.providers.http.triggers.http"],
            }
        ],
        "connection-types": [
            {"hook-class-name": "airflow.providers.http.hooks.http.HttpHook", "connection-type": "http"}
        ],
    }

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
        "package-name": "apache-airflow-providers-atlassian-jira",
        "name": "Atlassian Jira",
        "description": "`Atlassian Jira <https://www.atlassian.com/software/jira/>`__\n",
        "state": "ready",
        "source-date-epoch": 1743477791,
        "versions": [
            "3.0.2",
            "3.0.1",
            "3.0.0",
            "2.7.1",
            "2.7.0",
            "2.6.1",
            "2.6.0",
            "2.5.1",
            "2.5.0",
            "2.4.0",
            "2.3.0",
            "2.2.0",
            "2.1.1",
            "2.1.0",
            "2.0.1",
            "2.0.0",
            "1.1.0",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Atlassian Jira",
                "external-doc-url": "https://www.atlassian.com/software/jira",
                "logo": "/docs/integration-logos/Jira.png",
                "tags": ["software"],
            }
        ],
        "operators": [
            {
                "integration-name": "Atlassian Jira",
                "python-modules": ["airflow.providers.atlassian.jira.operators.jira"],
            }
        ],
        "sensors": [
            {
                "integration-name": "Atlassian Jira",
                "python-modules": ["airflow.providers.atlassian.jira.sensors.jira"],
            }
        ],
        "hooks": [
            {
                "integration-name": "Atlassian Jira",
                "python-modules": ["airflow.providers.atlassian.jira.hooks.jira"],
            }
        ],
        "connection-types": [
            {
                "hook-class-name": "airflow.providers.atlassian.jira.hooks.jira.JiraHook",
                "connection-type": "jira",
            }
        ],
        "notifications": ["airflow.providers.atlassian.jira.notifications.jira.JiraNotifier"],
        "dependencies": [
            "apache-airflow>=2.9.0",
            "apache-airflow-providers-common-compat>=1.6.0",
            "atlassian-python-api>3.41.10",
        ],
        "devel-dependencies": [],
    }

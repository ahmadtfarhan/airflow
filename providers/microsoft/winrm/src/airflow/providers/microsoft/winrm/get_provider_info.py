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
        "package-name": "apache-airflow-providers-microsoft-winrm",
        "name": "Windows Remote Management (WinRM)",
        "description": "`Windows Remote Management (WinRM) <https://docs.microsoft.com/windows/win32/winrm/portal>`__\n",
        "state": "ready",
        "source-date-epoch": 1741509045,
        "versions": [
            "3.9.1",
            "3.9.0",
            "3.7.0",
            "3.6.1",
            "3.6.0",
            "3.5.1",
            "3.5.0",
            "3.4.0",
            "3.3.0",
            "3.2.2",
            "3.2.1",
            "3.2.0",
            "3.1.1",
            "3.1.0",
            "3.0.0",
            "2.0.5",
            "2.0.4",
            "2.0.3",
            "2.0.2",
            "2.0.1",
            "2.0.0",
            "1.2.0",
            "1.1.0",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Windows Remote Management (WinRM)",
                "external-doc-url": "https://docs.microsoft.com/en-us/windows/win32/winrm/portal",
                "logo": "/docs/integration-logos/WinRM.png",
                "how-to-guide": ["/docs/apache-airflow-providers-microsoft-winrm/operators.rst"],
                "tags": ["protocol"],
            }
        ],
        "operators": [
            {
                "integration-name": "Windows Remote Management (WinRM)",
                "python-modules": ["airflow.providers.microsoft.winrm.operators.winrm"],
            }
        ],
        "hooks": [
            {
                "integration-name": "Windows Remote Management (WinRM)",
                "python-modules": ["airflow.providers.microsoft.winrm.hooks.winrm"],
            }
        ],
        "dependencies": ["apache-airflow>=2.9.0", "pywinrm>=0.5.0"],
        "devel-dependencies": [],
    }

# Copyright 2015, Pinterest, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import imp
import fnmatch
import os


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


WORKFLOWS = {}

workflow_config_paths = find('workflow_config.py', 'betterment/datawarehouse/workflows')
for workflow_config_path in workflow_config_paths:
    workflow_config_module = imp.load_source('WorkflowConfig', workflow_config_path)
    workflow_config = workflow_config_module.WorkflowConfig().get()
    WORKFLOWS.update(workflow_config)



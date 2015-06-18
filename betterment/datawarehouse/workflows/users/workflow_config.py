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

from datetime import datetime
from datetime import timedelta

from pinball_ext.workflow.config import JobConfig
from pinball_ext.workflow.config import WorkflowConfig
from pinball_ext.workflow.config import ScheduleConfig
from pinball_ext.job_templates import JobTemplate
from pinball_ext.job_templates import CommandJobTemplate


class WorkflowConfig:
    FINAL_JOB = CommandJobTemplate('final', 'echo success')

    WORKFLOW = {
        'users': WorkflowConfig(
            jobs={
                'cmd_parent': JobConfig(CommandJobTemplate('ExamplePinballMagicCMD',
                                                           'echo PINBALL:EVENT_ATTR:a_cmd_key=a_cmd_value'), []),
                'python_parent': JobConfig(JobTemplate('ExamplePinballMagicPythonJob'), []),
                'child': JobConfig(CommandJobTemplate('CHILD', 'echo "child: %%(a_cmd_key)s %%(a_python_key)s"'),
                                   ['cmd_parent', 'python_parent']),
            },
            final_job_config=JobConfig(FINAL_JOB),
            schedule=ScheduleConfig(recurrence=timedelta(days=1),
                                    reference_timestamp=datetime(
                                        year=2015, month=1, day=1, second=1)),
            notify_emails='yuriy+pinball@betterment.com'),
    }

    def get(self):
        return self.WORKFLOW

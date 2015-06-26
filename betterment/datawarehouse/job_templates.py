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

from pinball_ext import job_templates

class DatabaseTableSyncJobTemplate(job_templates.JobTemplate):

    def __init__(self, name, executor=None, executor_config=None, write_lock=None,
                 max_attempts=1, emails=None, priority=None,
                 warn_timeout_sec=None, abort_timeout_sec=None, table_sync_config=None):
        super(DatabaseTableSyncJobTemplate, self).__init__(
            name=name,
            write_lock=write_lock,
            max_attempts=max_attempts,
            emails=emails,
            priority=priority,
            warn_timeout_sec=warn_timeout_sec,
            abort_timeout_sec=abort_timeout_sec)
        self._table_sync_config = table_sync_config if table_sync_config is not None else {}

    def get_pinball_job(self, inputs, outputs, params):
        # these are really workflow level params inherited by the job
        job_params = params.get('job_params', {})
        job_params.update(self._table_sync_config)
        params['job_params'] = job_params
        return super(DatabaseTableSyncJobTemplate, self).get_pinball_job(inputs, outputs, params)

    """A JobTemplate for syncing odbc accessible database tables"""
    def hello_world(self):
        print "I am DatabaseTableSyncJobTemplate"
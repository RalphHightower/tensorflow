# Copyright 2023 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================

class DispatchGrpcDataServer:
    def __init__(self, *args, **kwargs) -> None: ...
    def bound_port(self) -> int: ...
    def join(self) -> None: ...
    def num_workers(self) -> int: ...
    def snapshot_streams(self, *args, **kwargs): ...
    def start(self) -> Status: ...
    def stop(self) -> None: ...

class SnapshotStreamInfoWrapper:
    def __init__(self) -> None: ...
    @property
    def index(self) -> int: ...
    @property
    def state(self) -> int: ...

class SnapshotTaskProgressWrapper:
    def __init__(self) -> None: ...
    @property
    def completed(self) -> bool: ...
    @property
    def snapshot_task_base_path(self) -> bytes: ...
    @property
    def snapshot_task_stream_index(self) -> int: ...

class WorkerGrpcDataServer:
    def __init__(self, *args, **kwargs) -> None: ...
    def bound_port(self) -> int: ...
    def join(self) -> None: ...
    def num_tasks(self) -> int: ...
    def snapshot_task_progresses(self, *args, **kwargs): ...
    def start(self) -> Status: ...
    def stop(self) -> None: ...

def TF_DATA_GetDataServiceMetadataByID(*args, **kwargs): ...
def TF_DATA_NewDispatchServer(arg0: str) -> DispatchGrpcDataServer: ...
def TF_DATA_NewWorkerServer(arg0: str) -> WorkerGrpcDataServer: ...

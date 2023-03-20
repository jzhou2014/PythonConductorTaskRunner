from datetime import datetime
from conductor.client.http.models import Task, TaskResult
from conductor.client.http.models.task_result_status import TaskResultStatus
from conductor.client.worker.worker_interface import WorkerInterface


class SimplePythonWorker(WorkerInterface):
    def execute(self, task: Task) -> TaskResult:
        task_result = self.get_task_result_from_task(task)
        # ct stores current time
        ct = datetime.now()
        print(f"Current time: - {ct}")
        task_result.add_output_data("currentTimeOnServer", ct);
        task_result.add_output_data(
            "Message", "The simple python task runs successfully."
        )
        task_result.status = TaskResultStatus.COMPLETED
        return task_result

    def get_polling_interval_in_seconds(self) -> float:
        return 2

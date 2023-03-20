import config
import logging
import os
from conductor.client.automator.task_handler import TaskHandler
from task.example.SimplePythonWorker import SimplePythonWorker

workers = [
    SimplePythonWorker(task_definition_name="python_task_example"),
]

if os.environ.get("DEBUG") == "true":
    logging.basicConfig(
        filename="logs/workflow-python.log",
        encoding="utf-8",
        level=logging.DEBUG,
    )
else:
    print("logging not yet configured")

if __name__ == "__main__":
    print(" Python Workers Polling ")
    with TaskHandler(workers, config.conductor_config) as task_handler:
        task_handler.start_processes()
        task_handler.join_processes()

from repository import TaskRepository, CacheTask
from schema.task import TaskShema
from dataclasses import dataclass


@dataclass
class TaskService:
    task_repo: TaskRepository
    task_cache: CacheTask

    def get_tasks(self):
        if cache_task := self.task_cache.get_task():
            return cache_task
        else:
            tasks = self.task_repo.get_tasks()
            tasks_schema = [TaskShema.model_validate(task) for task in tasks]
            self.task_cache.set_task(tasks_schema)
            return tasks_schema

import json

from redis import Redis
from schema.task import TaskShema

class CacheTask:
    def __init__(self, redis_: Redis):
        self.redis_ = redis_

    def get_task(self) -> list[TaskShema]:
        with self.redis_ as red:
            task_json = red.lrange("tasks", 0, -1)
            return [TaskShema.model_validate(json.loads(task)) for task in task_json]


    def set_task(self, tasks: list[TaskShema]):
        tasks_json = [json.dumps(task.model_dump()) for task in tasks]
        self.redis_.delete("tasks")
        if tasks_json:
            self.redis_.lpush("tasks", *tasks_json)



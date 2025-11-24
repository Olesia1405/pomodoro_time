from typing import Annotated
from fastapi import APIRouter, status
from fastapi.params import Depends

from service import TaskService
from schema.task import TaskShema
from repository import TaskRepository, CacheTask
from dependency import get_task_repository, get_task_service

router = APIRouter(prefix="/task", tags=["task"])

@router.get(
    "/all",
    response_model=list[TaskShema]
)
async def get_tasks(
        task_service: Annotated[TaskService, Depends(get_task_service)]
):
    return task_service.get_tasks()


@router.post(
    "/",
    response_model=TaskShema
)
async def create_task(task: TaskShema, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task


@router.patch(
    "/{task_id}",
    response_model=TaskShema
)
async def patch_task(task_id: int, name: str, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    return task_repository.update_task_name(task_id, name)



@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    return task_repository.delete_task(task_id)

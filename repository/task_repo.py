from sqlalchemy import update, select, delete
from sqlalchemy.orm import Session
from models import Tasks, Categories
from schema import TaskShema


class TaskRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_tasks(self):
        with self.db_session() as session:
            tasks = session.execute(select(Tasks)).scalars().all()
        return tasks

    def get_task(self, task_id: int) -> Tasks | None:
        with self.db_session() as session:
            task = session.execute(select(Tasks).where(Tasks.id == task_id)).scalar_one_or_none()
            return task

    def create_task(self, task: TaskShema) -> int:
        task_model = Tasks(name=task.name, pomodoro_count=task.pomodoro_count, category_id=task.category_id)
        with self.db_session() as session:
            session.add(task_model)
            session.commit()
            return task_model.id

    def update_task_name(self, task_id: int, name: str):
        query = update(Tasks).where(Tasks.id == task_id).values(name=name).returning(Tasks.id)
        with self.db_session() as session:
            task_id: int = session.execute(query).scalar_one_or_none()
            return self.get_task(task_id)


    def delete_task(self, task_id: int) -> None:
        with self.db_session() as session:
            session.execute(delete(Tasks).where(Tasks.id == task_id))
            session.commit()

    def get_tasks_by_category_name(self, category_name: str) -> list[Tasks]:
        query = select(Tasks).join(Categories, Tasks.category_id == Categories.id).where(Categories.name == category_name)
        with self.db_session() as session:
            task: list[Tasks] = session.execute(query).scalars().all()
            return task





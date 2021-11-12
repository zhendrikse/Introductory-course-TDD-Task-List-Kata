from typing import List
from datetime import date
from typing import Union
from task import Task

class TaskList:
  def __init__(self, tasks: List[Task]) -> None:
    self.tasks = tasks

  def get_tasks_by_id(self, id:str) -> List[Task]:
    return [x for x in self.tasks if (x.get_id().id_string == id)]

  def has_task_with_id(self, id: str) -> bool:
    return len(self.get_tasks_by_id(id)) > 0

  def get_task_by_id(self, task_id: Union[int, str]) -> Task:
    id = task_id if type(task_id) is str else str(task_id)
    if not self.has_task_with_id(id):
      raise ValueError("No such task")
    return self.get_tasks_by_id(id)[0]

  def update_task(self, task_id: str, deadline: date) -> None:
      task = self.get_task_by_id(task_id)
      task.set_deadline(deadline)

  def is_empty(self) -> bool:
    return len(self.tasks) == 0

  def todays_tasks(self) -> List[Task]:
    return [x for x in self.tasks if x.get_deadline() == date.today()]
    #return filter(lambda x: x.due_date == date.today(), self.tasks)

from datetime import date
from task import Task, TaskId

class TaskList:
  def __init__(self):
    self.tasks = list()

  def today(self) -> list:
    return [x for x in self.tasks if x.due_date == date.today()]
    #return filter(lambda x: x.due_date == date.today(), self.tasks)

  def add(self, task: Task) -> None:
    if (self.contains_task(task)):
      raise ValueError("Task with given task ID already exists")
    self.tasks.append(task)

  def get_task(self, task_id: TaskId) -> Task:
    raise ValueError("No such task")

  def contains_task(self, task: Task) -> bool:
    id_exists = [x for x in self.tasks if (x.task_id == task.task_id)]
    return len(id_exists) > 0
    
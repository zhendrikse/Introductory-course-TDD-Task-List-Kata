from datetime import date
from task import Task 

class TaskList:
  def __init__(self):
    self.tasks = list()

  def today(self) -> list:
    return [x for x in self.tasks if x.due_date == date.today]
    #return filter(lambda x: x.due_date == date.today, self.tasks)

  def add(self, task: Task) -> None:
    self.tasks.append(task)
    
from typing import List
from datetime import datetime
from task import Task

class TaskList:
  def __init__(self, tasks: List[Task]) -> None:
    self.tasks = tasks

  def has_task_with_id(self, id: int) -> bool:
    id_exists = [x for x in self.tasks if (x.id == id)]
    return len(id_exists) > 0

  def get_task_by_id(self, id: int) -> Task:
    if not self.has_task_with_id(id):
      raise ValueError("No such task")
    return self.tasks[0]

  def is_empty(self) -> bool:
    return len(self.tasks) == 0

  def handle_query(self, querty: str) -> List[Task]:
    return []

  def handle_deadline_command(self, arguments:List[str]) -> None:
      if len(arguments) != 3:
        raise ValueError("Invalid arguments")
      task_id = int(arguments[1])
      task_date = datetime.strptime(arguments[2], '%d-%m-%Y').date()
      if len(self.tasks) == 0:
        raise ValueError("No such task")
      task = self.get_task_by_id(task_id)
      task.set_deadline(task_date)

  def handle_command(self, command: str) -> None:
    if command.startswith("deadline"):
      self.handle_deadline_command(command.split(" "))
      return 

    raise ValueError("Invalid command")
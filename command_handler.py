from typing import List
from datetime import datetime
from task_list import TaskList
from task_id import TaskId

class CommandHandler:
  def __init__(self, tasklist:TaskList) -> None:
    self.tasklist = tasklist

  def handle_deadline_command(self, arguments:List[str]) -> None:
      if len(arguments) != 3:
        raise ValueError("Invalid arguments")
      task_id = TaskId(arguments[1])
      task_date = datetime.strptime(arguments[2], '%d-%m-%Y').date()
      self.tasklist.update_task(task_id, task_date)

  def handle_command(self, command: str) -> None:
    if command.startswith("deadline"):
      self.handle_deadline_command(command.split(" "))
    else:
      raise ValueError("Invalid command")

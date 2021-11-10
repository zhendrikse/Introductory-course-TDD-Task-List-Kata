from datetime import date
from dataclasses import dataclass

class TaskId:
  def __init__(self, id: str):
    self.validate_id(id)
    self.id = id

  def validate_id(self, id:str) -> None:
    if (" " in id):
      raise ValueError("ID contains spaces")
    if not id.isalnum():
      raise ValueError("ID contains special characters")
  
  @classmethod
  def from_string(cls, id: str):
    return TaskId(id)

  @classmethod
  def from_int(cls, id: int):
    return TaskId(str(id))
  
  def __eq__(self, other) -> bool:
    if isinstance(other, TaskId):
        return self.id == other.id
    return False

@dataclass
class Task:
  task_id: TaskId
  description: str
  due_date: date = date.today()

  def __eq__(self, other) -> bool:
    if isinstance(other, Task):
        return self.task_id == other.task_id
    return False

  def set_deadline(self, due_date: date) -> None:
    self.due_date = due_date
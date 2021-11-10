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
  
  def __eq__(self, other):
    if isinstance(other, TaskId):
        return self.id == other.id
    return False

@dataclass(frozen = True)
class Task:
    task_id: TaskId
    description: str
    due_date: date = date.today()

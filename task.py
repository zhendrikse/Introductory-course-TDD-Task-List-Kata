from datetime import date
from dataclasses import dataclass

class TaskId:
  def __init__(self, id: str):
    self.id = id

  @classmethod
  def from_string(cls, id: str):
    return TaskId(id)

  @classmethod
  def from_int(cls, id: int):
    return TaskId(str(id))

@dataclass(frozen = True)
class Task:
    task_id: TaskId
    description: str
    due_date: date = date.today()

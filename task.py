from datetime import date
from typing import Union

class Task:
  def __init__(self, id:int, description: str) -> None:
    self.validate_parameters(id, description)

    self.description = description
    self.id = id
    self.deadline = date.today()
    self.has_deadline = False

  def get_deadline(self) -> Union[date, None]:
    return self.deadline if self.has_deadline else None

  def set_deadline(self, due_date:date) -> None:
    self.has_deadline = True
    self.deadline = due_date

  def validate_parameters(self, id:int, description: str) -> None:
    if id < 0:
      raise ValueError("ID cannot be negative")
    if not description:
      raise ValueError("Description cannot be empty")
  
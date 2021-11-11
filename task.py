from datetime import date
from typing import Union

class Task:
  def __init__(self, id:Union[int, str], description: str) -> None:
    self.validate_parameters(id, description)

    self.description = description
    self.id = id if type(id) is str else str(id)
    self.deadline = date.today()
    self.has_deadline = False

  def get_deadline(self) -> Union[date, None]:
    return self.deadline if self.has_deadline else None

  def set_deadline(self, due_date:date) -> None:
    self.has_deadline = True
    self.deadline = due_date

  def validate_string_id(self, id:str) -> None:
    if (" " in id):
      raise ValueError("ID contains spaces")
    if not id.isalnum():
      raise ValueError("ID contains special characters")

  def validate_int_id(self, id:int) -> None:
      if id < 0:
        raise ValueError("ID cannot be negative")

  def validate_parameters(self, id:Union[int, str], description: str) -> None:
    if type(id) is int:
      self.validate_int_id(id)
    elif type(id) is str:
      self.validate_string_id(id)

    if not description:
      raise ValueError("Description cannot be empty")
  
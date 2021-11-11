from datetime import date
from typing import Union

class Task:
  def __init__(self, id:Union[int, str], description: str) -> None:
    self.validate_id(id)
    self.validate_description(description)

    self.description = description
    self.id_int = -1 if type(id) is str else id
    self.id_string = id if type(id) is str else str(id)
    self.deadline = date.today()
    self.has_deadline = False

  def get_id(self) -> Union[int, str]:
    return self.id_string if self.id_int == -1 else self.id_int

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

  def validate_description(self, description:str) -> None:
    if not description:
      raise ValueError("Description cannot be empty")
  
  def validate_id(self, id:Union[int, str]) -> None:
    if type(id) is int:
      self.validate_int_id(id)
    if type(id) is str:
      self.validate_string_id(id)


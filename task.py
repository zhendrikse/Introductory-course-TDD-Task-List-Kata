from datetime import date

class Task:
  def __init__(self, id: int, description: str, due_date: date = date.today):
    self.id = id
    self.description = description
    self.due_date = due_date

from mamba import description, it, context, before
from expects import expect, equal, raise_error
from datetime import date
from task import Task

with description(Task) as self:
  with context("Given a new task without due date"):
    with before.each:
      self.my_task = Task(1, "Clean up living room") 

    with it("should have a description"):
      expect(self.my_task.description).to(equal("Clean up living room"))
    with it("should have a default due date of today"):
      expect(self.my_task.due_date).to(equal(date.today))
      

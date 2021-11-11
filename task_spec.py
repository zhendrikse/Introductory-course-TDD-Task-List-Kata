from mamba import description, it, context, before
from expects import expect, equal, raise_error, be_a
from datetime import date
from task import Task

with description(Task) as self:
  with description("Creating a task"):
    with it("should throw an exception when ID is negative"):
      expect(lambda: Task(-1, "todo")).to(raise_error(ValueError, "ID cannot be negative"))

    with it("should throw an exception when description is empty"):
      expect(lambda: Task(1, "")).to(raise_error(ValueError, "Description cannot be empty"))
    
    with it("should create a task when ID is non-negative"):
      expect(Task(0, "todo")).to(be_a(Task))

  with description("Given a task") as self:
    with before.each:
      self.task = Task(0, "todo")
    
    with it("should not have a deadline set"):
      expect(self.task.get_deadline()).to(equal(None))
    
    with it("should return deadline when set"):
      self.task.set_deadline(date.today())
      expect(self.task.get_deadline()).to(equal(date.today()))

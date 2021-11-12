from mamba import description, it, before
from expects import expect, equal, raise_error
from datetime import date
from task import Task, TaskId

with description(Task) as self:
  with description("Creating a task"):
    with it("should throw an exception when ID contains non-alphanumeric chars"):
      expect(lambda: Task(TaskId("1#2"), "todo")).to(raise_error(ValueError, "ID contains special characters"))

    with it("should throw an exception when description is empty"):
      expect(lambda: Task(TaskId(1), "")).to(raise_error(ValueError, "Description cannot be empty"))

  with description("Given a task") as self:
    with before.each:
      self.task = Task(TaskId(0), "todo")
    
    with it("should not have a deadline set"):
      expect(self.task.get_deadline()).to(equal(None))
    
    with it("should return deadline when set"):
      self.task.set_deadline(date.today())
      expect(self.task.get_deadline()).to(equal(date.today()))

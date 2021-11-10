from mamba import description, it, context, before
from expects import expect, equal, raise_error
from datetime import date
from task import Task, TaskId
from task_list import TaskList

with description(Task) as self:

  with context("Given a task with ID 1"):
    with before.each:
      self.task_1 = Task(TaskId.from_int(1), "TODO number 1") 
    with it("should be equal to another task with ID 1"):
      task_2 = Task(TaskId.from_int(1), "TODO number 2")
      expect(self.task_1).to(equal(task_2))
    with it("should be unequal to another task with ID 2"):
      task_2 = Task(TaskId.from_int(2), "TODO number 2")
      expect(self.task_1).to_not(equal(task_2))

  with context("Given a new task without due date"):
    with before.each:
      self.my_task = Task(TaskId.from_int(1), "Clean up living room") 

    with it("should have a default due date of today"):
      expect(self.my_task.due_date).to(equal(date.today()))

  with it("should throw an exception when ID contains a space"):
    expect(lambda: TaskId("1 2")).to(raise_error(ValueError, "ID contains spaces"))

  with it("should throw an exception when ID contains special characters"):
    expect(lambda: TaskId("1#3")).to(raise_error(ValueError, "ID contains special characters"))

with description(TaskId):
  with context("Given a task ID"):
    with it("should be equal to an equal ID"):
      expect(TaskId("123")).to(equal(TaskId("123")))
    with it("should be unequal to an unequal ID"):
      expect(TaskId("123")).not_to(equal(TaskId("1")))
    with it("should be unequal to another class"):
      expect(TaskId.from_string("123")).not_to(equal(TaskList()))
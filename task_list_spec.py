from mamba import description, it, context, before
from expects import expect, equal, be_empty, contain_exactly, raise_error
from datetime import date, timedelta
from task_list import TaskList
from task import Task, TaskId

with description(TaskList) as self:
  with context("Given a new task list"):
    with before.each:
      self.my_task_list = TaskList()
      self.new_task = Task(TaskId.from_int(1), "A new task")

    with it("should be empty"):
      expect(self.my_task_list.tasks).to(be_empty)

    with it("should throw an exception when requesting a task by ID"):
      expect(lambda: self.my_task_list.get_task(TaskId.from_string("1"))).to(raise_error(ValueError, "No such task"))

    with it("should be possible to add a task with an int as ID"):
      self.my_task_list.add(self.new_task)
      expect(self.my_task_list.tasks).not_to(be_empty)
      expect(self.my_task_list.tasks).to(contain_exactly(self.new_task))

    with it("should not be possible to add the same task twice"):
      self.my_task_list.add(self.new_task)
      expect(lambda: self.my_task_list.add(self.new_task)).to(raise_error(ValueError, "Task with given task ID already exists"))

    with it("should be possible to add a task with a string as ID"):
      my_task = Task(TaskId.from_string("1"), "Clean living room")
      self.my_task_list.add(my_task)
      expect(self.my_task_list.tasks).not_to(be_empty)
      expect(self.my_task_list.tasks).to(contain_exactly(my_task))
      
    with it("should have no tasks for today"):
      expect(self.my_task_list.today()).to(be_empty)

    with context("with a task added for tomorrow"):
      with before.each:
        tomorrow = date.today() + timedelta(days=1)
        self.my_task = Task(TaskId.from_int(1), "Clean living room", tomorrow)
        self.my_task_list.add(self.my_task)

      with it("should contain the task for tomorrow"):
        expect(self.my_task_list.tasks).to(contain_exactly(self.my_task))
      with it("should not list any tasks for today"):
        expect(self.my_task_list.today()).to(be_empty)

      with description("and a task for today added as well"):
        with it("should list one task for today"):
          task_today = Task(TaskId.from_int(2), "Clean bathroom")
          self.my_task_list.add(task_today)

          expect(self.my_task_list.today()).to(contain_exactly(task_today))
        

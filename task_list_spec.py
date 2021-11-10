from mamba import description, it, context, before
from expects import expect, equal, be_empty, contain_exactly
from datetime import date, timedelta
from task_list import TaskList
from task import Task

with description(TaskList) as self:
  with context("Given a new task list"):
    with before.each:
      self.my_task_list = TaskList()

    with it("should be empty"):
      expect(self.my_task_list.tasks).to(be_empty)
      
    with it("should have no tasks for today"):
      expect(self.my_task_list.today()).to(be_empty)

    with context("with a task added for tomorrow"):
      with before.each:
        tomorrow = date.today() + timedelta(days=1)
        self.my_task = Task(1, "Clean living room", tomorrow)
        self.my_task_list.add(self.my_task)

      with it("should contain the task for tomorrow"):
        expect(self.my_task_list.tasks).to(contain_exactly(self.my_task))
      with it("should not list any tasks for today"):
        expect(self.my_task_list.today()).to(be_empty)

      with description("and a task for today added as well"):
        with it("should list one task for today"):
          task_today = Task(2, "Clean bathroom")
          self.my_task_list.add(task_today)

          expect(self.my_task_list.today()).to(contain_exactly(task_today))
        

from mamba import description, it, context, before
from expects import expect, equal, be_empty, have_len, raise_error
from datetime import date, timedelta, datetime
from task_list import TaskList
from task import Task

with description(TaskList) as self:
  with context("Given a new empty task list"):
    with it("should be empty"):
      expect(TaskList([]).is_empty()).to(equal(True))

    with it("should throw exception when no task with given ID exists"):
      expect(lambda: TaskList([]).get_task_by_id(1)).to(raise_error(ValueError, "No such task"))

    with it("should return empty list when sent the today command"):
      expect(TaskList([]).handle_query("today")).to(be_empty)

  with context("Given a task list with one task"):
    with before.each:
      self.my_task_list = TaskList([Task(1, "todo")])

    with it("should not be empty"):
      expect(self.my_task_list.is_empty()).to(equal(False))

    with it("should return empty list when sent the today command"):
      expect(TaskList([]).handle_query("today")).to(be_empty)

    with description("And the deadline has been set unequal to today"):
      with before.each:
        self.my_task_list.handle_command("deadline 1 20-10-2021")
      
      with it("should have set the deadline for the contained task"):
        task = self.my_task_list.get_task_by_id(1)
        deadline = datetime.strptime("20-10-2021", '%d-%m-%Y').date()
        expect(task.get_deadline()).to(equal(deadline))
        
      with it("should return empty list when sent the today command"):
        expect(self.my_task_list.handle_query("today")).to(be_empty)

    with description("And the deadline has been set equal to today"):
      with it("should return list with single task due today"):
        today_as_string = datetime.today().strftime("%d-%m-%Y")
        self.my_task_list.handle_command("deadline 1 " + today_as_string)
        tasks_today = self.my_task_list.handle_query("today")
        expect(len(tasks_today)).to(equal(1))

  with context("Given a task list with two tasks"):
    with it("should not be empty"):
      my_task_list = TaskList([Task(1, "todo"), Task(2, "todo")])
      expect(my_task_list.is_empty()).to(equal(False))

  with description("When sending a command"):
    with it("should throw exception with empty command string"):
      expect(lambda: TaskList([]).handle_command("")).to(raise_error(ValueError, "Invalid command"))

    with context("When sending a deadline command"):
      with it("should throw exception when command does not start with deadline keyword"):      
        expect(lambda: TaskList([]).handle_command("deedlien")).to(raise_error(ValueError, "Invalid command"))

      with it("should throw exception when command is not followed by an ID"):      
        expect(lambda: TaskList([]).handle_command("deadline")).to(raise_error(ValueError, "Invalid arguments"))     

      with it("should throw exception when ID is not followed by a date"):      
        expect(lambda: TaskList([]).handle_command("deadline 1")).to(raise_error(ValueError, "Invalid arguments"))         

      with it("should throw exception when ID is not an integer"):
        expect(lambda: TaskList([]).handle_command("deadline a 20-11-2021")).to(raise_error(ValueError))

      with it("should throw exception when date is not a date"):
        expect(lambda: TaskList([]).handle_command("deadline 1 ab-11-2021")).to(raise_error(ValueError))

      with it("should throw exception when no task with given ID exists"):
        expect(lambda: TaskList([]).handle_command("deadline 1 20-11-2021")).to(raise_error(ValueError, "No such task"))

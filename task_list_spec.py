from mamba import description, it, context, before
from expects import expect, equal, be_empty, raise_error
from datetime import datetime
from task_list import TaskList
from task import Task
from command_handler import CommandHandler
from query_handler import QueryHandler

with description(TaskList) as self:
  with context("Given a new empty task list"):
    with it("should be empty"):
      expect(TaskList([]).is_empty()).to(equal(True))

    with it("should throw exception when no task with given ID exists"):
      expect(lambda: TaskList([]).get_task_by_id(1)).to(raise_error(ValueError, "No such task"))

    with description("When sending today query"):
      with it("should return empty list"):
        expect(QueryHandler(TaskList([])).handle_query("today")).to(be_empty)

    with description("When sending an empty command"):
      with it("should throw exception with empty command string"):
        expect(
          lambda: CommandHandler(TaskList([])).handle_command("")
        ).to(raise_error(ValueError, "Invalid command"))

    with context("When sending a deadline command"):
      with before.each:
        self.command_handler = CommandHandler(TaskList([]))

      with it("should throw exception when command does not start with deadline keyword"):      
        expect(
          lambda: self.command_handler.handle_command("deedlien")
        ).to(raise_error(ValueError, "Invalid command"))

      with it("should throw exception when command is not followed by an ID"):
        expect(
          lambda: self.command_handler.handle_command("deadline")
        ).to(raise_error(ValueError, "Invalid arguments"))     

      with it("should throw exception when ID is not followed by a date"):
        expect(
          lambda: self.command_handler.handle_command("deadline 1")
        ).to(raise_error(ValueError, "Invalid arguments"))         

      with it("should throw exception when ID is not an integer"):
        expect(
          lambda: self.command_handler.handle_command("deadline a 20-11-2021")
        ).to(raise_error(ValueError))

      with it("should throw exception when date is not a date"):
        expect(
          lambda: self.command_handler.handle_command("deadline 1 ab-11-2021")
        ).to(raise_error(ValueError))

      with it("should throw exception when no task with given ID exists"):
        expect(
          lambda: self.command_handler.handle_command("deadline 1 20-11-2021")
        ).to(raise_error(ValueError, "No such task"))

  with context("Given a task list with one task"):
    with before.each:
      self.my_task_list = TaskList([Task(1, "todo")])

    with it("should not be empty"):
      expect(self.my_task_list.is_empty()).to(equal(False))

    with it("should return empty list when sent the today query"):
      expect(QueryHandler(self.my_task_list).handle_query("today")).to(be_empty)

    with it("should throw exception when deadline command is given wrong ID"):
      expect(
        lambda: CommandHandler(self.my_task_list).handle_command("deadline 11 20-11-2021")
      ).to(raise_error(ValueError, "No such task"))

    with description("And the deadline has been set unequal to today"):
      with before.each:
        CommandHandler(self.my_task_list).handle_command("deadline 1 20-10-2021")
      
      with it("should have set the deadline for the contained task"):
        task = self.my_task_list.get_task_by_id(1)
        deadline = datetime.strptime("20-10-2021", '%d-%m-%Y').date()
        expect(task.get_deadline()).to(equal(deadline))
        
      with it("should return empty list when sent the today query"):
        expect(QueryHandler(self.my_task_list).handle_query("today")).to(be_empty)

    with description("And the deadline has been set equal to today"):
      with it("should return list with single task due today"):
        today_as_string = datetime.today().strftime("%d-%m-%Y")
        CommandHandler(self.my_task_list).handle_command("deadline 1 " + today_as_string)
        tasks_today = QueryHandler(self.my_task_list).handle_query("today")
        expect(len(tasks_today)).to(equal(1))

  with context("Given a task list with two tasks"):
    with before.each:
      self.task1 = Task(1, "todo")
      self.task2 = Task(2, "todo")
      self.my_task_list = TaskList([self.task1, self.task2])

    with it("should not be empty"):
      expect(self.my_task_list.is_empty()).to(equal(False))

    with it("should be able to retrieve second task by ID"):
      expect(self.my_task_list.get_task_by_id(2)).to(equal(self.task2))


## Features

You should be able to give the list with tasks the following commands:

1. Deadlines
  - Give each task an optional deadline with the `deadline <ID> <date>` command.
  - Show all tasks due today with the `today` command.
2. Customisable IDs
  - Allow the user to specify an identifier that’s not a number.
  - Disallow spaces and special characters from the ID.
3. Deletion
  - Allow users to delete tasks with the `delete <ID>` command.
4. Views
  - View tasks by date with the `view by date` command.
  - View tasks by deadline with the `view by deadline` command.
  - Don’t remove the functionality that allows users to view tasks by project, but change the command to `view by project`.

## Getting started

Make a plan

1. Create a task with a mandatory integer ID and description as string
  - Tasks with equal ID should be equal
  - Tasks with negative ID should not be allowed
  - Empty descriptions should not be allowed
2. Create an empty task list
  - Should be empty
  - Should throw an exception when requesting a task by ID
3. Adding tasks
  - Should be able to accept a new task with integer ID
  - Should throw an exception if the same new task is added twice


### References

- [Task list kata](https://kata-log.rocks/task-list-kata)
- [Expects matchers](https://expects.readthedocs.io/en/stable/matchers.html#)
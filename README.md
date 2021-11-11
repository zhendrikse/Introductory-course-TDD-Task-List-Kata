# The Kata

## Features

You should be able to give the list with tasks the following commands:

1. Deadlines
  - Give each task an optional deadline with the `deadline <ID> <date>` command.
  - Show all tasks due today with the `today` query.
2. Customisable IDs
  - Allow the user to specify an identifier that’s not a number.
  - Disallow spaces and special characters from the ID.
3. Deletion
  - Allow users to delete tasks with the `delete <ID>` command.
4. Views
  - View tasks by date with the `view by date` query.
  - View tasks by deadline with the `view by deadline` query.
  - Don’t remove the functionality that allows users to view tasks by project, but change the query to `view by project`.

Please also take into consideration the [Considerations and Approaches](https://kata-log.rocks/task-list-kata) section from the original kata description.

# Implementation

Let's implement the requirements one by one.

## Implementing the deadline command

As discussed in the first course, let's first make a plan.

### Making a plan first

1. Create a task with a mandatory integer ID and description as string
    - Tasks with negative ID should not be allowed
    - Empty descriptions should not be allowed
    - Deadline should not be set initially
2. Create an empty task list
    - Should be empty
    - Should throw an exception when requesting a task by ID
3. Create a filled task list
    - Make the constructor accept an empty task list
    - Make the constructor accept a task list with a single task
    - Make the constructor accpet a task list with two tasks
4. Make the task list accept the `deadline <ID> <date>` command
    - Throw an exception when the command token is not `deadline`
    - Throw an exception if the `deadline` is not followed by an integer and date
    - Throw an exception when task with `<ID>` does not exist
    - Should fire and forget when task with `<ID>` exists, but task due date must be set
5. Make the task list accept the `today` command, which returns all tasks due today
    - Make the command return an empty list when invoked on an empty task list
    - Make the command return the task of today after setting deadline of a task to today
    - Make the command return an empty list after setting deadline of a task to tomorrow


### References

- [Task list kata](https://kata-log.rocks/task-list-kata)
- [Expects matchers](https://expects.readthedocs.io/en/stable/matchers.html#)
- [Mamba PDF doc](https://readthedocs.org/projects/mamba-bdd/downloads/pdf/latest/)
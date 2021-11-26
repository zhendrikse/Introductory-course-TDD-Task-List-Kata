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

Please also take into consideration the [Considerations and Approaches](https://kata-log.rocks/task-list-kata) section from the original kata description. At least alwyas segregate commands (that don't return anything and modify the state of the system) and queries (returning values but leaving the state of the system invariant).

Last but not least: verify all the time you have 100% test coverage. As soon as you get below 100%, you wrote production code that you did not specify/test yet!

# Implementation

Let's implement the requirements one by one.

## Implementing the deadline command

As discussed in the first course, let's first make a plan.

### Making a plan first

Like the stack kata, we'll start with an empty task list first. The simplest thing that could possibly work!

1. An new/empty task list
    - Contains zero tasks / has a zero task count (hint!)
    - Throws an exception when we request a task by ID
2. Implement the possibility to add one or more tasks to the task list
    - Verify that the task(s) is/are returned when getting the list of tasks
    - Verify that the right task(s) is/are returned when retrieved by ID
    - Specify we expect an exception when you try to add another task with an existing ID
3. Make the task list accept the `deadline <ID> <date>` command
    - Throw an exception when the command token is not `deadline`
    - Throw an exception if the `deadline` is not followed by an integer and date
    - Throw an exception when task with `<ID>` does not exist
    - Should fire and forget when task with `<ID>` exists, but task due date must be set
5. Make the task list accept the `today` command, which returns all tasks due today
    - Make the command return an empty list when invoked on an empty task list
    - Make the command return the task of today after setting deadline of a task to today
    - Make the command return an empty list after setting deadline of a task to tomorrow

## Implementing ID as string

The main challenge here is to generalze the existing code base in (extremely) small steps. A possible solution is to use Python's unions:

```python
class Task:
  def __init__(self, id:Union[int, str], description: str) -> None:
```

These type cases can then be distinguished like so: 

```python
  def validate_id(self, id:Union[int, str]) -> None:
    if type(id) is int:
      self.validate_int_id(id)
    if type(id) is str:
      self.validate_string_id(id)
```

### Refactoring: single responsibility principle

#### Task ID

You may want to move the task ID related logic into its own (value) object. 

#### Command handling

Command handling should not be a responsibility of the task list. The command handling logic should therefore also be moved to its own classes.

## Implementing the delete command


### References

- [Task list kata](https://kata-log.rocks/task-list-kata)
- [Expects matchers](https://expects.readthedocs.io/en/stable/matchers.html#)
- [Mamba PDF doc](https://readthedocs.org/projects/mamba-bdd/downloads/pdf/latest/)
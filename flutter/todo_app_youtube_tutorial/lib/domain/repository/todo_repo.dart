/*

TO DO REPOSITORY

Here you define what the app can do.

*/

import 'package:todo_app_youtube_tutorial/domain/models/todo.dart';

abstract class TodoRepo {
  // get list of todos
  Future<List<Todo>> getTodos();

  // add a new todo
  Future<Todo> addTodo(Todo newTodo);

  // update an existing todo
  Future<Todo> updateTodo(Todo todo);

  // delete a todo
  Future<Todo> deleteTodo(Todo todo);
}

/*

Notes:

- the repo in the domain layer otlines what operations the app can do,
  but doesn't worry about the specific implementation details. That's for
  the data layer.

- technology agnostic: independant of any technology or framework.

*/

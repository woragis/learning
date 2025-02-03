/*

DATABASE REPO

This implements the todo repo and handles storing, retrieving, updating,
deleting to isar database.

*/

import 'package:isar/isar.dart';
import 'package:todo_app_youtube_tutorial/data/models/isar_todo.dart';
import 'package:todo_app_youtube_tutorial/domain/models/todo.dart';
import 'package:todo_app_youtube_tutorial/domain/repository/todo_repo.dart';

class IsarTodoRepo implements TodoRepo {
  // database
  final Isar db;
  TodoIsar todoIsars;

  IsarTodoRepo(this.db);

  // get todos
  @override
  Future<List<Todo>> getTodos() async {
    // fetch from db
    final todos = await db.todoIsars.where().findAll();

    // return list of todos
    return todos.map((todoIsar) => todoIsar.toDomain()).toList();
  }
  // add todo
  // update todo
  // delete todo
}

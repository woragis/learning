import 'package:sqflite/sqflite.dart';

class Todo {
  final int? id;
  final String title;
  final String description;
  final String? createdAt;

  Todo({
    this.id,
    required this.title,
    required this.description,
    this.createdAt,
  });
}

class SqlHelper {
  late final Database database;

  Future<Database> db() async {
    database = await openDatabase("main.db",
        onCreate: (Database db, int version) async {
      await db.execute("""
      CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        title TEXT,
        description TEXT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
      );""");
    });
    return database;
  }

  Future<List<Todo>> readTodos(Database db, String tableName, Todo todo) async {
    String stmt = "SELECT * FROM $tableName";
    await db.rawQuery(stmt, []);
  }

  Future<Todo> readTodoById(Database db, String tableName, Todo todo) async {
    String stmt = "SELECT * FROM $tableName WHERE id = ?;";
    await db.rawQuery(stmt, [todo.id]);
  }

  Future<Todo> createTodo(Database db, String tableName, Todo todo) async {
    String stmt =
        "INSERT INTO $tableName (title, description) VALUES (?, ?) RETURNING id, created_at;";
    await db.rawInsert(stmt, [todo.title, todo.description]);
  }

  Future<Todo> updateTodo(Database db, String tableName, Todo todo) async {
    String stmt =
        "UPDATE $tableName SET title = ?, description = ? WHERE id = ?;";
    await db.rawUpdate(stmt, [todo.title, todo.description, todo.id]);
  }

  Future<void> deleteTodo(Database db, String tableName, Todo todo) async {
    String stmt = "DELETE FROM $tableName WHERE id = ?;";
    await db.rawDelete(stmt, [todo.id]);
  }
}

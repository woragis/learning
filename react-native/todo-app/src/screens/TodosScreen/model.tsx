import { TodoInterface } from '@/src/types/todo.types'
import { useState } from 'react'

export const useTodosScreenModel = () => {
  const [todo, setTodo] = useState<string>('')
  const [todoList, setTodoList] = useState<TodoInterface[]>([])
  const [editedTodo, setEditedTodo] = useState<TodoInterface | undefined>(
    {} as TodoInterface
  )

  const handleTodoChange = (userText: string) => {
    setTodo(userText)
  }

  const handleTodoSubmit = () => {
    if (todo.length === 0) return
    setTodoList(
      (prev) => (prev = [...prev, { id: Date.now().toString(), title: todo }])
    )
    setTodo('')
  }

  const handleTodoDelete = (id: string) => {
    setTodoList((prev) => (prev = prev.filter((todo) => todo.id !== id)))
  }

  const handleTodoEdit = (todo: TodoInterface) => {
    setTodo(todo.title)
    setEditedTodo(todo)
  }

  const handleTodoEditSubmit = () => {
    if (todo.length === 0) return
    if (editedTodo) {
      setTodoList(
        (prev) => (prev = prev.filter((todo) => todo.id !== editedTodo.id))
      )
      setTodoList(
        (prev) => (prev = [...prev, { id: editedTodo.id, title: todo }])
      )
      setTodo('')
      setEditedTodo(undefined)
    }
  }

  return {
    editedTodo,
    handleTodoChange,
    handleTodoDelete,
    handleTodoEdit,
    handleTodoEditSubmit,
    handleTodoSubmit,
    todo,
    todoList,
  }
}

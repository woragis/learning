import { useAppDispatch, useAppSelector } from '@/src/redux/hooks'
// import { addTodo, deleteTodo, editTodo } from '@/src/redux/todos/actions'
import {
  todosAddAsync,
  todosDeleteAsync,
  todosEditAsync,
} from '@/src/redux/todos/thunks'
import { TodoInterface } from '@/src/types/todo.types'
import { useState } from 'react'

export const useTodosScreenModel = () => {
  const { todos, loading, error } = useAppSelector((state) => state.todos)
  const todoInitialState: TodoInterface = {
    id: '',
    title: '',
    description: '',
    completed: false,
    author_id: '',
  }

  const [todo, setTodo] = useState<TodoInterface>(todoInitialState)

  const [editedTodo, setEditedTodo] = useState<TodoInterface | undefined>(
    undefined
  )

  const handleTodoChange = (userText: string) => {
    setTodo((prev) => (prev = { ...prev, title: userText }))
  }

  const dispatch = useAppDispatch()
  const handleTodoSubmit = () => {
    if (todo.title.length === 0) return
    // dispatch(addTodo(todo))
    dispatch(todosAddAsync(todo))
    setTodo(todoInitialState)
  }

  const handleTodoDelete = (todo: TodoInterface) => {
    // dispatch(deleteTodo(todo))
    dispatch(todosDeleteAsync(todo))
  }

  const handleTodoEdit = (todo: TodoInterface) => {
    setTodo(todo)
    setEditedTodo(todo)
  }

  const handleTodoEditSubmit = () => {
    if (todo.title.length === 0 || !editedTodo) return
    // dispatch(editTodo(editedTodo))
    dispatch(todosEditAsync(todo))
    setTodo(todoInitialState)
    setEditedTodo(undefined)
  }

  return {
    editedTodo,
    error,
    handleTodoChange,
    handleTodoDelete,
    handleTodoEdit,
    handleTodoEditSubmit,
    handleTodoSubmit,
    loading,
    todo,
    todos,
  }
}

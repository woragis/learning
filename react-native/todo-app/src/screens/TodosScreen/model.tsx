import { useAppDispatch, useAppSelector } from '@/src/redux/hooks'
import todosApi from '@/src/redux/todos/apiSlice'
// import { addTodo, deleteTodo, editTodo } from '@/src/redux/todos/actions'
import { TodoInterface } from '@/src/types/todo.types'
import { useState } from 'react'
import {
  todosAddAsync,
  todosDeleteAsync,
  todosEditAsync,
} from '@/src/redux/todos/thunks'

export const useTodosScreenModel = () => {
  const dispatch = useAppDispatch()
  const { todos, loading, error } = useAppSelector((state) => state.todos)
  const [addTodoApi, { data, isLoading }] = todosApi.usePostTodoMutation()

  const todoInitialState: TodoInterface = {
    title: '',
    description: 'Random',
    author_id: 'f03576b9-b62e-4c36-a2ef-ad3aaa2a71fa',
  }

  const [todo, setTodo] = useState<TodoInterface>(todoInitialState)

  const [editedTodo, setEditedTodo] = useState<TodoInterface | undefined>(
    undefined
  )

  const handleTodoChange = (userText: string) => {
    setTodo((prev) => (prev = { ...prev, title: userText }))
  }

  const handleTodoSubmit = () => {
    if (todo.title.length === 0) return
    dispatch(todosAddAsync(todo))
    setTodo(todoInitialState)
  }

  const handleTodoDelete = (todo: TodoInterface) => {
    dispatch(todosDeleteAsync(todo))
  }

  const handleTodoEdit = (todo: TodoInterface) => {
    setTodo(todo)
    setEditedTodo(todo)
  }

  const handleTodoEditSubmit = () => {
    if (todo.title.length === 0 || !editedTodo) return
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

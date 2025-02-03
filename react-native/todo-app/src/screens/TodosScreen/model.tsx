import { useAppDispatch, useAppSelector } from '@/src/redux/hooks'
import todosApi from '@/src/redux/todos/apiSlice'
import { addTodo, deleteTodo, editTodo } from '@/src/redux/todos/actions'
// import {
//   todosAddAsync,
//   todosDeleteAsync,
//   todosEditAsync,
// } from '@/src/redux/todos/thunks'
import { TodoInterface } from '@/src/types/todo.types'
import { useState } from 'react'

export const useTodosScreenModel = () => {
  const dispatch = useAppDispatch()
  const { todos, loading, error } = useAppSelector((state) => state.todos)
  const [addTodoApi, { data, isLoading }] = todosApi.usePostTodoMutation()

  const [todo, setTodo] = useState<TodoInterface>({} as TodoInterface)

  const [editedTodo, setEditedTodo] = useState<TodoInterface | undefined>(
    undefined
  )

  const handleTodoChange = (userText: string) => {
    setTodo((prev) => (prev = { ...prev, title: userText }))
  }

  const handleTodoSubmit = () => {
    if (todo.title.length === 0) return
    dispatch(addTodo({ ...todo, id: Date.now().toString() }))
    setTodo({ title: '' } as TodoInterface)
  }

  const handleTodoDelete = (todo: TodoInterface) => {
    dispatch(deleteTodo(todo))
  }

  const handleTodoEdit = (todo: TodoInterface) => {
    setTodo(todo)
    setEditedTodo(todo)
  }

  const handleTodoEditSubmit = () => {
    if (todo.title.length === 0 || !editedTodo) return
    dispatch(editTodo(todo))
    setTodo({ title: '' } as TodoInterface)
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

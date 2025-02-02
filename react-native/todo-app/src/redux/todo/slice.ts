import { TodoState } from '@/src/types/redux.types'
import { TodoInterface } from '@/src/types/todo.types'
import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import addAsyncBulider from './builder/addAsync'
import editAsyncBulider from './builder/editAsync'
import deleteAsyncBulider from './builder/deleteAsync'

export const todosSlice = createSlice({
  name: 'todos',
  initialState: {} as TodoState,
  reducers: {
    addTodo: (state, action: PayloadAction<TodoInterface>) => {
      state.todos.push(action.payload)
    },
    editTodo: (state, action: PayloadAction<TodoInterface>) => {
      let updatedTodo = action.payload
      let oldTodos = state.todos.filter((todo) => todo.id !== updatedTodo.id)
      oldTodos.push(updatedTodo)
      state.todos = oldTodos
    },
    deleteTodo: (state, action: PayloadAction<TodoInterface>) => {
      state.todos.filter((todo) => todo.id !== action.payload.id)
    },
  },
  extraReducers: (builder) => {
    addAsyncBulider(builder)
    editAsyncBulider(builder)
    deleteAsyncBulider(builder)
  },
})

export default todosSlice

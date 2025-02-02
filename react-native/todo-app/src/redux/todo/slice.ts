import { TodoState } from '@/src/types/redux.types'
import { TodoInterface } from '@/src/types/todo.types'
import { createSlice, PayloadAction } from '@reduxjs/toolkit'

export const todoSlice = createSlice({
  name: 'todos',
  initialState: {} as TodoState,
  reducers: {
    add: (state, action: PayloadAction<TodoInterface>) => {
      state.todos.push(action.payload)
    },
    edit: (state, action: PayloadAction<TodoInterface>) => {
      let updatedTodo = action.payload
      let oldTodos = state.todos.filter((todo) => todo.id !== updatedTodo.id)
      oldTodos.push(updatedTodo)
      state.todos = oldTodos
    },
    delete: (state, action: PayloadAction<TodoInterface>) => {
      state.todos = state.todos.filter((todo) => todo.id !== action.payload.id)
    },
  },
  extraReducers: (builder) => {},
})

export default todoSlice.reducer

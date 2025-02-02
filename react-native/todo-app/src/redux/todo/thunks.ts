import { TodoInterface } from '@/src/types/todo.types'
import { createAsyncThunk } from '@reduxjs/toolkit'

export const todosAddAsync = createAsyncThunk(
  'todos/add',
  async (todo: TodoInterface) => {
    // Axios/React Query request
  }
)

export const todosEditAsync = createAsyncThunk(
  'todos/edit',
  async (todo: TodoInterface) => {
    // Axios/React Query request
  }
)

export const todosDeleteAsync = createAsyncThunk(
  'todos/delete',
  async (todo: TodoInterface) => {
    // Axios/React Query request
  }
)

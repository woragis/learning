import { DeleteResponse, TodoRepsonse } from '@/src/types/response.types'
import { TodoInterface } from '@/src/types/todo.types'
import { createAsyncThunk } from '@reduxjs/toolkit'
import axios from 'axios'

const BASE_URL = 'http://localhost:8080/todos'

export const todosAddAsync = createAsyncThunk(
  'todos/add',
  async (todo: TodoInterface) => {
    const response = await axios.post<TodoRepsonse>(`${BASE_URL}/`, todo)

    return response.data.data
  }
)

export const todosEditAsync = createAsyncThunk(
  'todos/edit',
  async (todo: TodoInterface) => {
    const response = await axios.put<TodoRepsonse>(
      `${BASE_URL}/${todo.id}`,
      todo
    )

    return response.data.data
  }
)

export const todosDeleteAsync = createAsyncThunk(
  'todos/delete',
  async (todo: TodoInterface) => {
    const response = await axios.delete<DeleteResponse>(
      `${BASE_URL}/${todo.id}`
    )

    // return response.data.data
    return todo.id
  }
)

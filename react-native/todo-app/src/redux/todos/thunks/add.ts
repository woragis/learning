import { TodoRepsonse } from '@/src/types/response.types'
import { TodoInterface } from '@/src/types/todo.types'
import {
  ActionReducerMapBuilder,
  createAsyncThunk,
  PayloadAction,
} from '@reduxjs/toolkit'
import { TODOS_BASE_URL } from '.'
import { TodosState } from '@/src/types/redux.types'
import axios from 'axios'

export const todosAddAsync = createAsyncThunk(
  'todos/add',
  async (todo: TodoInterface) => {
    const response = await axios.post<TodoRepsonse>(`${TODOS_BASE_URL}/`, todo)

    return response.data.data
  }
)

const addAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(todosAddAsync.fulfilled, (state, action: PayloadAction<any>) => {
      state.loading = false
      state.error = undefined
      state.todos.push(action.payload)
    })
    .addCase(todosAddAsync.pending, (state) => {
      state.loading = true
      state.error = undefined
    })
    .addCase(todosAddAsync.rejected, (state) => {
      state.loading = false
      state.error = 'Erro ao tentar criar todo'
    })
}

export default addAsyncBulider

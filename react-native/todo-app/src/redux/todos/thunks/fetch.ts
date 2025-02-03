import { TodosRepsonse } from '@/src/types/response.types'
import { createAsyncThunk } from '@reduxjs/toolkit'
import { TODOS_BASE_URL } from '.'
import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder, PayloadAction } from '@reduxjs/toolkit'
import axios from 'axios'

export const todosFetchAsync = createAsyncThunk('todos/fetch', async () => {
  const response = await axios.get<TodosRepsonse>(`${TODOS_BASE_URL}/`)

  return response.data.data
})

const fetchAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(todosFetchAsync.fulfilled, (state, action: PayloadAction<any>) => {
      state.loading = false
      state.error = undefined
      state.todos = action.payload
    })
    .addCase(todosFetchAsync.pending, (state) => {
      state.loading = true
      state.error = undefined
    })
    .addCase(todosFetchAsync.rejected, (state) => {
      state.loading = false
      state.error = 'Erro ao tentar achar todos'
    })
}

export default fetchAsyncBulider

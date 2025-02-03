import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder, PayloadAction } from '@reduxjs/toolkit'
import { DeleteResponse } from '@/src/types/response.types'
import { TodoInterface } from '@/src/types/todo.types'
import { createAsyncThunk } from '@reduxjs/toolkit'
import axios from 'axios'
import { TODOS_BASE_URL } from '.'

export const todosDeleteAsync = createAsyncThunk(
  'todos/delete',
  async (todo: TodoInterface) => {
    await axios.delete<DeleteResponse>(`${TODOS_BASE_URL}/${todo.id}`)

    return todo.id
  }
)

const deleteAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(
      todosDeleteAsync.fulfilled,
      (state, action: PayloadAction<any>) => {
        state.loading = false
        state.error = undefined
        state.todos = state.todos.filter((todo) => todo.id !== action.payload)
      }
    )
    .addCase(todosDeleteAsync.pending, (state, action) => {
      state.loading = true
      state.error = undefined
    })
    .addCase(todosDeleteAsync.rejected, (state, action) => {
      state.loading = false
      state.error = 'Erro ao tentar deletar todo'
    })
}

export default deleteAsyncBulider

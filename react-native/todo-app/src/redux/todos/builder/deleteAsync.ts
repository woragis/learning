import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder, PayloadAction } from '@reduxjs/toolkit'
import { todosDeleteAsync } from '../thunks'

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

import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder } from '@reduxjs/toolkit'
import { todosDeleteAsync } from '../thunks'

const deleteAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(todosDeleteAsync.fulfilled, (state, action) => {
      state.loading = false
    })
    .addCase(todosDeleteAsync.pending, (state, action) => {
      state.loading = true
    })
    .addCase(todosDeleteAsync.rejected, (state, action) => {
      state.loading = false
    })
}

export default deleteAsyncBulider

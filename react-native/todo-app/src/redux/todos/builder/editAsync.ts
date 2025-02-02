import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder } from '@reduxjs/toolkit'
import { todosEditAsync } from '../thunks'

const editAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(todosEditAsync.fulfilled, (state, action) => {
      state.loading = false
    })
    .addCase(todosEditAsync.pending, (state, action) => {
      state.loading = true
    })
    .addCase(todosEditAsync.rejected, (state, action) => {
      state.loading = false
    })
}

export default editAsyncBulider

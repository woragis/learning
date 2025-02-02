import { TodoState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder } from '@reduxjs/toolkit'
import { todosAddAsync } from '../thunks'

const addAsyncBulider = (builder: ActionReducerMapBuilder<TodoState>) => {
  builder
    .addCase(todosAddAsync.fulfilled, (state, action) => {
      state.loading = false
    })
    .addCase(todosAddAsync.pending, (state, action) => {
      state.loading = true
    })
    .addCase(todosAddAsync.rejected, (state, action) => {
      state.loading = false
    })
}

export default addAsyncBulider

import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder, PayloadAction } from '@reduxjs/toolkit'
import { todosFetchAsync } from '../thunks'

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

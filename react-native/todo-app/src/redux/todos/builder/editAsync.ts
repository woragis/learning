import { TodosState } from '@/src/types/redux.types'
import { ActionReducerMapBuilder, PayloadAction } from '@reduxjs/toolkit'
import { todosEditAsync } from '../thunks'
import { TodoInterface } from '@/src/types/todo.types'

const editAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(todosEditAsync.fulfilled, (state, action: PayloadAction<any>) => {
      state.loading = false
      state.error = undefined
      state.todos
        .filter((todo) => todo.id !== action.payload.id)
        .push(action.payload)
    })
    .addCase(todosEditAsync.pending, (state, action) => {
      state.loading = true
      state.error = undefined
    })
    .addCase(todosEditAsync.rejected, (state, action) => {
      state.loading = false
      state.error = 'Erro ao adicionar Todo'
    })
}

export default editAsyncBulider

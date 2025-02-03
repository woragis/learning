import { TodosState } from '@/src/types/redux.types'
import {
  ActionReducerMapBuilder,
  AsyncThunkAction,
  AsyncThunkPayloadCreatorReturnValue,
  PayloadAction,
} from '@reduxjs/toolkit'
import { todosAddAsync } from '../thunks'
import { TodoInterface } from '@/src/types/todo.types'

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

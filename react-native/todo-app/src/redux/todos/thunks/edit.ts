import { TodoRepsonse } from '@/src/types/response.types'
import { TodoInterface } from '@/src/types/todo.types'
import {
  ActionReducerMapBuilder,
  createAsyncThunk,
  PayloadAction,
} from '@reduxjs/toolkit'
import { TODOS_BASE_URL } from '.'
import { TodosState } from '@/src/types/redux.types'

const todosEditAsync = createAsyncThunk(
  'todos/edit',
  async (todo: TodoInterface) => {
    const response = await axios.put<TodoRepsonse>(
      `${TODOS_BASE_URL}/${todo.id}`,
      todo
    )

    return response.data.data
  }
)

const editAsyncBulider = (builder: ActionReducerMapBuilder<TodosState>) => {
  builder
    .addCase(todosEditAsync.fulfilled, (state, action: PayloadAction<any>) => {
      state.loading = false
      state.error = undefined
      state.todos = state.todos.map((todo) => {
        if (todo.id === action.payload.id) {
          return { ...todo, title: action.payload.title }
        }
        return todo
      })
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

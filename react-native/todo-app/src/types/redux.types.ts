import { TodoInterface } from './todo.types'

export interface TodosState {
  todos: TodoInterface[]
  loading: boolean
  error: string | undefined
}

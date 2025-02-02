import { TodoInterface } from './todo.types'

export interface TodoState {
  todos: TodoInterface[]
  loading: boolean
}

import { TodoInterface } from './todo.types'

interface Response {
  message: string
  status: number
  error: string | undefined
}

export interface TodosRepsonse extends Response {
  data: TodoInterface[]
}

export interface TodoRepsonse extends Response {
  data: TodoInterface
}

export interface DeleteResponse extends Response {
  data: null
}

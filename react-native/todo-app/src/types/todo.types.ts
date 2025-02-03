export interface TodoInterface {
  id?: string
  title: string
  description: string
  completed?: boolean
  author_id: string
}

export interface TodoListInterface {
  item: TodoInterface
  index: number
}

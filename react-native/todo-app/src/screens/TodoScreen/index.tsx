import { useTodoScreenModel } from './model'
import { TodoScreenView } from './view'

const TodoScreen = () => {
  const model = useTodoScreenModel()

  return <TodoScreenView {...model} />
}

export default TodoScreen

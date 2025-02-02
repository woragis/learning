import { useTodosScreenModel } from './model'
import { TodosScreenView } from './view'

const TodosScreen = () => {
  const model = useTodosScreenModel()

  return <TodosScreenView {...model} />
}

export default TodosScreen

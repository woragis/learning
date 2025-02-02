import { TodoListInterface } from '@/src/types/todo.types'
import { useTodosScreenModel } from './model'
import {
  FlatList,
  SafeAreaView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native'
import { IconButton } from 'react-native-paper'

export const TodosScreenView = ({
  editedTodo,
  handleTodoChange,
  handleTodoDelete,
  handleTodoEdit,
  handleTodoEditSubmit,
  handleTodoSubmit,
  todo,
  todoList,
}: ReturnType<typeof useTodosScreenModel>) => {
  const renderTodos = ({ item, index }: TodoListInterface) => {
    return (
      <View
        key={`todo_item_${item.id}_at_${index}`}
        style={styles.todoList}
      >
        <IconButton
          icon='pencil'
          iconColor='#fff'
          onPress={() => handleTodoEdit(item)}
        />
        <IconButton
          icon='trash-can'
          iconColor='#fff'
          onPress={() => handleTodoDelete(item.id)}
        />
        <Text style={styles.todoListText}>{item.title}</Text>
      </View>
    )
  }
  return (
    <SafeAreaView>
      <Text>TodoScreen</Text>

      {/* Todo Component */}
      <View style={styles.container}>
        <TextInput
          style={styles.textInput}
          placeholder='Add a task'
          value={todo}
          onChangeText={handleTodoChange}
        />

        {editedTodo ? (
          <TouchableOpacity
            style={styles.touchable}
            onPress={handleTodoEditSubmit}
          >
            <Text style={styles.touchableText}>Save Todo</Text>
          </TouchableOpacity>
        ) : (
          <TouchableOpacity
            style={styles.touchable}
            onPress={handleTodoSubmit}
          >
            <Text style={styles.touchableText}>Add Todo</Text>
          </TouchableOpacity>
        )}

        {/* Render todo list */}
        <FlatList
          data={todoList}
          renderItem={renderTodos}
        />
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    margin: 16,
  },
  textInput: {
    borderWidth: 2,
    borderColor: '#1e98ff',
    borderRadius: 6,
    paddingVertical: 8,
    paddingHorizontal: 16,
  },
  touchable: {
    backgroundColor: '#000',
    borderRadius: 8,
    paddingVertical: 8,
    marginVertical: 34,
    alignItems: 'center',
  },
  touchableText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 28,
  },
  todoList: {
    backgroundColor: '#1c90ff',
    borderRadius: 6,
    paddingHorizontal: 6,
    paddingVertical: 12,
    marginBottom: 12,
    flexDirection: 'row',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.8,
    shadowRadius: 3,
    elevation: 3,
  },
  todoListText: {
    color: '#fff',
    fontSize: 20,
    fontWeight: '800',
    flex: 1,
  },
})

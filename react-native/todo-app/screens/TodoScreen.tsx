import {
  FlatList,
  SafeAreaView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native'
import React from 'react'

interface DataInterface {
  id: string
  title: string
}
const dummyData: DataInterface[] = [
  { id: '81', title: 'wash car' },
  { id: '82', title: 'read a book' },
]

interface TodoListInterface {
  item: DataInterface
  index: number
}

const TodoScreen = () => {
  const renderTodos = ({ item, index }: TodoListInterface) => {
    return (
      <View
        key={`todo_item_${item.id}_at_${index}`}
        style={styles.todoList}
      >
        <Text>{item.title}</Text>
      </View>
    )
  }
  return (
    // General Component
    <SafeAreaView>
      <Text>TodoScreen</Text>

      {/* Todo Component */}
      <View style={styles.container}>
        <TextInput
          style={styles.textInput}
          placeholder='Add a task'
        />

        <TouchableOpacity style={styles.touchable}>
          <Text style={styles.touchableText}>Add Todo</Text>
        </TouchableOpacity>

        {/* Render todo list */}
        <FlatList
          data={dummyData}
          renderItem={renderTodos}
        />
      </View>
    </SafeAreaView>
  )
}

export default TodoScreen

const styles = StyleSheet.create({
  container: {
    margin: 16,
  },
  textInput: {
    borderWidth: 2,
    borderColor: '#1e98ff',
    borderRadius: 6,
    paddingVertical: 12,
    paddingHorizontal: 16,
  },
  touchable: {
    backgroundColor: '#000',
    borderRadius: 6,
    paddingVertical: 12,
    marginTop: 24,
    alignItems: 'center',
  },
  touchableText: {
    color: '#fff',
    fontWeight: 'bold',
    fontSize: 28,
  },
  todoList: {},
})

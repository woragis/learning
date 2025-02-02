import { configureStore } from '@reduxjs/toolkit'
import todosReducer from './todo/slice'

const store = configureStore({
  reducer: {
    todos: todosReducer,
  },
})

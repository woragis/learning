import { Action, configureStore, ThunkAction } from '@reduxjs/toolkit'
import todosSlice from './todo/slice'

const store = configureStore({
  reducer: {
    todos: todosSlice.reducer,
  },
})

export type AppDispatch = typeof store.dispatch
export type RootState = ReturnType<typeof store.getState>
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>
export default store

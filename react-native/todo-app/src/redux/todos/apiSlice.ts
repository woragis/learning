import { TodoInterface } from '@/src/types/todo.types'
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

const todosApi = createApi({
  reducerPath: 'todosApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://10.0.2.2:8080/todos' }),
  tagTypes: ['todos'],
  endpoints: (builder) => ({
    getTodos: builder.query<TodoInterface[], void>({
      query: () => '/',
      providesTags: ['todos'],
      transformResponse: (response: TodoInterface[]) => {
        return response
      },
    }),
    getTodoById: builder.query<TodoInterface, TodoInterface['id']>({
      query: (id) => `/${id}`,
    }),
    postTodo: builder.mutation<TodoInterface, TodoInterface>({
      query: (todo) => ({
        url: '/',
        body: todo,
        method: 'POST',
      }),
      invalidatesTags: ['todos'],
    }),
    putTodo: builder.mutation<TodoInterface, TodoInterface>({
      query: (todo) => ({
        url: `/${todo.id}`,
        body: todo,
        method: 'PUT',
      }),
      invalidatesTags: ['todos'],
    }),
    deleteTodo: builder.mutation<{}, TodoInterface['id']>({
      query: (id) => ({
        url: `/${id}`,
        // body: todo,
        method: 'DELETE',
      }),
      invalidatesTags: ['todos'],
    }),
  }),
})

export default todosApi

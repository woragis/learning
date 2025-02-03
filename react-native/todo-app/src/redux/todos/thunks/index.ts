import addAsyncBulider from './add'
import deleteAsyncBulider from './delete'
import editAsyncBulider from './edit'
import fetchAsyncBulider from './fetch'

export const TODOS_BASE_URL = 'http://localhost:8080/todos'

export {
  addAsyncBulider,
  editAsyncBulider,
  deleteAsyncBulider,
  fetchAsyncBulider,
}

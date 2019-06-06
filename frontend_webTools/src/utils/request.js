import axios from 'axios'
import { Message } from 'element-ui'

// 默认配置
// axios.defaults.baseURL = 'http://www.xxxx.com'
// axios.defaults.headers.post['Content-Type'] = 'application/json'

// http request 拦截器
axios.interceptors.request.use(
  config => {
    // token 处理代码
    return config
  },
  error => {
    Promise.reject(error)
  }
)

// http response 拦截器
axios.interceptors.response.use(
  response => {
    return response.data
  },
  error => {
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default axios

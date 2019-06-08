/**
 * API 配置
 */
import { get, post, put, del } from '@/utils/request/'
// 获取财务报表信息
export const getFinanceReport = function (date) {
  return get('/api/report/?month=' + date)
}
// 新增财务报表信息
export const addFinanceReport = function (params) {
  return post('/api/report/', params)
}
// 修改财务报表信息
export const modifyFinanceReport = function (id, params) {
  return put('/api/report/' + id + '/', params)
}
// 删除财务报表信息
export const deleteFinanceReport = function (id) {
  return del('/api/report/' + id)
}

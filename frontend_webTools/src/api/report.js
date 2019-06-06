/**
 * API 配置
 */
import { get } from '@/utils/request/'
// 获取财务报表信息
export const getFinanceReport = function () {
  return get('/api/v1/')
}

/**
 * API 配置
 */
import { get } from '@/utils/request/'
// 获取面试题信息
export const getInterview = function (date) {
  return get('/api/interview/')
}

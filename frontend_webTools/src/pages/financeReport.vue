<template>
  <div class="financeReport">
    <div class="tableWrap">
      <el-table :data="tableData" style="width: 100%" :span-method="objectSpanMethod">
        <el-table-column prop="date" label="2019-6" width="150" align="center">
          <el-table-column prop="date" label="资产" width="150" align="center">
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="incomeChannel" label="收入平台" width="120"></el-table-column>
            <el-table-column prop="incomeAmount" label="实收金额" width="120"></el-table-column>
            <el-table-column prop="incomeDate" label="实收日期" width="120"></el-table-column>
          </el-table-column>
          <el-table-column label="负债" align="center">
            <el-table-column prop="name" label="姓名" width="120"></el-table-column>
            <el-table-column prop="debtChannel" label="负债平台" width="120"></el-table-column>
            <el-table-column prop="debtAmount" label="还款金额" width="120"></el-table-column>
            <el-table-column prop="repayDate" label="还款日期" width="120"></el-table-column>
            <el-table-column prop="isRepay" label="还款状态" width="120"></el-table-column>
          </el-table-column>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import { getFinanceReport } from '@/api/report'

export default {
  data () {
    return {
      tableData: []
    }
  },
  created () {
    this.getFinanceReport()
  },
  methods: {
    getFinanceReport () {
      getFinanceReport().then((data) => {
        this.tableData = data
      })
    },
    objectSpanMethod ({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0) {
        if (rowIndex % 2 === 0) {
          return {
            rowspan: 2,
            colspan: 1
          }
        } else {
          return {
            rowspan: 0,
            colspan: 0
          }
        }
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.tableWrap {
  width: 1200px;
  padding: 50px;
}
</style>

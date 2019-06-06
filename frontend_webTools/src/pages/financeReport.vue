<template>
  <div class="financeReport primary-bg wh-100">
    <div class="tableWrap">
      <div class="selectMonth">
        <span class="demonstration">请选择月份</span>
        <el-date-picker v-model="month" type="month" placeholder="选择月" @change="selectData"></el-date-picker>
      </div>
      <el-table :data="tableData" style="width: 100%" :span-method="objectSpanMethod">
        <el-table-column prop="date" label="资产" align="center">
          <el-table-column prop="name" label="姓名">
            <template slot-scope="scope">
              <el-input v-model="scope.row.name" readonly="false"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="incomeChannel" label="收入平台">
            <template slot-scope="scope">
              <el-input v-model="scope.row.incomeChannel"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="incomeAmount" label="实收金额">
            <template slot-scope="scope">
              <el-input v-model="scope.row.incomeAmount"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="incomeDate" label="实收日期">
            <template slot-scope="scope">
              <el-input v-model="scope.row.incomeDate"></el-input>
            </template>
          </el-table-column>
        </el-table-column>
        <el-table-column label="负债" align="center">
          <el-table-column prop="name" label="姓名">
            <template slot-scope="scope">
              <el-input v-model="scope.row.name"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="debtChannel" label="负债平台">
            <template slot-scope="scope">
              <el-input v-model="scope.row.debtChannel"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="debtAmount" label="还款金额">
            <template slot-scope="scope">
              <el-input v-model="scope.row.debtAmount"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="repayDate" label="还款日期">
            <template slot-scope="scope">
              <el-input v-model="scope.row.repayDate"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="isRepay" label="还款状态">
            <template slot-scope="scope">
              <el-input v-model="scope.row.isRepay"></el-input>
            </template>
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
      tableData: [],
      month: ''
    }
  },
  created () {
    this.getFinanceReport()
  },
  methods: {
    getFinanceReport () {
      this.month = this.month !== 'Invalid date' ? this.month : ''
      console.log(this.month)
      getFinanceReport(this.month).then((data) => {
        this.tableData = data
      })
    },
    selectData (val) {
      this.month = this.Moment(val).format('YYYY-MM')
      this.getFinanceReport()
    },
    objectSpanMethod ({ row, column, rowIndex, columnIndex }) {
      // if (columnIndex === 0) {
      //   if (rowIndex % 2 === 0) {
      //     return {
      //       rowspan: 2,
      //       colspan: 1
      //     }
      //   } else {
      //     return {
      //       rowspan: 0,
      //       colspan: 0
      //     }
      //   }
      // }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.financeReport {
  .tableWrap {
    padding: 10px 200px 50px 200px;
  }
  .selectMonth {
    padding: 30px 0;
  }
}
</style>
<style>
.el-input__inner {
  border: none !important;
  background: none !important;
}
</style>

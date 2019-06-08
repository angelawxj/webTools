<template>
  <div class="financeReport primary-bg wh-100">
    <div class="tableWrap">
      <div class="selectMonth">
        <div>
          <span class="table_date">请选择月份：</span>
          <el-date-picker v-model="month" type="month" placeholder="选择月" @change="selectData"></el-date-picker>
        </div>
        <div>
          <el-button type="primary" @click="addData">新增数据</el-button>
          <el-button type="primary" @click="saveData">提交</el-button>
        </div>
      </div>
      <div class="table">
        <el-table :data="tableData" style="width: 100%" :span-method="objectSpanMethod">
          <el-table-column prop="date" label="资产" align="center">
            <el-table-column prop="name" label="姓名">
              <template slot-scope="scope">
                <el-input v-model="scope.row.name"></el-input>
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
            <el-table-column prop="debtName" label="姓名">
              <template slot-scope="scope">
                <el-input v-model="scope.row.debtName"></el-input>
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
            <el-table-column prop="isRepay" label="操作">
              <template slot-scope="scope">
                <div class="button">
                  <el-button type="success" @click="modifyData(scope.row.id)">修改</el-button>
                  <el-button type="danger" @click="deleteData((scope.row.id))">删除</el-button>
                </div>
              </template>
            </el-table-column>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import { getFinanceReport, addFinanceReport, modifyFinanceReport, deleteFinanceReport } from '@/api/report'

export default {
  data () {
    return {
      tableData: [],
      month: '',
      list: {}
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
    addData () {
      this.list = {
        month: '2019-6',
        name: '',
        incomeChannel: '',
        incomeAmount: '',
        incomeDate: '',
        debtName: '',
        debtChannel: '',
        debtAmount: '',
        repayDate: '',
        isRepay: ''
      }
      this.tableData.unshift(this.list)
    },
    saveData () {
      addFinanceReport(this.tableData[0]).then((data) => {
        this.$message({
          message: '恭喜你，新增成功',
          type: 'success'
        })
        this.getFinanceReport()
      })
    },
    modifyData (id) {
      console.log(id)
      modifyFinanceReport(id, this.tableData[0]).then((data) => {
        this.$message({
          message: '恭喜你，修改成功',
          type: 'success'
        })
        this.getFinanceReport()
      })
    },
    deleteData (id) {
      deleteFinanceReport(id).then((data) => {
        this.$message({
          message: '恭喜你，删除成功',
          type: 'success'
        })
        this.getFinanceReport()
      })
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
    padding: 10px 100px 50px 100px;
  }
  .selectMonth {
    display: flex;
    justify-content: space-between;
    padding: 30px 0;
  }
  .table_date {
    color: #fff;
  }
  .button {
    display: flex;
    justify-content: space-between;
  }
}
</style>
<style>
.table .el-input__inner {
  border: none !important;
  background: none !important;
}
.el-table th > .cell {
  font-weight: bold;
  font-size: 14px;
}
.el-table th > .cell,
.cell input {
  text-align: center;
}
.el-table thead.is-group th {
  background: #ef3221;
  color: #fff;
}
</style>

<template>
  <div class="financeReport">
    <div class="tableWrap">
      <el-table :data="tableData" style="width: 100%" :span-method="objectSpanMethod">
        <el-table-column prop="date" label="资产" width="150" align="center">
          <el-table-column prop="name" label="姓名" width="120"></el-table-column>
          <el-table-column prop="name" label="收入平台" width="120"></el-table-column>
          <el-table-column prop="name" label="实收金额" width="120"></el-table-column>
          <el-table-column prop="name" label="实收日期" width="120"></el-table-column>
        </el-table-column>
        <el-table-column label="负债" align="center">
          <el-table-column prop="name" label="姓名" width="120"></el-table-column>
          <el-table-column prop="name" label="负债平台" width="120"></el-table-column>
          <el-table-column prop="name" label="还款日期" width="120"></el-table-column>
          <el-table-column prop="name" label="还款状态" width="120"></el-table-column>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tableData: [{
        id: '12987122',
        name: '汪小娟',
        amount1: '234',
        amount2: '3.2',
        amount3: 10
      }, {
        id: '12987123',
        name: '王小虎',
        amount1: '165',
        amount2: '4.43',
        amount3: 12
      }, {
        id: '12987124',
        name: '王小虎',
        amount1: '324',
        amount2: '1.9',
        amount3: 9
      }, {
        id: '12987125',
        name: '王小虎',
        amount1: '621',
        amount2: '2.2',
        amount3: 17
      }, {
        id: '12987126',
        name: '王小虎',
        amount1: '539',
        amount2: '4.1',
        amount3: 15
      }]
    }
  },
  methods: {
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

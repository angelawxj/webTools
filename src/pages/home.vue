<template>
  <div class="gdgg_xjbb_page">
    <div class="gdgg_xjbb_rainbowBG"></div>
    <div class="gdgg_xjbb_page-margin">
      <el-row type="flex" :gutter="80">
        <el-col :span="4">
          <img src="../assets/images/report.png" alt class="gdgg_xjbb_modular">
          <span class="gdgg_xjbb_label">财务报表</span>
        </el-col>
        <el-col :span="4">
          <img src="../assets/images/business-and-finance.png" alt class="gdgg_xjbb_modular">
          <span class="gdgg_xjbb_label">现金流机器</span>
        </el-col>
        <el-col :span="4">
          <img src="../assets/images/Interview.png" alt class="gdgg_xjbb_modular">
          <span class="gdgg_xjbb_label">面试刷题</span>
        </el-col>
        <el-col :span="4">
          <img src="../assets/images/skill.png" alt class="gdgg_xjbb_modular">
          <span class="gdgg_xjbb_label">技能树</span>
        </el-col>
        <el-col :span="4">
          <img src="../assets/images/library.png" alt class="gdgg_xjbb_modular">
          <span class="gdgg_xjbb_label">图书馆</span>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.gdgg_xjbb_page {
  display: block;
  width: 100%;
  height: 100%;
}
.gdgg_xjbb_rainbowBG {
  position: absolute;
  background: #e8a36c;
  height: 100%;
  overflow: hidden;
  width: 100%;
}
.gdgg_xjbb_rainbowBG::after {
  content: '';
  position: absolute;
  display: block;
  width: 200%;
  height: 60px;
  bottom: 300px;
  margin-left: -50%;
  transform: rotate(-20deg);
  box-shadow: 0 60px 0 #f7c44f, 0 120px 0 #fc9047, 0 180px 0 #ea4e52,
    0 240px 0 #902fb0, 0 300px 0 #008cfb;
  background: #57bc56;
  z-index: 0;
}
.gdgg_xjbb_page-margin {
  width: 70%;
  min-width: 800px;
  margin: auto;
  padding: 20px 30px;
}
.gdgg_xjbb_modular {
  height: 90px;
  border-radius: 4px;
}
.gdgg_xjbb_label {
  display: block;
  text-align: center;
  line-height: 4;
  color: #fff;
}
</style>

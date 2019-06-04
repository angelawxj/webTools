<template>
  <div class="gdgg_xjbb_page">
    <div class="gdgg_xjbb_rainbowBG"></div>
    <div class="gdgg_xjbb_page-margin">
      <el-row type="flex" :gutter="80">
        <el-col :span="4">
          <div class="gdgg_xjbb_modular"></div>
          <span class="gdgg_xjbb_label">财报</span>
          </el-col>
        <el-col :span="4">
          <div class="gdgg_xjbb_modular"></div></el-col>
        <el-col :span="4"><div class="gdgg_xjbb_modular"></div></el-col>
        <el-col :span="4"><div class="gdgg_xjbb_modular"></div></el-col>
        <el-col :span="4"><div class="gdgg_xjbb_modular"></div></el-col>
        <el-col :span="4"><div class="gdgg_xjbb_modular"></div></el-col>
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
  .gdgg_xjbb_page{
    display:block;
    width:100%;
    height: 100%;
  }
  .gdgg_xjbb_rainbowBG{
    position: absolute;
    background: #E8A36C;
    height: 100%;
    overflow: hidden;
    width: 100%;
  }
  .gdgg_xjbb_rainbowBG::after{
    content: "";
    position: absolute;
    display:block;
    width: 200%;
    height: 60px;
    bottom: 300px;
    margin-left: -50%;
    transform: rotate(-20deg);
    box-shadow: 0 60px 0 #F7C44F,
    0 120px 0 #FC9047,
    0 180px 0 #EA4E52,
    0 240px 0 #902FB0,
    0 300px 0 #008CFB;
    background: #57BC56;
    z-index: 0;
  }
  .gdgg_xjbb_page-margin{
    width: 70%;
    min-width: 800px;
    margin:auto;
    padding:20px 30px;
  }
  .gdgg_xjbb_modular{
    height: 90px;
    background-color: #fff;
    border-radius: 4px;
  }
  .gdgg_xjbb_label{
    display:block;
    text-align: center;
    line-height: 4;
    }
</style>

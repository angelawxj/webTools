<template>
  <div class="interview">
    <el-row>
      <el-col :span="5">
        <div class="grid-content bg-purple menu-heignt">
          <el-menu default-active="2" class="el-menu-vertical-demo" background-color="#545c64" text-color="#fff" active-text-color="#ffd04b">
            <el-submenu index="1">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span>导航一</span>
              </template>
              <el-menu-item-group>
                <template slot="title">分组一</template>
                <el-menu-item index="1-1">选项1</el-menu-item>
                <el-menu-item index="1-2">选项2</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="分组2">
                <el-menu-item index="1-3">选项3</el-menu-item>
              </el-menu-item-group>
              <el-submenu index="1-4">
                <template slot="title">选项4</template>
                <el-menu-item index="1-4-1">选项1</el-menu-item>
              </el-submenu>
            </el-submenu>
            <el-menu-item index="2">
              <i class="el-icon-menu"></i>
              <span slot="title">导航二</span>
            </el-menu-item>
            <el-menu-item index="3">
              <i class="el-icon-document"></i>
              <span slot="title">导航三</span>
            </el-menu-item>
            <el-menu-item index="4">
              <i class="el-icon-setting"></i>
              <span slot="title">导航四</span>
            </el-menu-item>
          </el-menu>
        </div>
      </el-col>
      <el-col :span="19">
        <div class="grid-content bg-purple-light topic">
          <el-collapse v-for="(item, index) in interviewList" :key="index">
            <el-collapse-item :title="item.question" name="1">
              <div>{{item.answer}}</div>
            </el-collapse-item>
          </el-collapse>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { getInterview } from '@/api/interview'

export default {
  data () {
    return {
      interviewList: []
    }
  },
  created () {
    this.getInterview()
  },
  methods: {
    getInterview () {
      getInterview().then((data) => {
        this.interviewList = data
      })
    }

  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
.topic {
  margin: 60px 100px 50px 100px;
}
.menu-heignt {
  height: 100vh;
  background: rgb(84, 92, 100);
}
.el-menu-vertical-demo {
  padding-top: 50px;
}
.el-collapse-item__content {
  color: #409eff;
}
</style>
<style>
.el-collapse-item__content {
  color: #409eff;
}
</style>

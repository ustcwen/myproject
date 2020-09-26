<template>
  <div>
    <el-table :data="tableData"
                  border
                  width="100%">
          <el-table-column
            :key="col.prop"
            :label="col.label"
            :prop="col.prop"
            v-for="col in cols">
          </el-table-column>

        </el-table>
  </div>
</template>

<script>
  export default {
     data () {
        return {
            tableData: [],
            cols: [],
            id: '',
          code: ''
                }
            },
    created(){
       this.search();
    },
    methods: {
      search () {
        let formData = new FormData()
        formData.append('id', this.id)
        let config = {headers: {'Content-Type': 'multipart/form-data'}}
        this.$http.post('http://127.0.0.1:8000/api/gettable/', formData, config).then(res => {
          this.$message({
            message: '查询成功！',
            type: 'success'
          })
          this.cols = []
          this.code = res.data.data.code
          console.log(res.data.data.code)
          console.log(res.data.data)
          for (var j = 0; j < res.data.data.cols_list.length; j++) {
            var obj = {}
            obj.label = res.data.data.cols_list[j].label
            obj.prop = res.data.data.cols_list[j].prop
            this.cols.push(obj)
          }

          this.tableData = []
          for (var i = 0; i < res.data.data.each_row.length; i++) {
            this.tableData.push(res.data.data.each_row[i])
          }
          console.log(this.tableData)
        }, (error) => {
          this.$message.error('查询失败' + error.response.data.msg)
        })
    }
    }

  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>

</style>

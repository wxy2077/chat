<template>
  <div id="app">
      <router-view></router-view>
      <menu-tab-bar  />
  </div>
</template>

<script>
    import MenuTabBar from '@/components/common/MenuTabBar'
    export default {
        name: 'App',
        components: {
            MenuTabBar,
        }
    }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  /*color: #2c3e50;*/
}
</style>

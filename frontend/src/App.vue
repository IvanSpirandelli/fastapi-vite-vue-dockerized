<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import RandomQuestionButton from './components/RandomQuestionButton.vue'
import Login from './components/Login.vue'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <div>
      <NavBar/> 
      <RouterView/> 
  </div>
</template>

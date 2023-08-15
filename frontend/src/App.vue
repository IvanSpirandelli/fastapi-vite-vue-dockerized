<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import Button from './components/Button.vue'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <div>
    <!-- <header> -->
      <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
      <div>
        <NavBar/>
      </div>
      <div>
        <Button/>
      </div>
      
      <!-- <div class="wrapper">    
        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/backend">Backend</RouterLink>
          <RouterLink to="/info">Links</RouterLink>
        </nav>
      </div> -->

    <!-- </header> -->
    <!-- <RouterView /> -->

  </div>
</template>

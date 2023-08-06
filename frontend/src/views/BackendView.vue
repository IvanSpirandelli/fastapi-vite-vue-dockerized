<template>
    <div>
    <button @click="getMessage">Get Random Message</button>
    <h1 class="green" data="message">{{ message }}</h1>
    </div>
    </template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      message: null
    }
  },
  methods: {
    async getMessage() {
      await axios.get('http://0.0.0.0:1071/get_random_message').then(
          response => this.message = response.data.message
      )
    }
  }
}
</script>

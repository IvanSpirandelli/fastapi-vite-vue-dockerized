<template>
  <div class="justify-center">
    <button @click="getMessage" class="bg-transparent text-gray-700 font-semibold hover:text-gray-500 py-2 px-4 border border-gray-500 hover:border-gray-300">
      What does the backend want to tell us?
    </button>

    <h1 class="py-8 bg-transparent text-gray-700 font-semibold" data="message">{{ message }}</h1>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      message: "Nothing yet . . ."
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
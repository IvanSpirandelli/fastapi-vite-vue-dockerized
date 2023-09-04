<script setup>
    import { useLoggedIn } from '../composables/useLoggedIn.js'
    const isLoggedIn = useLoggedIn()
</script>

<template>
    <div class = "absolute inset-x-0 top-0 h-16 bg-blue-200 flex items-stretch"> 
        <div class= "px-0 py-0 w-16 h-16"> 
            <img src = "/src/assets/oct.png"> 
        </div>
        <div class = "flex items-center ml-auto mr-5"> 
            <div @click="logout" class = "text-lg border-gray-500 hover:underline hover:cursor-pointer">
                <p>Logout</p>
            </div>
            <!-- <div v-if="!isLoggedIn">
                <p>KEK</p>
            </div> -->
        </div>
        
    </div>
</template>

<script>
import axios from 'axios'

export default {
    methods: {
        logout() {
            axios('http://localhost:1071/auth/token/logout', {
                method: "post",
                withCredentials: true
            })
            .then((response) => {
                this.$router.push('/')
            })
            .catch((error) => {
                this.$router.push('/')
                console.log(error)
            })
        }
    }
}
</script>

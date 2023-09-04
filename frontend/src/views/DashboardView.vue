<script setup>
    import { useLoggedIn } from '../composables/useLoggedIn.js'
    const isLoggedIn = useLoggedIn()
</script>

<template>
    <div>
        <div v-if="isLoggedIn">
            <p>Such Content. Many wow.</p>
        </div>
        <div v-if="!isLoggedIn">
            <div @click="toLoginPage" class = "text-lg">
                <p>
                    You need to be logged in to see this page! <a href="#" class="font-medium text-primary-600 hover:underline hover:cursor-pointer hover:underline">Log In</a>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
export default{
    methods: 
    {
        toLoginPage() {
            this.$router.push('/')
        }
    }
} 
</script>


<template>
    <div class="h-screen flex items-center justify-center mx-auto">
        <div class="rounded-lg shadow">
            <div class="p-6 space-y-4">
                <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                    Sign in to your account
                </h1>
                <form class="space-y-4" action="#">
                    <div>
                        <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Your email</label>
                        <input v-model="email" type="email" name="email" id="email" placeholder="name@company.com" required="" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5">
                    </div>
                    <div>
                        <label for="password" class="block mb-2 text-sm font-medium text-gray-900">Password</label>
                        <input v-model="password" type="password" name="password" id="password" placeholder="••••••••" required="" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5">
                    </div>
                    <div class="flex items-center justify-center">
                        <button @click="signIn" class="bg-transparent text-gray-700 font-semibold hover:text-gray-500 py-2 px-4 border border-gray-500 hover:border-gray-300 rounded-lg">
                        Sign in
                        </button>
                    </div>
                    <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                        Don’t have an account yet? <a href="#" class="font-medium text-primary-600 hover:underline">Sign up</a>
                    </p>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    data() {
        return {
            email: "",
            password: "",
        }
    },
    methods: {
        async signIn() {
            await axios.post('http://0.0.0.0:1071/auth/token/login',
            {
                username: this.email,
                password: this.password
            },
            {
                headers: {'content-type': 'application/x-www-form-urlencoded'}
            }).then(
                response => this.message = response.data.message,
                this.$router.push('/info')
            )
        }
    }
}
</script>
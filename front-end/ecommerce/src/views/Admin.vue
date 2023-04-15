<template>
    <div class="admin">
        <h2>Login</h2>
        <form>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" name="email" id="email" v-model="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" name="password" id="password" v-model="password" required>
            </div>
            <button type="submit" @click.prevent="onSubmit">Login</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        login() {
            return this.$store.dispatch('auth/login', { email: this.email, password: this.password });
        },
        onSubmit() {
            this.login().then(() => {
                axios.post('http://127.0.0.1:8081/admin', {
                    login: this.email,
                    password: this.password
                });
            });
        }
    }
};
</script>

<style>
.login {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
}

.form-group {
    margin-bottom: 10px;
    text-align: left;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input {
    width: 100%;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    font-size: 16px;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    cursor: pointer;
    font-size: 16px;
}
</style>
  
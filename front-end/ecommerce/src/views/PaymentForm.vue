<template>
    <div class="payment-form">
        <h3>Detalhes do Pagamento</h3>
        <form @submit.prevent="submitPaymentForm">
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" v-model="paymentForm.name" required>
            </div>
            <div class="form-group">
                <label for="email">E-mail:</label>
                <input type="email" id="email" v-model="paymentForm.email" required>
            </div>
            <div class="form-group">
                <label for="address">Endereço:</label>
                <input type="text" id="address" v-model="paymentForm.address" required>
            </div>
            <div class="form-group">
                <label for="cardNumber">Número do Cartão:</label>
                <input type="text" id="cardNumber" v-model="paymentForm.cardNumber" required>
            </div>
            <button type="submit" class="btn-pay">Realizar Compra</button>
        </form>

        <!-- Mensagem de status da compra -->
        <div class="payment-status" v-if="paymentStatus !== null">
            {{ paymentStatus ? 'Compra Aprovada' : 'Não foi possível realizar a compra' }}
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    data() {
        return {
            paymentForm: {
                name: '',
                email: '',
                address: '',
                cardNumber: ''
            },
            paymentStatus: null
        };
    },
    methods: {
        submitPaymentForm() {
            // Enviar dados do formulário para a API de pagamento
            // Substitua a URL "http://localhost:8081/payment" pela URL correta da sua API
            axios.post('http://localhost:8081/payment', this.paymentForm)
                .then(response => {
                    if (response.data.payment === true) {
                        this.paymentStatus = true; // Compra aprovada
                    } else {
                        this.paymentStatus = false; // Falha na compra
                    }
                })
                .catch(error => {
                    console.log(error);
                    this.paymentStatus = false; // Falha na compra
                });
        }
    }
};
</script>
  
<style scoped>
.payment-form {
    margin-top: 20px;
}

.form-group {
    margin-bottom: 10px;
}

.label {
    display: block;
    font-weight: bold;
}

input[type="text"],
input[type="email"] {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button.btn-pay {
    padding: 10px 20px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.payment-status {
    margin-top: 20px;
    font-weight: bold;
}
</style>
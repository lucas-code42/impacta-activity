<template>
    <div class="product-update">
        <h2>Atualizar Produto</h2>
        <form @submit.prevent="submitForm">
            <div class="form-group">
                <label for="title">Título:</label>
                <input type="text" id="title" v-model="form.title" required>
            </div>
            <div class="form-group">
                <label for="price">Preço:</label>
                <input type="number" id="price" v-model="form.price" required>
            </div>
            <div class="form-group">
                <label for="description">Descrição:</label>
                <textarea id="description" v-model="form.description" required></textarea>
            </div>
            <div class="form-group">
                <label for="category">Categoria:</label>
                <input type="text" id="category" v-model="form.category" required>
            </div>
            <div class="form-group">
                <label for="image">Imagem:</label>
                <input type="text" id="image" v-model="form.image" required>
            </div>
            <div class="form-group">
                <label for="id">ID:</label>
                <input type="text" id="id" v-model="form.id" required>
            </div>
            <div class="form-group">
                <button type="submit" class="update-btn">Atualizar</button>
            </div>
        </form>
    </div>
</template>
  
<script>
export default {
    data() {
        return {
            form: {
                title: '',
                price: '',
                description: '',
                category: '',
                image: '',
                id: ''
            }
        }
    },
    methods: {
        submitForm() {
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(this.form)
            };
            fetch('http://localhost:8081/update/products', requestOptions)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erro ao atualizar produto');
                    }
                    alert('Produto atualizado com sucesso!');
                    this.form = {
                        title: '',
                        price: '',
                        description: '',
                        category: '',
                        image: '',
                        id: ''
                    };
                })
                .catch(error => {
                    alert(error.message);
                });
        }
    }
}
</script>
  
<style scoped>
.product-update {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 5px;
}

h2 {
  margin-bottom: 20px;
  text-align: center;
  font-size: 24px;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  font-size: 14px;
  line-height: 1.5;
}

button[type="submit"] {
  display: block;
  width: 100%;
  background-color: #4285f4;
  color: #fff;
  border: none;
  border-radius: 3px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #1a73e8;
}

.update-btn {
  background-color: #dc3545;
}

.update-btn:hover {
  background-color: #c82333;
}
</style>
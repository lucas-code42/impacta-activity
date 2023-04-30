<template>
    <div>
      <h2>Cadastro de Produto</h2>
      <form @submit.prevent="submitForm">
        <div>
          <label for="title">Título:</label>
          <input type="text" id="title" v-model="form.title" required>
        </div>
        <div>
          <label for="price">Preço:</label>
          <input type="number" id="price" v-model="form.price" required>
        </div>
        <div>
          <label for="description">Descrição:</label>
          <textarea id="description" v-model="form.description" required></textarea>
        </div>
        <div>
          <label for="category">Categoria:</label>
          <input type="text" id="category" v-model="form.category" required>
        </div>
        <div>
          <label for="image">Imagem:</label>
          <input type="text" id="image" v-model="form.image" required>
        </div>
        <div>
          <button type="submit">Cadastrar</button>
        </div>
      </form>
    </div>
</template>
  
<script>
  export default {
    name: "Create",
    data() {
      return {
        form: {
          title: '',
          price: '',
          description: '',
          category: '',
          image: ''
        }
      }
    },
    methods: {
      submitForm() {
        fetch('http://localhost:8081/products', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.form)
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Erro ao cadastrar produto');
          }
          alert('Produto cadastrado com sucesso!');
          this.form = {
            title: '',
            price: '',
            description: '',
            category: '',
            image: ''
          };
        })
        .catch(error => {
          alert(error.message);
        });
      }
    }
  };
</script>

<style scoped>
.product-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 30px;
  background-color: #fff;
  box-shadow: 0px 0px 10px #ddd;
  border-radius: 5px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 10px;
}

input[type="text"],
input[type="number"],
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 3px;
  font-size: 16px;
  line-height: 1.5;
}

button[type="submit"] {
  background-color: #007aff;
  color: #fff;
  border: none;
  border-radius: 3px;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

button[type="submit"]:hover {
  background-color: #0069d9;
}
</style>
  
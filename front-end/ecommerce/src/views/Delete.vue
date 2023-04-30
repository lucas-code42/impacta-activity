<template>
    <div class="product-delete">
      <h2>Excluir Produto</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="id">ID:</label>
          <input type="text" id="id" v-model="form.id" required>
        </div>
        <div class="form-group">
          <button type="submit" class="delete-btn">Excluir</button>
        </div>
      </form>
    </div>
</template>
  
<script>
  export default {
    data() {
      return {
        form: {
          id: ''
        }
      }
    },
    methods: {
      submitForm() {
        const requestOptions = {
          method: 'DELETE',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.form)
        };
        fetch('http://localhost:8081/admin/delete', requestOptions)
          .then(response => {
            if (!response.ok) {
              throw new Error('Erro ao excluir produto');
            }
            alert('Produto excluído com sucesso!');
            this.form.id = '';
          })
          .catch(error => {
            alert(error.message);
          });
      }
    }
  }
</script>
  
<style scoped>
  .product-delete {
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
  
  input[type="text"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 3px;
    font-size: 16px;
    line-height: 1.5;
  }
  
  button[type="submit"] {
    background-color: #ff3b30;
    color: #fff;
    border: none;
    border-radius: 3px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
  }
  
  button[type="submit"]:hover {
    background-color: #e8505b;
  }
</style>
  
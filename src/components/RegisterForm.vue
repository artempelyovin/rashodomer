<template>
  <div class="register-form">
    <h2>Регистрация</h2>

    <form @submit.prevent="handleSubmit">
      <!-- Имя -->
      <div class="form-group">
        <label for="firstName">Имя</label>
        <input
            type="text"
            id="firstName"
            v-model="firstName"
            :class="{'is-invalid': errors.firstName}"
        />
        <div v-if="errors.firstName" class="error-message">{{ errors.firstName }}</div>
      </div>

      <!-- Фамилия -->
      <div class="form-group">
        <label for="lastName">Фамилия</label>
        <input
            type="text"
            id="lastName"
            v-model="lastName"
            :class="{'is-invalid': errors.lastName}"
        />
        <div v-if="errors.lastName" class="error-message">{{ errors.lastName }}</div>
      </div>

      <!-- Логин -->
      <div class="form-group">
        <label for="username">Логин</label>
        <input
            type="text"
            id="username"
            v-model="username"
            :class="{'is-invalid': errors.username}"
        />
        <div v-if="errors.username" class="error-message">{{ errors.username }}</div>
      </div>

      <!-- Пароль -->
      <div class="form-group">
        <label for="password">Пароль</label>
        <input
            type="password"
            id="password"
            v-model="password"
            :class="{'is-invalid': errors.password}"
        />
        <div v-if="errors.password" class="error-message">{{ errors.password }}</div>
      </div>

      <!-- Повторите пароль -->
      <div class="form-group">
        <label for="confirmPassword">Повторите пароль</label>
        <input
            type="password"
            id="confirmPassword"
            v-model="confirmPassword"
            :class="{'is-invalid': errors.confirmPassword}"
        />
        <div v-if="errors.confirmPassword" class="error-message">{{ errors.confirmPassword }}</div>
      </div>

      <!-- Кнопка регистрации -->
      <button type="submit" :disabled="isSubmitting">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      username: '',
      password: '',
      confirmPassword: '',
      errors: {},
      isSubmitting: false
    };
  },
  methods: {
    validateForm() {
      this.errors = {};

      if (!this.firstName) this.errors.firstName = 'Имя обязательно для заполнения';
      if (!this.lastName) this.errors.lastName = 'Фамилия обязательна для заполнения';
      if (!this.username) this.errors.username = 'Логин обязателен';
      if (!this.password) this.errors.password = 'Пароль обязателен';
      if (this.password !== this.confirmPassword) {
        this.errors.confirmPassword = 'Пароли не совпадают';
      }

      return Object.keys(this.errors).length === 0;
    },

    handleSubmit() {
      if (this.validateForm()) {
        this.isSubmitting = true;
        // Здесь можно добавить логику отправки данных на сервер, например:
        // axios.post('/api/register', { ... })

        // Для примера просто выводим данные в консоль:
        console.log({
          firstName: this.firstName,
          lastName: this.lastName,
          username: this.username,
          password: this.password
        });

        this.isSubmitting = false;
      }
    }
  }
};
</script>

<style scoped>
.register-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
}

.form-group {
  margin-bottom: 15px;
}

input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:disabled {
  background-color: #cccccc;
}

.is-invalid {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 0.9em;
}
</style>

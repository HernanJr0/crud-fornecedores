<template>
  <q-page class="q-pa-md">
    <q-card class="q-pa-lg shadow-2 rounded-borders  mx-auto">
      <div class="text-h5 q-mb-md">Novo Fornecedor</div>

      <q-form>
        <q-input

          v-model="fornecedor.nome"
          label="Nome"
          outlined 
          :rules="[val => !!val || 'Nome é obrigatório']"
          class="q-mb-md"
        />
        <q-input
          v-model="fornecedor.email"
          label="E-mail"
          outlined 
          type="email"
          :rules="[val => !!val || 'E-mail é obrigatório']"
          class="q-mb-md"
        />
        <q-input
          v-model="fornecedor.telefone"
          label="Telefone"
          outlined 
          :rules="[val => !!val || 'Telefone é obrigatório']"
          class="q-mb-md"
        />

        <div class="row justify-end q-gutter-sm">
          <q-btn label="Cancelar" flat color="primary" type="reset" @click="cancelar" />
          <q-btn label="Criar" color="primary"  @click="verifyCreate"/>
        </div>
      </q-form>
    </q-card>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { api } from 'boot/axios'
import { useRouter } from 'vue-router'

interface Fornecedor {
  nome: string
  email: string
  telefone: string
}

const fornecedor = ref<Fornecedor>({
  nome: '',
  email: '',
  telefone: '',
})

const router = useRouter()

 async function verifyCreate(){
  try {
    await api.post('/fornecedores/', fornecedor.value)
    void router.push('/listafornecedores') 
  } catch (error) {
    console.error('Erro ao criar fornecedor:', error)
    //  $q.notify 
  }
}

function cancelar(){
  router.back()
}
</script>

<style scoped>
.max-w-md {
  max-width: 500px;
}
</style>
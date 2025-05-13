<template>
  <q-page class="q-pa-md">
    <div class="row items-center justify-between q-mb-md">
      <div class="text-h5">Fornecedor</div>
      <q-btn color="primary" label="Novo Fornecedor" @click="novoFornecedor" />
    </div>

    <q-table title="Lista de Fornecedores" :rows="fornecedores" :columns="colunas" row-key="id" flat bordered>
      <template #body-cell-acoes="props">
        <q-td :props="props">
          <q-btn color="negative" icon="delete" size="sm" round dense @click="deletarFornecedor(props.row.id)" />
        </q-td>
      </template>
    </q-table>
  </q-page>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from 'boot/axios'
import { useRouter } from 'vue-router'
import { Notify } from 'quasar'

const router = useRouter()

const colunas = [
  { name: 'nome', label: 'Nome', field: 'nome', align: 'left' as const },
  { name: 'email', label: 'Email', field: 'email', align: 'left' as const },
  { name: 'telefone', label: 'Telefone', field: 'telefone', align: 'left' as const },
  { name: 'acoes', label: 'Ações', field: 'id', align: 'center' as const }
]

const fornecedores = ref<IFornecedor[]>([])

interface IFornecedor {
  id: number
  nome: string
  email: string
  telefone: string
}

const fetchFornecedores = async () => {
  try {
    const response = await api.get<IFornecedor[]>('/fornecedores/')
    fornecedores.value = response.data
  }
  catch (err) {
    console.error('Erro ao carregar fornecedores:', err)
    Notify.create({
      type: 'negative',
      message: 'Falha ao carregar lista de fornecedores.'
    })
  }
}

onMounted(fetchFornecedores)

const deletarFornecedor = async (id: number) => {
  try {
    await api.delete(`/fornecedores/${id}/`)
    await fetchFornecedores()
    Notify.create({
      type: 'positive',
      message: 'Fornecedor deletado com sucesso!'
    })
  }
  catch (err) {
    console.error('Erro ao deletar fornecedor:', err)
    Notify.create({
      type: 'negative',
      message: 'Não foi possível deletar o fornecedor.'
    })
  }
}

const novoFornecedor = () => {
  void router.push('/novofornecedor')
}
</script>

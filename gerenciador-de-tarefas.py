import json

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
        self.carregar_tarefas()

    def adicionar_tarefa(self, titulo, descricao, data_vencimento):
        tarefa = Tarefa(titulo, descricao, data_vencimento)
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def listar_tarefas(self):
        for tarefa in self.tarefas:
            print(tarefa)

    def editar_tarefa(self, indice, novo_titulo, nova_descricao, nova_data_vencimento):
        tarefa = self.tarefas[indice]
        tarefa.titulo = novo_titulo
        tarefa.descricao = nova_descricao
        tarefa.data_vencimento = nova_data_vencimento
        self.salvar_tarefas()

    def remover_tarefa(self, indice):
        del self.tarefas[indice]
        self.salvar_tarefas()

    def concluir_tarefa(self, indice):
        self.tarefas[indice].concluida = True
        self.salvar_tarefas()

    def salvar_tarefas(self):
        with open('tarefas.json', 'w') as f:
            json.dump([vars(tarefa) for tarefa in self.tarefas], f, indent=4)

    def carregar_tarefas(self):
        try:
            with open('tarefas.json', 'r') as f:
                tarefas_salvas = json.load(f)
                for tarefa in tarefas_salvas:
                    self.tarefas.append(Tarefa(**tarefa))
        except FileNotFoundError:
            pass

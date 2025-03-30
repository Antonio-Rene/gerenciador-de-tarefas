class Tarefa:
    def __init__(self, titulo, descricao, data_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.data_vencimento = data_vencimento
        self.concluida = False

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"{self.titulo} - {status} (Vencimento: {self.data_vencimento})"

from professor import Professor

class Fila_de_Prioridade:

    def __init__(self, fila_prioridade):
        self.fila_de_prioridade = fila_prioridade
        self.proxima = None
        self.fila_de_prioridade = Professor


    def push(self, professor):
        self.fila_de_prioridade = Fila_de_Prioridade(professor)
        self.fila_de_prioridade.proxima = self.proxima
        self.fila_de_prioridade.proxima = self.fila_de_prioridade
        self.__professor +=1


    def pop(self):
        self.__professor = self.__campus_atual
        self.__professor.pop(0)

    def empty(self, professor):
        atual = self.proxima

        while atual is not None:
            if atual.professor == professor:
                return True
            atual = atual.proxima
        return False

    def __str__(self):
        return self.fila_de_prioridade.__str__()
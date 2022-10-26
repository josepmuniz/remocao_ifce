from professor import Professor
from fila_de_prioridade import Fila_de_Prioridade

def filas_de_prioridades():
    professor1 = Professor("Gustavo")
    print(professor1)
    professor2 = Professor("Alexandre")
    print(professor2)

    fila_professor = Fila_de_Prioridade()
    fila_professor.push(professor1)
    fila_professor.push(professor2)

    print(fila_professor)

    fila_professor.pop()
    print(fila_professor)

    print(fila_professor.empty(professor1))
    print(fila_professor.empty(professor2))









if __name__ == '__main__':
    filas_de_prioridades()



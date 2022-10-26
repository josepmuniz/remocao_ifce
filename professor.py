from fila_de_prioridade import Fila_de_Prioridade

class Professor:

    def __init__(self, nome, professor, novo_professor):

        self.__nome = nome
        self.__idade = 0
        self.__matricula = 0
        self.__professor = professor
        self.__proxima = novo_professor
        self.__professor = Fila_de_Prioridade


    def string(self, string):
        self.__professor = string
        self.__nome = string
        self.__proxima = string
        self.__string = string
        self.subarea = string
        self.__campus_atual = string
        self.__campus_removido = string


    def inteiro(self, inteiro):
        self.__matricula = inteiro
        self.__idade = inteiro
        self.__inteiro = inteiro
        self.__tempo_ifce = inteiro
        self.__nota_concurso = inteiro


    def inserir(self, nome, idade, matricula, subarea, campus_atual, campus_removido, tempo_ifce, nota_concurso):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula
        self.subarea = subarea
        self.__campus_atual = campus_atual
        self.__campus_removido = campus_removido
        self.__tempo_ifce = tempo_ifce
        self.__nota_concurso = nota_concurso

        self.__nome += 1
        self.__idade +=1
        self.__matricula +=1
        self.__subarea +=1
        self.__nota_concurso +=1
        self.campus_atual +=1
        self.campus_removido = self.__campus_atual -1
        self.__tempo_ifce +=1
        self.__nota_concurso +=1



    def subarea(self, subarea):
        self.__subarea = subarea
        return self.__string

    def campus_atual(self,campus_atual):
        self.__campus_atual = campus_atual
        return self.__string

    def campus_removido(self, campus_removido):
        self.__campus_removido = campus_removido
        return self.__string

    def tempo_ifce(self):
        self.tempo_ifce = 0
        return self.__inteiro

    def nota_concurso(self):
        self.nota_concurso = 0
        return self.__inteiro


    def __str__(self):
        return self.__string

    def __int__(self):
        return self.__inteiro

    @property
    def proxima(self):
        return self.__proxima

    @proxima.setter
    def proxima(self, proxima):
        self.__proxima = proxima

    @property
    def professor(self):
        return self.__professor

    @property
    def nome(self):
        return self.__nome








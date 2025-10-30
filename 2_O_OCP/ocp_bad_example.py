'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''
from abc import ABC, abstractmethod

# Exemplo de uso:
class Exames(ABC):
    @abstractmethod
    def __init__(self, tipo: str) -> None: pass

    @abstractmethod
    def verifica_condicoes_exame(self, exame: Exames) -> True: pass

class ExameDeSangue(Exames):
    def __init__(self, tipo='sangue') -> None:
        self.tipo = tipo

    def verifica_condicoes_exame(self, exame: Exames) -> True:
        # implemente as condições específicas do exame de sangue
        return True

class ExameDeRaioX(Exames):
    def __init__(self, tipo='raio-x') -> None:
        self.tipo = tipo

    def verifica_condicoes_exame(self, exame: Exames) -> True:
        # implemente as condições específicas do exame de raio-x
        return True


class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exames) -> None:

        if exame.tipo == "sangue":
            if exame.verifica_condicoes_exame(exame):
                print("Exame sanguíneo aprovado!")

        elif exame.tipo == "raio-x":
            if exame.verifica_condicoes_exame(exame):
                print("Raio-X aprovado!")
                pass

exame_de_sangue = ExameDeSangue()
exame_de_raio_x = ExameDeRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_de_sangue)
aprovador.aprovar_solicitacao_exame(exame_de_raio_x)
class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

    def __str__(self):
        return f"Passageiro(nome={self.nome}, documento={self.documento})"


class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

    def __str__(self):
        return (f"Corrida(nota={self.nota}, distancia={self.distancia}km, "
                f"valor=R${self.valor}, passageiro={self.passageiro})")


class Motorista:
    def __init__(self, nome: str, idade: int, nota: float):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.corridas = []

    def adicionar_corrida(self, corrida: Corrida):
        self.corridas.append(corrida)

    def __str__(self):
        return (f"Motorista(nome={self.nome}, idade={self.idade}, nota={self.nota}, "
                f"corridas=[{', '.join(str(c) for c in self.corridas)}])")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.motorista_dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nome = input("Nome do motorista: ")
        idade = int(input("Idade do motorista: "))
        nota_motorista = float(input("Nota do motorista: "))

        motorista = Motorista(nome, idade, nota_motorista)

        while True:
            print("Nova corrida:")
            nota_corrida = float(input("Nota da corrida: "))
            distancia = float(input("Distância percorrida: "))
            valor = float(input("Valor da corrida: "))

            nome_passageiro = input("Nome do passageiro: ")
            documento_passageiro = input("Documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            motorista.adicionar_corrida(corrida)
            cont = input("Deseja adicionar outra corrida? (s/n): ").lower()
            if cont != 's':
                break
        self.motorista_dao.create_motorista(motorista)

    def read_motorista(self):
        id = input("ID do motorista: ")
        motorista = self.motorista_dao.read_motorista_by_id(id)
        if motorista:
            print("\n--- Dados do Motorista ---")
            print(f"Nome: {motorista.nome}")
            print(f"Idade: {motorista.idade}")
            print(f"Nota: {motorista.nota}")
            print("Corridas:")
            for i, corrida in enumerate(motorista.corridas, 1):
                print(f" Corrida {i}:")
                print(f"   Nota: {corrida.nota}")
                print(f"   Distância: {corrida.distancia} km")
                print(f"   Valor: R${corrida.valor}")
                print(f"   Passageiro: {corrida.passageiro.nome} ({corrida.passageiro.documento})")
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        id = input("ID do motorista a atualizar: ")
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        nota = float(input("Nova nota: "))
        update_data = {
            "nome": nome,
            "idade": idade,
            "nota": nota
        }
        self.motorista_dao.update_motorista(id, update_data)

    def delete_motorista(self):
        id = input("ID do motorista a deletar: ")
        self.motorista_dao.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()

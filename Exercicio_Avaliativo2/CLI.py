from database import Database
from teacher_crud import TeacherCRUD

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("\nDigite um comando (create, read, update, delete, quit): ").lower()
            if command == "quit":
                print("Encerrando o programa. Até mais!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")

class TeacherCLI(SimpleCLI):
    def __init__(self, teacher_crud):
        super().__init__()
        self.teacher_crud = teacher_crud
        self.add_command("create", self.create_teacher)
        self.add_command("read", self.read_teacher)
        self.add_command("update", self.update_teacher)
        self.add_command("delete", self.delete_teacher)

    def create_teacher(self):
        name = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento: "))
        cpf = input("Digite o CPF: ")
        self.teacher_crud.create(name, ano_nasc, cpf)
        print(f"Professor '{name}' criado com sucesso!")

    def read_teacher(self):
        name = input("Digite o nome do professor a ser buscado: ")
        resultado = self.teacher_crud.read(name)
        if resultado:
            for r in resultado:
                print(r)
        else:
            print("Professor não encontrado.")

    def update_teacher(self):
        name = input("Digite o nome do professor a ser atualizado: ")
        novo_cpf = input("Digite o novo CPF: ")
        self.teacher_crud.update(name, novo_cpf)
        print(f"CPF do professor '{name}' atualizado com sucesso!")

    def delete_teacher(self):
        name = input("Digite o nome do professor a ser deletado: ")
        self.teacher_crud.delete(name)
        print(f"Professor '{name}' deletado com sucesso!")


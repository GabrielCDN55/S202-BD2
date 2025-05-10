from database import Database
from teacher_crud import TeacherCRUD 

def main():
    db = Database("bolt://3.239.171.157:7687", "neo4j", "semaphores-aptitude-signalmen")
    teacher_crud = TeacherCRUD(db)
    db.drop_all()

    #b) 
    teacher_crud.create("Chris Lima", 1956, "189.052.396-66")
    print("Professor criado com sucesso")

    #c)
    resultado = teacher_crud.read("Chris Lima")
    print("Dados do professor:", resultado)

    #d)
    teacher_crud.update("Chris Lima", "162.052.777-77")
    print("dado atualizado")

    db.close()

if __name__ == "__main__":
    main()

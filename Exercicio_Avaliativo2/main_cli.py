from database import Database
from teacher_crud import TeacherCRUD
from CLI import TeacherCLI 

def main():
    db = Database("bolt://3.239.171.157:7687", "neo4j", "semaphores-aptitude-signalmen")
    teacher_crud = TeacherCRUD(db)
    
    cli = TeacherCLI(teacher_crud)
    cli.run()
    
    db.close()

if __name__ == "__main__":
    main()

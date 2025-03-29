from database import Database
from writeAJson import writeAJson
from MotoristaDAO import MotoristaDAO
from cli import MotoristaCLI

db = Database(database="motoristas", collection="motoristas")
motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()

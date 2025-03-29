from pymongo import MongoClient
from bson.objectid import ObjectId
from cli import Motorista, Corrida, Passageiro 

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista: Motorista):
        try:
            motorista_data = {
                "nome": motorista.nome,
                "idade": motorista.idade,
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": corrida.nota,
                        "distancia": corrida.distancia,
                        "valor": corrida.valor,
                        "passageiro": {
                            "nome": corrida.passageiro.nome,
                            "documento": corrida.passageiro.documento
                        }
                    }
                    for corrida in motorista.corridas
                ]
            }
            res = self.db.collection.insert_one(motorista_data)
            print(f"Motorista created with id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            data = self.db.collection.find_one({"_id": ObjectId(id)})
            if data:
                motorista = Motorista(data["nome"], data["idade"], data["nota"])
                for corrida_data in data.get("corridas", []):
                    passageiro = Passageiro(
                        corrida_data["passageiro"]["nome"], 
                        corrida_data["passageiro"]["documento"]
                    )
                    corrida = Corrida(
                        corrida_data["nota"], 
                        corrida_data["distancia"], 
                        corrida_data["valor"], 
                        passageiro
                    )
                    motorista.adicionar_corrida(corrida)
                print(f"motorista found: {motorista}")
                return motorista
            else:
                print("Motorista não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o motorista: {e}")
            return None

    def update_motorista(self, id: str, update_data: dict):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None

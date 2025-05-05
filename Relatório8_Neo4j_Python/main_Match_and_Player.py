from database import Database
from Match_and_Player_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.243.228:7687", "neo4j", "dereliction-stairs-connection")
db.drop_all()

# Criando uma instância da classe SchoolDatabase para interagir com o banco de dados
jogo_db = GameDatabase(db)

# Criando jogadores
jogo_db.create_player("p1", "João")
jogo_db.create_player("p2", "Gabriel")
jogo_db.create_player("p3", "Paulo")
jogo_db.create_player("p4", "Jonas")
jogo_db.create_player("p5", "Davi")
jogo_db.create_player("p6", "Ian")

# Criando partidas
jogo_db.create_match("m1")
jogo_db.create_match("m2")
jogo_db.create_match("m3")
jogo_db.create_match("m4")
jogo_db.create_match("m5")
jogo_db.create_match("m6")

# Registrando jogadores em partidas com pontuações
jogo_db.insert_player_match("p1", "m1", 10)
jogo_db.insert_player_match("p2", "m1", 20)
jogo_db.insert_player_match("p3", "m2", 15)
jogo_db.insert_player_match("p4", "m2", 25)
jogo_db.insert_player_match("p5", "m3", 30)
jogo_db.insert_player_match("p6", "m3", 5)
jogo_db.insert_player_match("p1", "m4", 18)
jogo_db.insert_player_match("p3", "m4", 22)
jogo_db.insert_player_match("p2", "m5", 12)
jogo_db.insert_player_match("p5", "m5", 28)
jogo_db.insert_player_match("p6", "m6", 19)
jogo_db.insert_player_match("p4", "m6", 21)

#Atualização
jogo_db.update_player("p1", "João Pedro")

#Exclusão
jogo_db.delete_player("p6")
jogo_db.delete_match("m3")

#Mostrando dados
print("Jogadores:")
print(jogo_db.get_players())

print("\nPartidas de Gabriel (p2):")
print(jogo_db.get_player_informacoes("p2"))

print("\nInformações da Partida m1:")
print(jogo_db.get_match_informacoes("m1"))

db.close()
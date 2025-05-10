from database import Database

db = Database("bolt://3.239.171.157:7687", "neo4j", "semaphores-aptitude-signalmen")
#db.drop_all()

#QUESTÃO 1

#a)
query = """
MATCH (t:Teacher {name: 'Renzo'})
RETURN t.ano_nasc, t.cpf
"""
print("a)", db.execute_query(query))

#b)
query = """
MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name, t.cpf
"""
print("b):", db.execute_query(query))

#c)
query = """
MATCH (c:City)
RETURN c.name
"""
print("c)", db.execute_query(query))

#d)
query = """
MATCH (s:School)
WHERE s.number >= 150 AND s.number <= 550
RETURN s.name, s.address, s.number
"""
print("d)", db.execute_query(query))

########################################################################################################################################################################################################

#QUESTÃO 2

#a)
query = """
MATCH (t:Teacher)
RETURN max(t.ano_nasc) AS MaisJovem, min(t.ano_nasc) AS MaisVelho
"""
print("a)", db.execute_query(query))

#b)
query = """
MATCH (c:City)
RETURN avg(c.population) AS MediaHabitantes
"""
print("b)", db.execute_query(query))

#c)
query = """
MATCH (c:City {cep: '37540-000'})
RETURN replace(c.name, 'a', 'A') AS NomeModificado
"""
print("c)", db.execute_query(query))

#d)
query = """
MATCH (t:Teacher)
RETURN substring(t.name, 2, 1) AS Caractere
"""
print("d)", db.execute_query(query))

db.close()
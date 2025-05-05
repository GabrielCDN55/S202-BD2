class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (:player {id: $player_id, name: $name})"
        parameters = {"player_id": player_id, "name": name}
        self.db.execute_query(query, parameters)

    def update_player(self, old_id, new_name):
        query = "MATCH (p:player {id: $old_id}) SET p.name = $new_name"
        parameters = {"old_id": old_id, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_id):
        query = "MATCH (p:player {id: $player_id}) DETACH DELETE p"
        parameters = {"player_id": player_id}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:player) RETURN p.id AS id, p.name AS name"
        results = self.db.execute_query(query)
        return [{"id": result["id"], "name": result["name"]} for result in results]

    def create_match(self, match_id):
        query = "CREATE (:Match {id: $match_id})"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def delete_match(self, match_id):
        query = "MATCH (m:Match {id: $match_id}) DETACH DELETE m"
        parameters = {"match_id": match_id}
        self.db.execute_query(query, parameters)

    def insert_player_match(self, player_id, match_id, pontos):
        query = """
        MATCH (p:player {id: $player_id}), (m:Match {id: $match_id})
        CREATE (p)-[:PARTICIPATED {pontos: $pontos}]->(m)
        """
        parameters = {"player_id": player_id, "match_id": match_id, "pontos": pontos}
        self.db.execute_query(query, parameters)

    def get_match_informacoes(self, match_id):
        query = """
        MATCH (p:player)-[r:PARTICIPATED]->(m:Match {id: $match_id})
        RETURN m.id AS match_id, p.id AS player_id, p.name AS player_name, r.pontos AS pontos
        """
        parameters = {"match_id": match_id}
        results = self.db.execute_query(query, parameters)
        return [{
            "match_id": result["match_id"],
            "player_id": result["player_id"],
            "player_name": result["player_name"],
            "pontos": result["pontos"]
        } for result in results]

    def get_player_informacoes(self, player_id):
        query = """
        MATCH (p:player {id: $player_id})-[r:PARTICIPATED]->(m:Match)
        RETURN m.id AS match_id, r.pontos AS pontos
        ORDER BY m.id
        """
        parameters = {"player_id": player_id}
        results = self.db.execute_query(query, parameters)
        return [{"match_id": result["match_id"], "pontos": result["pontos"]} for result in results]

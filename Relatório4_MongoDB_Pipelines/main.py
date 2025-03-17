from database import Database
from helper.WriteAJson import writeAJson
db = Database(database="mercado", collection="compras")
#db.resetDatabase()

# 1- Média de gasto total:
# result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#    {"$group": {"_id": None, "media": {"$avg": "$total"}}}
# ])

# writeAJson(result, "Média de gasto total")

# # 2- Cliente que mais comprou em cada dia:
# result = db.collection.aggregate([
#     {"$unwind": "$produtos"},
#     {"$group": {"_id": {"cliente": "$cliente_id", "data": "$data_compra"}, "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#     {"$sort": {"_id.data": 1, "total": -1}},
#     {"$group": {"_id": "$_id.data", "cliente": {"$first": "$_id.cliente"}, "total": {"$first": "$total"}}}
# ])

# writeAJson(result, "Cliente que mais comprou em cada dia")

# 3- Produto mais vendido:
#result = db.collection.aggregate([
#    {"$unwind": "$produtos"},
#    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
#    {"$sort": {"total": -1}},
#    {"$limit": 1}
#])

#writeAJson(result, "Produto mais vendido")

#----------------------------------------------EXERCICIOS PROPOSTOS----------------------------------------------#

class ProductAnalyzer:
    def __init__(self, db):
        self.db = db

    def total_vendas_por_dia(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$data_compra",
                "total_vendas": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"_id": 1}}
        ])
        return list(result)

    def produto_mais_vendido(self):
        result = self.db.collection.aggregate([
        {"$unwind": "$produtos"},
        {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
        {"$sort": {"total": -1}},
        {"$limit": 1}])
        return list(result)

    def cliente_mais_gastou(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$cliente_id",
                "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])
        return list(result)
        
    def produtos_vendidos_mais_1(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "total_vendido": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {"total_vendido": {"$gt": 1}}},
            {"$sort": {"total_vendido": -1}}
        ])
        return list(result)
        
analise = ProductAnalyzer(db)
#Mostra o produto mais vendido em todos os dias
print(analise.produto_mais_vendido())
#Mostra o valor total em reais das vendas realizadas no dia
print(analise.total_vendas_por_dia())
#Mostra o cliente que mais gastou em todos os dias
print(analise.cliente_mais_gastou())
#Mostra os produtos que tiveram uma quantidade vendida acima de 1
print(analise.produtos_vendidos_mais_1())
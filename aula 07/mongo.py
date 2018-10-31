#!/usr/bin/python3
from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from bson import objectid # funcao para importar e trabalhar com objectId do mongoDB / criar exemplo

try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))

#types
print(type(db.usuarios.find({"nome":"robson"})))
print(type(db.usuarios.find_one()))

# No mongoDB existe o findOne() e no python para nao quebrar o padrao foi implementado o find_one()
print(db.usuarios.find_one())

# Percorendo o cursor e printando cada registro
for usuario in db.usuarios.find():
    print(usuario)

# lista vazio
users = []

# converter o curosr em lista percorrendo o cursor
for usuario in db.usuarios.find():
    users.append(usuario)

# "Pretty print" pprint para melhor apresentacao em lista 
pprint(users)

users2 = []

# converter cursor em lista com list compression
users2 = [x for x in db.usuarios.find()]

pprint(users2)

# no python precisa passar aspas no nome do campo nas buscas
print (db.usuarios.find_one({'nome':'robson'}))

db.usuarios.remove({'nome':'joao'})
db.usuarios.update({'_id' :4},{'$set':{'sobrenome':'teixeira'}})

date = {
    '_id' : 6,
    'nome': 'jose',
    'sobrenome' : 'teixeira',
    'hora' : datetime.now().strftime('%d-%m-%Y %H:%M:%S')
}
db.usuarios.insert(date)




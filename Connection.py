from pymongo import MongoClient
from pprint import  pprint

#connessione in local a mongoDB
client = MongoClient('localhost', 27017)
pprint("Connessione stabilita")

#accesso al databaset e alla collezione interessata
database = client["dataset_covid"]
collection = database.covid_campania
collection2 = database.covid19_italy_province
listaCampania=[]

for documentCampania in collection.find():
    listaCampania.append(documentCampania)

result = database.collection.aggregate([
    {
        '$lookup': {
            'from': collection2,
            'localField': 'Latitudine',
            'foreignField': 'Latitude',
            'as': 'x'
        }
    }
])

for item in result:
    print(item)




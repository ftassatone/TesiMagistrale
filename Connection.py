from pymongo import MongoClient
from pprint import  pprint
from bson import objectid
import bson
from bson.codec_options import CodecOptions

#connessione in local a mongoDB
client = MongoClient('localhost', 27017)
pprint("Connessione stabilita")

#accesso al databaset e alla collezione interessata
database = client["dataset_covid"]
collectionCampania = database.covid_campania
collectionProvince = database.covid19_italy_province

for item in collectionCampania.find({}):
    z = item["Latitudine"]
    for itemProvince in collectionProvince.find():
        if z == itemProvince["Latitude"]:
            print("Latitudine: ", z, "Latitude: ", itemProvince["Latitude"])






from pymongo import MongoClient
import csv
import numpy as np

#connessione in local a mongoDB
#client = MongoClient('localhost', 27017)
from pymongo.errors import BulkWriteError

client = MongoClient("mongodb+srv://admin:admin@tesifrancescatassatone.jlr3s.gcp.mongodb.net/dataset_covid?retryWrites=true&w=majority")
print("Connessione stabilita")

#accesso al databaset e alla collezione interessata
db = client["dataset_covid"]
collectionRegion = db["covid19_italy_region"]
collectionProvince = db["covid19_italy_province"]

regionList = []
regionIndex = []
provinceList = []
provinceIndex = []


for itemRegion in collectionRegion.find({},{'_id': False}):
   regionList.append(itemRegion)
   regionIndex.append(itemRegion["RegionName"])

for itemProvince in collectionProvince.find({},{'_id': False}):
   provinceList.append(itemProvince)
   provinceIndex.append(itemProvince["RegionName"])

#se la collezione myOut esiste, la elimino e successivamente la ricreo
myOut = db["myOut"]
if "myOut" in db.list_collection_names():
    myOut.drop()
    print("Collection eliminata")
db.create_collection("myOut")
print("Collection creata")

#implementazione match regioni
arrReg = []
arrProv = []

for item in regionIndex:
    flag = True
    for item2 in provinceIndex:
        if item == item2:
            if flag == True:
                reg = regionIndex.index(item)
                arrReg.append(regionList[reg])
                flag = False
            prov = provinceIndex.index(item2)
            arrProv.append(provinceList[prov])


for i in range(arrProv.__len__() ):
    print("i ",i)
    myOut.insert_one(provinceList[i])
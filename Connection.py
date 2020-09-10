from pymongo import MongoClient
import csv

#connessione in local a mongoDB
client = MongoClient('localhost', 27017)
print("Connessione stabilita")

#accesso al databaset e alla collezione interessata
db = client["dataset_covid"]
collectionRegion = db["covid19_italy_region"]
collectionProvince = db["covid19_italy_province"]

regionList = []
regionIndex = []
provinceList = []
provinceIndex = []
newline = ''

with open('innovators.csv', 'w', ',') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

for itemRegion in collectionRegion.find({}):
   regionList.append(itemRegion)
   regionIndex.append(itemRegion["RegionName"])

for itemProvince in collectionRegion.find({}):
   provinceList.append(itemProvince)
   provinceIndex.append(itemProvince["RegionName"])



for item in regionIndex:
    for itemProvince in provinceIndex:
        if item == itemProvince:
            print(item, "-", itemProvince)
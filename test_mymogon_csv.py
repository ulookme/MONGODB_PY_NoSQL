import csv
import json
import pymongo
from pymongo import MongoClient

cluster=MongoClient("mongodb+srv://root:root@clusterch-i1t5r.azure.mongodb.net/test?retryWrites=true&w=majority")

db=cluster["test"]
collection=db["Nancy"]



post1={"id":1,"nom":"jack","prenom":"perdu","skill":"001","temps":"00:00"}
post2={"id":2,"nom":"jean","prenom":"jaune","skill":"101","temps":"02:00"}
post3={"id":3,"nom":"joe","prenom":"defis","skill":"021","temps":"10:00"}
post4={"id":4,"nom":"julie","prenom":"cava","skill":"401","temps":"00:30"}
post5={"id":5,"nom":"jeson","prenom":"fichier","skill":"006","temps":"40:00"}
post6={"id":6,"nom":"jaja","prenom":"jamais","skill":"091","temps":"12:00"}
post7={"id":7,"nom":"jaqueline","prenom":"aufond","skill":"301","temps":"01:00"}
post8={"id":8,"nom":"mercato","prenom":"remontada","skill":"1000","temps":"24:00"}

collection.insert_many([post1,post2,post3,post4,post5,post6,post7,post8])


#Charger le fichier CSV
fcsv = '/Library/Frameworks/R.framework/Versions/3.3/Resources/doc/BioC_mirrors.csv'


# l'emplacement de l'enregistrement du fichier json
fjson = '/Users/ano/Desktop/dossierpython/Jsondata_test_mongo'

data = []
#transformation du fichier CSV EN JSON
with open(fcsv) as csvfile:
    reader = csv.DictReader(csvfile)
    for rows in reader:
        data.append(rows)

# Enregistrer le fichier JSON

with open(fjson, 'w') as jsonFile:
    jsonFile.write(json.dumps(data, indent=2))
print("JSON enregistrer!")

print(data)

#observer l'interieur du fichier json
with open(fjson) as f:
    file_data = json.load(f)




#collection.insert_many(file_data)

resultas=collection.find({"CountryCode":"uk"})
print(resultas)

cluster.close()
print('Fichier Importer avec succes!!')
#Script 1
#For simply printing out part of read in scraped data, json reading and data slicing can work to print out specific components of the data after it's read in
#data.txt is the desired json file to be read in
import json
with open('data.txt') as json_file:
    data = json.load(json_file)
    for p in data['{ "_id" :']:
        print('"_id": ' + p['"_id"'])
        print('"groupID": ' + p['"groupID"'])
        print('"jobID"' + p['"jobID"'])
        print('"$date"' + p['"$date"'])
        print('')
        
#slicing data by printing sections
print(data[::2])    
#Script 2
#The json data is loaded using python functions for loading json data and then parsed according to desired output
jsonparse = json.loads("data.txt")
print(json.dumps(jasonparse, indent=4, sort_keys=True))
#It can be iterated over the full json file
for x in jsonparse:
	print("%s: %d" % (x, loaded_json[x]))
    
#Desired sections of the json dictionary can be loaded into pytrhon and printed individually as follows, printing 
#invididual sections of the data
with open('data.txt', 'r') as f:
    jsonparse = json.load(f)

for x in jsonparse:
    print(x['_id'])
    print(x['timestamp'])
    print(x[entry])
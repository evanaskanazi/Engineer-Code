#Script 
#For simply printing out part of read in scraped data, json reading and data slicing can work to print out specific components of the data after it's read in

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

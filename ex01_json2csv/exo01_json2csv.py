import os,json,csv

file = "sample.json"

if os.path.exists(file):
    
    with open(file,"r") as file:
        data = json.load(file) # is a Dictionnary

    key = list(data)[0] #need to cast in list to get first element @see dico_key
    diseases = data[key]    
    fieldnames = diseases[0].keys() # get my fieldnames for csv
    
    csvfile = open("data_file.csv","w+")
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames) # as dico, need DictWriter
    csvwriter.writeheader()
    
    for element in diseases:
        csvwriter.writerow(element)
    print("Job done !")
else:
    print("File doesn't exist ... " + file)





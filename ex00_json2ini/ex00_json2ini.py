import os,json

file = "sample.json"
string = ""

if os.path.exists(file):
    
    with open(file,"r") as file : 
        data = json.load(file)
        
    data.keys()
    
    for section in data.keys():
        string += "[" + section + "]" + "\n"
        for values in data[section].keys():
            string +=  values + " = " + data[section][values] + "\n"
        string += "\n"
        
    with open('file.ini', 'w') as file:
        file.write(string)
       
else:
    print("File doesn't exist .. ")


    

    
    
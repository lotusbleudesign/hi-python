import os,json

file = "sample.json"
string = ""

if os.path.exists(file):
    
    with open(file,"r") as file : 
        data = json.load(file)
        
    for section in data.keys():
        string += "[" + section + "]" + "\n"
        sectionElement = data[section]
        for key in sectionElement.keys():
            string +=  key + " = " + sectionElement[key] + "\n"
        string += "\n"
        
    with open('file.ini', 'w') as file:
        file.write(string)
        print("Job done !")
       
else:
    print("File doesn't exist .. ")


    

    
    
import csv 
import ast 
from utils import get_headers
impure = 0

def removespces(val):
    if (val[0] == ' '): val = val[1:]
    if (val[-1] == ' '): val = val[:-1]
    return val

def getNameCountry(val):
    val = val.replace('"', '')
    val = val.replace("'", "")
    val = val.replace("[", "")
    val_l = val.split(',')
    return removespces(val_l[0]), removespces(val_l[1])

def fillingDict(dictionary1, dictionary2):
    global impure
    #bating and fieldin
    listabf = ['ListA', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    testsbf = ['Tests', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    twbf = ['T20s', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    odibf = ['ODIs', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

    #bowling
    listabw = ['ListA', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    testsbw = ['Tests', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    twbw = ['T20s', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    odibw = ['ODIs', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    
    #filling batting and fielding dictionary
    if 'Tests' not in dictionary1 : dictionary1['Tests'] = testsbf
    if 'T20s' not in dictionary1 : dictionary1['T20s'] = twbf    
    if 'ODIs' not in dictionary1 : dictionary1['ODIs'] = odibf
    
    #filling bowling dictionary
    if 'Tests' not in dictionary2 : dictionary2['Tests'] = testsbw
    if 'T20s' not in dictionary2 : dictionary2['T20s'] = twbw    
    if 'ODIs' not in dictionary2 : dictionary2['ODIs'] = odibw
    
    return dictionary1, dictionary2

def structure_data(csv_path, output_path):
    infile = open(csv_path, 'r')
    reader = csv.reader(infile, delimiter=',', quotechar='|')
    lists = []
    for row in reader:
        row = str(row).replace('\n', '')
        if not row == '':
            lists.append(row)
        
    with open(output_path, 'w+') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow(get_headers())
        iteration = 1
        for lst in lists:
            print ("Iteration: {}".format(iteration))
            try:
                row_split = lst.split('{')
                dict1 = ast.literal_eval('{'+row_split[1].replace('}', '')[:-4]+'}')  #batting and fielding dictionary
                dict2 = ast.literal_eval('{'+row_split[2].replace('}', '')[:-2]+'}')  #bowling dictionary
                name, country = getNameCountry(row_split[0])
                dict1, dict2 = fillingDict(dict1, dict2)
                #filter the bad out
                if len(dict1['Tests']) < 15 : 
                    continue
                if len(dict1['T20s']) < 15 : 
                    continue
                if len(dict1['ODIs']) < 15:
                    continue
                if len(dict2['Tests']) < 14 : 
                    continue
                if len(dict2['T20s']) < 14 : 
                    continue     
                if len(dict2['ODIs']) < 14:
                    continue
                
                data = [name, country]
                data.extend(dict1['ODIs'])
                data.extend(dict1['Tests'])
                data.extend(dict1['T20s'])
                data.extend(dict2['ODIs'])
                data.extend(dict2['Tests'])
                data.extend(dict2['T20s'])
                writer.writerow(data)
            except Exception as E:
                print(E)
            iteration += 1
            
    print("impurity added: {}".format(impure))          

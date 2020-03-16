import csv

with open('cb_checks.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter =',', quotechar='|')
    data = list(reader)
    print(data)
    
        

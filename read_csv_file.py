import csv
filepath='C:/.../somename.csv'

with open(filepath,'r') as f:
    reader = list(csv.reader(f))
    for row in reader:
        '''
        Do Something
        '''

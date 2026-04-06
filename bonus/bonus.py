filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentatation.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1) 
    #this only replaces the first instance, the '1', from '.' to '-'
    
    print(filename)
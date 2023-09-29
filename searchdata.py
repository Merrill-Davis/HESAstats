import csv

filenames = []

for years in range(1995,2022):
    filenames.append("formatted" + str(years) + str(years + 1) + ".csv")
    
def search(HEprovider="York", country=None, level="all", mode="all", category_marker="total", category="total"):
    
    if country != None and HEprovider != None:
        raise Exception("Cannot select university while also choosing region")
    
    '''Available Configs are as follows
    
    HEProvider - University names, as a list
    level - all, all postgraduate, all undergraduate
    mode - all, part-time, full-time
    category marker, category - (total, total) (domicile, total non-uk or total uk)
    
    
    '''
    
    
    filenames = []
    for years in range(1995,2022):
        filenames.append("formatted" + str(years) + str(years + 1) + ".csv")
    outputdata = dict()
    for filename in filenames:
        year = filename[9:13] + "-" + filename[13:17]
        print(year)
    
        try:
            mydata = open(filename)
        except:
            print("file: " + filename + " not found")
            continue
    
        reader = csv.reader(mydata, delimiter = ',')
        next(reader)
        for row in reader:
            tmpconfirmname = False
            if type(HEprovider) == list:
                for univs in HEprovider:
                    if univs.lower() in row[0].lower():
                        tmpconfirmname = True
            elif country.lower() == row[1].lower():
                tmpconfirmname = True
            if level.lower() == row[2].lower() and tmpconfirmname == True:
                if mode.lower() == row[3].lower():
                    if category_marker.lower() == row[4].lower():
                        if category.lower() == row[5].lower():
                            if row[0].lower() not in outputdata:
                                outputdata[row[0].lower()] = [year, row[6]]
                            else:
                                #outputdata[row[0].lower()] +=[year, row[6]]
                                tmp = outputdata[row[0].lower()]
                                outputdata.update({row[0].lower() : tmp + [year, row[6]] }) 
        mydata.close()                   
    formattedoutputdata = []
    for unis in outputdata:
        for index in range(0,len(outputdata[unis]),2):
            formattedoutputdata.append([str(unis), outputdata[unis][index],outputdata[unis][index + 1]])
    
    newdata = open("TempExport.csv","w",newline = "")
    writer = csv.writer(newdata)
    writer.writerow(["University","Year","Value"])
    writer.writerows(formattedoutputdata)
    newdata.close()
    return formattedoutputdata

print(search(["york","durham"],level="all undergraduate",mode="all"))

#print(search(HEprovider=None,country="england",level="all postgraduate",mode="all"))
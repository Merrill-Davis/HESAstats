import csv

category_domicile = ["total uk","total non-uk"]

filenames = []
savefilenames = []
for add in range(0,8):
    filenames.append("table 1-(" + str(2014 + add) + "-" + str(15 + add) + ").csv")
    savefilenames.append(str(2014 + add) + str(2015 + add) + ".csv")
for year in filenames:
    filename = year
    
    try:
        mydata = open(filename)
    except:
        print("file: " + filename + " not found")
        continue
    
    reader = csv.reader(mydata, delimiter = ',')
    
    outputdata = []
    for row in reader:
        '''uniname = "TO BE REMOVED"
        country = "TO BE REMOVED"
        level = "TO BE REMOVED"
        modeofstudy = "TO BE REMOVED"
        category_marker = "TO BE REMOVED"
        category = "TO BE REMOVED"
        value = "TO BE REMOVED"
        '''
        if not row[10].isdigit():
            continue
        if row[9].lower() in category_domicile:
            if not row[8].lower() == "domicile":
                continue
            elif not row[6].lower() == "all":
                continue
            elif row[5].lower() not in ["all postgraduate","all undergraduate","all"]:
                continue
        elif row[9].lower() == "total":
            if not row[8].lower() == "total":
                continue
        else:
            continue
        if row[4].lower() != "all":
            continue
        if row[3].lower() != "all":
            continue
        if row[2].lower() == "all":
            if row[1] != "total":
                continue
        
                
        uniname = row[1]
        if uniname == "total":
            uniname = "all"
        country = row[2]
        level = row[5]
        modeofstudy = row[6]
        category_marker = row[8]
        category = row[9]
        value = row[10]
        
        outputdata.append([uniname,country,level,modeofstudy,category_marker,category,value])
        
    mydata.close()
    newfilename = "formatted" + savefilenames[filenames.index(filename)]
    newdata = open(newfilename,"w",newline = "")
    writer = csv.writer(newdata)
    writer.writerow(["HE provider","Country of HE provider","Level of study","Mode of study","Category marker","Category","Number"])
    writer.writerows(outputdata)
    newdata.close()
    
    print("Year done" + filename)
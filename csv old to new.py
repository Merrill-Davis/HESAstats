import csv

def replacemultichar(word,stringofchars):
    for char in stringofchars:
        word = word.replace(char,"")
    return word

filenames = []

for add in range(0,19):
    filenames.append(str(1995 + add) + str(1996 + add) + ".csv")

for year in filenames:
    filename = year
    
    try:
        mydata = open(filename)
    except:
        print("file: " + filename + " not found")
        continue
    
    reader = csv.reader(mydata, delimiter = ',')
    headers = [item.lower() for item in next(reader)]
    print(headers)
    outputdata = []
    countries = ["england","wales","scotland","northern ireland"]
    country = "all"

    for row in [row for row in reader if row[0] != ""]:
        tmpfulltime = 0
        tmpparttime = 0
        tmpuk = 0
        tmpoverseas = 0
        if row[0].split(" ", 1)[-1].lower() in countries:
            country = row[0].split(" ", 1)[-1].lower()
            
        for index in range(1,len(headers)):
            uniname = replacemultichar(row[0],"()#1234567890").lower()
            if uniname == "total uk":
                uniname = "all"
            if uniname in ["total england","total scotland","total wales","total northern ireland"]:
                uniname = "total"
            if headers[index] == "total he students":
                outputdata.append([uniname,country,"all","all","total","total",row[index]])
            elif headers[index] == "pg-total-all":
                outputdata.append([uniname,country,"All postgraduate","all","total","total",row[index]])
            elif headers[index] == "pg-full-time":
                outputdata.append([uniname,country,"All postgraduate","full-time","total","total",row[index]])
                tmpfulltime += int(row[index])
            elif headers[index] == "pg-part-time":
                outputdata.append([uniname,country,"All postgraduate","part-time","total","total",row[index]])
                tmpparttime += int(row[index])
            elif headers[index] == "pg-total-uk":
                outputdata.append([uniname,country,"All postgraduate","all","domicile","total uk",row[index]])
                tmpuk += int(row[index])
            elif headers[index] == "pg-total-overseas":
                outputdata.append([uniname,country,"All postgraduate","all","domicile","total non-uk",row[index]])
                tmpoverseas += int(row[index])
            elif headers[index] == "ug-total-all":
                outputdata.append([uniname,country,"All undergraduate","all","total","total",row[index]])
            elif headers[index] == "ug-full-time":
                outputdata.append([uniname,country,"All undergraduate","full-time","total","total",row[index]])
                tmpfulltime += int(row[index])
            elif headers[index] == "ug-part-time":
                outputdata.append([uniname,country,"All undergraduate","part-time","total","total",row[index]])
                tmpparttime += int(row[index])
            elif headers[index] == "ug-total-uk":
                outputdata.append([uniname,country,"All undergraduate","all","domicile","total uk",row[index]])
                tmpuk += int(row[index])
            elif headers[index] == "ug-total-overseas":
                outputdata.append([uniname,country,"All undergraduate","all","domicile","total non-uk",row[index]])
                tmpoverseas += int(row[index])
            else:
                print(index)
                raise ValueError("Unknown column key")
        outputdata.append([uniname,country,"all","full-time","total","total",str(tmpfulltime)])
        outputdata.append([uniname,country,"all","part-time","total","total",str(tmpparttime)])
        outputdata.append([uniname,country,"all","all","domicile","total uk",str(tmpuk)])
        outputdata.append([uniname,country,"all","all","domicile","total non-uk",str(tmpoverseas)])

    mydata.close()

    newfilename = "formatted" + filename
    newdata = open(newfilename,"w",newline = "")
    writer = csv.writer(newdata)
    writer.writerow(["HE provider","Country of HE provider","Level of study","Mode of study","Category marker","Category","Number"])
    writer.writerows(outputdata)
    newdata.close()
    print("done years" + filename)

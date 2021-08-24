import re
if __name__ == '__main__':
    FH = open(r"./assets/SchoolTest.csv",'r')
    FH.readline()
    data = FH.readlines()
    school_dict = {}
    citySchool = {}
    maxcountSchool = float("-inf")
    uniqueCities = []
    locale={}
    city = ""
    for elt in data:
        rowData = elt.split(";")
        # print(rowData)
        schoolId, locId, region, schoolName, cityName, statecode = rowData[0],rowData[1],rowData[2],rowData[3],rowData[4],rowData[5]
        if statecode in school_dict:
            school_dict[statecode].append(schoolName)
        else:
            school_dict[statecode] = [schoolName]
        if region in locale:
            locale[region].append(schoolName)
        else:
            locale[region] = [schoolName]
        if cityName in citySchool:
            citySchool[cityName].append(schoolName)
        else:
            citySchool[cityName] = [schoolName]
    print(f"Total Schools are {len(data)}")
    print('*'*30)
    print("The number of schools pertaining to each state are as follows:- ")
    for key in school_dict:
        print(f"{key}: {len(school_dict[key])}")
    print('*' * 30)
    print("The number of schools pertaining to each Locale are as follows:- ")
    for key in locale:
        print(f"{key} : {len(locale[key])}")
    for key,value in citySchool.items():
        if len(citySchool[key])>maxcountSchool:
            city, maxcountSchool = key, len(citySchool[key])
    print('*' * 30)
    print(f"{city} has maximum schools and the number of schools are :{maxcountSchool}")
    for key in citySchool:
        if len(citySchool[key])>1:
            if key not in uniqueCities:
                uniqueCities.append(key)
    print('*' * 30)
    print(f"{len(uniqueCities)} are the unique number of Cities having Schools greater than 1 and the Cities are {uniqueCities}")

    print('*' * 30)

    inpSchool, inpCity, inpState = input().split(" ")
    if inpSchool is not None:
        for elt in data:
            rowData = elt.split(";")
            if inpSchool in rowData[3]:
                print(rowData)
    
    # if inpCity is not None:
    #     for elt in data:
    #         rowData = elt.split(";")
    #         if inpCity in rowData:
    #             print(rowData)
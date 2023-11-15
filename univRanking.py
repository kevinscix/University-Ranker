# Name: Kevin Wu
# Student Number: 251284607

#finds the capital when given country
def findContinentByCountryName(selectedCountry, capitalsInfo):
    selectedCountryUpper = selectedCountry.upper()
    countryIndex = capitalsInfo.index(selectedCountryUpper)
    return (capitalsInfo[countryIndex+2])

#1 Universities Count
# finds the number of universities in the rankins
def findNumberOfUni(rankingInfo):
    file = open("output.txt", "w")
    uniCount = 0
    for i in range(0, len(rankingInfo), 5):
        uniCount += 1
    str = "Total number of universities => {0}".format(uniCount)
    file.write(str)
    file.write("\n")
    file.close()

#2 Available countries
# finds what countries are in the rankings
def findAvailableCountries(rankingInfo):
    file = open("output.txt", "a")
    availableCountries = []
    for i in range(2, len(rankingInfo), 5):
        if rankingInfo[i] in availableCountries:
            continue
        else:
            availableCountries.append(rankingInfo[i].upper())
    file.write("Available countries => ")
    for i in range(0, len(availableCountries)):
        if i == len(availableCountries)-1:
            file.write("{0}".format(availableCountries[i]))
            file.write("\n")
        else:
            file.write("{0}, ".format(availableCountries[i]))
    file.close()


#3 Availabe Continents
# finds the continents that are in the rankings
def findAvaiabeContinents(capitalsInfo):
    file = open("output.txt", "a")
    availableContinents = []
    for i in range(2, len(capitalsInfo), 3):
        if capitalsInfo[i] in availableContinents:
            continue
        else:
            availableContinents.append(capitalsInfo[i].upper())
    file.write("Available continents => ")
    for i in range(0, len(availableContinents)):
        if i == len(availableContinents)-1:
            file.write("{0}".format(availableContinents[i]))
            file.write("\n")
        else:
            file.write("{0}, ".format(availableContinents[i]))
    file.close()


#4 Highest ranking uni
# finds highest ranking uni internationally in the country
def findHighestRank(selectedCountry, rankingInfo):
    file = open("output.txt", "a")
    rank = 10000000000
    insitution = ""
    for i in range(0, len(rankingInfo), 5):
        if int(rankingInfo[i]) < rank and rankingInfo[i+2] == selectedCountry:
            insitution = rankingInfo[i+1]
            rank = int(rankingInfo[i])
    file.write("At international rank => {0} the university name is => {1}".format(rank, insitution.upper()))
    file.write("\n")
    file.close()

#5 Highest national ranking uni
# finds highest ranking country in the nation
def findTopNationalRank(selectedCountry, rankingInfo):
    file = open("output.txt", "a")
    rank = 1000000000
    insitution = ""
    for i in range(3, len(rankingInfo), 5):
        if int(rankingInfo[i]) < rank and rankingInfo[i-1] == selectedCountry:
            insitution = rankingInfo[i-2]
            rank = int(rankingInfo[i])
    file.write("At national rank => {0} the university name is => {1}".format(rank, insitution.upper()))
    file.write("\n")
    file.close()


#6 Average score
# Finds average score of unis in the country
def findAverageScore(selectedCountry, rankingInfo):
    file = open("output.txt", "a")
    sum = 0
    numOfUni = 0
    for i in range(4, len(rankingInfo), 5):
        if rankingInfo[i-2] == selectedCountry:
            sum += float(rankingInfo[i])
            numOfUni += 1
    averageScore = sum/numOfUni

    file.write("The average score => %.2f" % (averageScore))
    file.write("\n")
    file.close()

    # returns the score for use in later questions
    return averageScore

#7 Relative score
# Finds relative score in relation to the continent
def findRelativeScore(averageScore, continent, rankingInfo, capitalsInfo):
    file = open("output.txt", "a")
    countriesInContinent = []
    for i in range(2, len(capitalsInfo), 3):
        if capitalsInfo[i] == continent:
            countriesInContinent.append(capitalsInfo[i-2])
    maxScore = 0.0
    for i in range(2, len(rankingInfo), 5):
        if rankingInfo[i] in countriesInContinent:
            if float(rankingInfo[i+2]) > maxScore:
                maxScore = float(rankingInfo[i+2])

    relativeScore = (averageScore / maxScore) * 100

    file.write("The relative score to the top university in {0} is => ({1:.2f} / {2:.2f}) x 100% = {3:.3f}%".format(continent.upper(), averageScore, maxScore, relativeScore))
    file.write("\n")
    file.close()


#8 Capital city
# Finds the capital city of the country
def findCapitalCity(selectedCountry, capitalsInfo):
    selectedCountryUpper = selectedCountry.upper()
    file = open("output.txt", "a")
    countryIndex = capitalsInfo.index(selectedCountryUpper)
    capital = capitalsInfo[countryIndex+1].upper()

    file.write("The capital is => {0}".format(capital))
    file.write("\n")
    file.close()

#9 Universities with capital in name
# Finds the unis with the capital of its country in its name
def findCaptialNameUni(selectedCountry, capitalsInfo, rankingInfo):
    selectedCountryUpper = selectedCountry.upper()
    file = open("output.txt", "a")
    countryIndex = capitalsInfo.index(selectedCountryUpper)
    capital = capitalsInfo[countryIndex+1]
    listOfSchools = []
    for i in range(2, len(rankingInfo), 5):
        if rankingInfo[i] == selectedCountryUpper:
            if capital in rankingInfo[i-1]:
                listOfSchools.append(rankingInfo[i-1])
    file.write("The universities that contain the capital name => ")
    file.write("\n")
    for i in range(0, len(listOfSchools)):
        file.write("#{0} {1}".format(i+1, listOfSchools[i]).upper())
        file.write("\n")
    file.close()


# opens files and reads data and stores it in lists for use in future questions
def getInformation(selectedCountry,rankingFileName,capitalsFileName):
    selectedCountryUpper = selectedCountry.upper()
    # Reads data from files
    rankingInfo = loadCSVData(rankingFileName)
    capitalsInfo = loadCSVData(capitalsFileName)

    #Finds continent which country is located in
    continent = findContinentByCountryName(selectedCountryUpper, capitalsInfo)


    #1 Universities Count
    numOfUni = findNumberOfUni(rankingInfo)

    
    #2 Available Countries
    availableCountries = findAvailableCountries(rankingInfo)


    #3 Available Continents
    availableContinents = findAvaiabeContinents(capitalsInfo)

    #4 Highest ranking uni
    highestRankingUni = findHighestRank(selectedCountryUpper, rankingInfo)


    #5 Top National Rank
    topNationalRank = findTopNationalRank(selectedCountryUpper, rankingInfo)


    #6 The average score
    averageScore = findAverageScore(selectedCountryUpper, rankingInfo)


    #7 The relative score
    relativeScore = findRelativeScore(averageScore, continent, rankingInfo, capitalsInfo)


    #8 The capital city
    captialCity = findCapitalCity(selectedCountry, capitalsInfo)


    #9 University with capital name
    captialNameUni = findCaptialNameUni(selectedCountry, capitalsInfo, rankingInfo)


# Opens files reads and stores the data into lissts
def loadCSVData(filename):
    # This function is intended to load the content of filename and return the content in a list format. Any exception in this function should be handled.
    list = []
    fileContent = open(filename, "r", encoding='utf8')
    count = 0
    for line in fileContent:
        line = line.upper().strip()
        if count != 0:
            templist = line.split(",")
            if filename == "capitals.csv":
                templist.pop(2)
                templist.pop(2)
                templist.pop(2)
                for item in templist:
                    list.append(item)
            elif filename == "TopUni.csv":
                templist.pop(4)
                templist.pop(4)
                templist.pop(4)
                templist.pop(4)
                for item in templist:
                    list.append(item)

        else:
            count += 1
    fileContent.close()
    return list

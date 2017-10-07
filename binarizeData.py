import numpy as np

##<<<<<<< HEAD
## Load training data and convert into two-dimensional array.
## Find unique features and construct feature array to be used
## in Perceptron.

def BinarizeData(dataSet):

    if dataSet == "train" or "dev" or "test":

        rawData = np.genfromtxt("income-data/income." + dataSet + ".txt",
               dtype=[('f0', '<U4'), ('f1', 'U17'),
                      ('f2', 'U13'), ('f3', 'U22'),
                      ('f4', 'U18'), ('f5', 'U19'),
                      ('f6', 'U7'), ('f7', '<i4'),
                      ('f8', 'U27'), ('f9', 'U6')],
               delimiter=", ")

        data = np.array(rawData.tolist())

        for i in range(0, len(data)):
            data[i, 0] = 'Age ' + data[i, 0]
            data[i, 7] = data[i, 7] + ' Hours'

        if dataSet == 'train':

            age = np.unique(data[:,0])
            work = np.unique(data[:,1])
            education = np.unique(data[:,2])
            maritalstatus = np.unique(data[:,3])
            occupation = np.unique(data[:,4])
            race = np.unique(data[:,5])
            gender = np.unique(data[:,6])
            workhours = np.unique(data[:,7])
            country = np.unique(data[:,8])
            salary = np.unique(data[:,9])

            featureArray = np.hstack((age, work, education,
                        maritalstatus, occupation, race,
                        gender, workhours, country, ['Bias']))

            return featureArray, data

        else:

            return data

    else:

        print("Invalid file name")
        return
##=======

##def BinarizeData():
##
##    data = np.genfromtxt("income-data/income.train.txt",
##               dtype=None,
##               delimiter=", ")
##
##    age = set(data['f0'])
##    work = set(data['f1'])
##    education = set(data['f2'])
##    relationship = set(data['f3'])
##    occupation = set(data['f4'])
##    race = set(data['f5'])
##    gender = set(data['f6'])
##    workhours = set(data['f7'])
##    country = set(data['f8'])
##    salary = set(data['f9'])
##
##    columns = len(age) + len(work) + len(education) + len(relationship) + len(occupation) + len(race) + len(gender) + len(workhours) + len(country) + len(salary)
##
##    newdata = [[0 for x in range(columns)] for y in range(data.size)]
##
##    for index,row in enumerate(data):
##        count = 0
##        for i in age:
##            if i == row[0]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in work:
##            if i == row[1]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in education:
##            if i == row[2]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in relationship:
##            if i == row[3]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in occupation:
##            if i == row[4]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in race:
##            if i == row[5]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in gender:
##            if i == row[6]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in workhours:
##            if i == row[7]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in country:
##            if i == row[8]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##        for i in salary:
##            if i == row[9]:
##                newdata[index][count] = 1
##            else:
##                newdata[index][count] = 0
##            count += 1
##
##    return newdata, columns
##>>>>>>> 3482cde8755e79c4d2ee5ac2852bd61122ccc1c4

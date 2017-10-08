import numpy as np

## Load training data and convert into two-dimensional array.
## Find unique features and construct feature array to be used
## in Perceptron.

def BinarizeData(sort=0, shuffle=0):

    rawTrainData = np.genfromtxt("income-data/income.train.txt",
           dtype=[('f0', '<i4'), ('f1', 'U17'),
                  ('f2', 'U13'), ('f3', 'U22'),
                  ('f4', 'U18'), ('f5', 'U19'),
                  ('f6', 'U7'), ('f7', '<i4'),
                  ('f8', 'U27'), ('f9', 'U6')],
           delimiter=", ")

    data = np.array(rawTrainData.tolist())

    rawDevData = np.genfromtxt("income-data/income.dev.txt",
           dtype=[('f0', '<i4'), ('f1', 'U17'),
                  ('f2', 'U13'), ('f3', 'U22'),
                  ('f4', 'U18'), ('f5', 'U19'),
                  ('f6', 'U7'), ('f7', '<i4'),
                  ('f8', 'U27'), ('f9', 'U6')],
           delimiter=", ")

    devData = np.array(rawDevData.tolist())

    if sort == 1:
        rawTrainData = np.sort(rawTrainData, order='f9', axis=0)
        rawTrainData = np.flip(rawTrainData, axis=0)

    data = np.array(rawTrainData.tolist())

    if shuffle == 1:
        np.random.shuffle(data)

    #for i in range(0, len(data)):
    #    data[i, 0] = 'Age ' + data[i, 0]
    #    data[i, 7] = data[i, 7] + ' Hours'

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

    featureArray = np.hstack((work, education,
                maritalstatus, occupation, race,
                gender, country, ['Age'], ['WorkHours'], ['Bias']))


    binarizedData = []
    binarizedDevData = []

    permutation = [7,0,1,2,3,4,5,8,6,9]

    isort = np.argsort(permutation)

    newdata = data[:, isort]
    newDevData = devData[:, isort]
    #print(newdata)

    for i in range(0, len(data)):
        row = np.isin(featureArray[:-3], newdata[i, :-3])
        row2 = np.append(row.astype(int), [data[i, 0], data[i, 7], 1])

        binarizedData.append(row2.astype(int))
        #print(binarizedData[i])


    toInt = lambda i: int(i == '>50K')
    toIntFunc = np.vectorize(toInt)
    salary = toIntFunc(data[:,-1:])

    finalData = np.concatenate([binarizedData,salary], axis=1)
    
    #print(binarizedData[0])
    #print(len(finalData[0]))

    for i in range(0, len(devData)):
        devRow = np.isin(featureArray[:-3], newDevData[i, :-3])
        devRow2 = np.append(devRow.astype(int), [devData[i, 0], devData[i, 7], 1])
              
        binarizedDevData.append(devRow2.astype(int))
        #print(binarizedData[i])


    toInt = lambda i: int(i == '>50K')
    toIntFunc = np.vectorize(toInt)
    salaryDev = toIntFunc(devData[:,-1:])

    finalDevData = np.concatenate([binarizedDevData,salaryDev], axis=1)
    
    #print(binarizedData[0])
    #print(len(finalData[0]))
    
    return finalData, finalDevData, featureArray

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
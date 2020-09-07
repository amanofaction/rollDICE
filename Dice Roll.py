import numpy as np

#Validating the user input of number of dice
value = False
noOfdice=input('Enter no of dices(1-8): ')

while value==False:
    try:
        #Check if user enters an integer value, if not then an exception is thrown and user have to re-enter it
        noOfdice=int(noOfdice)
        if noOfdice>=1 and noOfdice<=8:
            value=True
        else:
            print('Value not in range(1-8)')
    except:
        print('Invalid input, please enter an integer value')
    if value==False:
        noOfdice=input('Enter no of dices(1-8): ')

#Validating the user input of number of rolls
value = False
noOfRolls=input('Enter no of Rolls(>=1): ')
while value==False:
    try:
        #Check if user enters an integer value, if not then an exception is thrown and user have to re-enter it
        noOfRolls=int(noOfRolls)
        if noOfRolls>=1:
            value=True
        else:
            print('Value not in greater than 0')
    except:
        print('Invalid input, please enter an integer value')
    if value==False:
        noOfRolls=input('Enter no of Rolls(>=1): ')

#Creating an integer array of size no of dice * no of rolls and fill it with random numbers 1-6
array = np.random.randint(1,7,(noOfdice,noOfRolls))

#print(array)

#Counting the occurance of each integer in the array
unique,counts=np.unique(array,return_counts=True)
count=dict(zip(unique, counts))

#Calculating the actual percentage probability as there are 6 faces so probability of each face is 1/6 
actual=1/6*100

#Calculating the percentage occurance of each face
total=sum(count.values())
for k,v in count.items():
    percentage = round((v/total)*100, 2)
    count[k]=percentage
print(count)


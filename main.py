#Name: Hamani ewetan
#Date: 24/3/25
#Title: List and average
#discription: this program makes a list of a hundred random numbers and then finds the average of those hundred numbers
import random
numbers=[]
for index in range(1,100):   
    num=random.randint(0,100)
    print(num)
    numbers.append(num)
average=(sum(numbers)/100)
print("average is", average)
        
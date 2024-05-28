import csv
import time

#Reading values of Runtimes of algorithums from txt file
given_file = open (file = 'Nvalues.txt', mode = 'r')
lines = given_file. read ()
numbers = []
arr = lines.split()
for s in arr:
 num = s
 numbers.append(num)
print(numbers)

#Reading values of Runtimes of algorithums from txt file
with open("Nvalues.csv", mode='w',newline='') as file:
    writer = csv.writer(file)
    for i in numbers: 
        writer.writerow([i])
 
        


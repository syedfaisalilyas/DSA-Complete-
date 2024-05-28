# -*- coding: utf-8 

#Problem 1

print("Answer 1:")

givenfile = open(file = '"C:\DSA\Lab 1\test.txt"',mode = 'r')

lines = givenfile.read()
arr = []
arrr = lines.split()
for s in arrr:
 num = int(s)
 arr.append(num)

result = []

def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            result.append(i)
        else:
            continue
        
search(arr, 2)

print(result)


#problem 2

print("Answer 2")
print(sorted(arr))           
#Problem 3

print("Answer 4:")
    
def minimum(Array, starting, ending):

    min_index = starting  
    min_value = Array[starting]  

    for i in range(starting, ending + 1):
        if Array[i] < min_value:
            min_value = Array[i]
            min_index = i

    return min_index

Array = [3, 4, 7, 8, 0, 1, 23, -2, -5]
result = minimum(Array, 4, 7)
print(result)  

#Problem 4
print("Answer 4:")

def Sort4(Array):
    for i in range(len(Array)):
        mini = i
        
        for j in range(i,len(Array)):
            if Array[mini] > Array[j]:
                mini = j
                
        temp = Array[i]
        Array[i] = Array[mini]
        Array[mini] = temp
        
    return Array

sortedarray = Sort4(Array)
print(sortedarray)


#problem 5

print("Problem 5:")

def StringReverse(s, starting, ending):
   
    new = s[starting:ending + 1]

    resultstr = new[::-1]

    return resultstr


s = "University of Engineering and Technology Lahore"
print(StringReverse(s, 14, 24))


#Problem 6

print("Problem 6:")

#using Iterative method
def SumIterative(number):
    sum=0
    
    while number>0:
        digit = number%10
        sum+= digit
        number = int(number/10)
        
    return sum

result = SumIterative(1524)
print(result)

#using RECURSIVE method

def SumRecursive(number):
    
    if(number < 10):
        return number
    else:
        digit = number%10
        number = int(number/10)
        return digit+ SumRecursive(number)
    
result = SumRecursive(1524)
print(result)


#Problem 7

print("Problem 7:")

print("Row Wise:")
A = [[1,2,3],[4,5,6],[7,8,9]]

def RowWiseSum(Mat):
    rowarr = []
    for i in range(3):
        sum=0
        for j in range(3):
            sum+= A[i][j]
        rowarr.append(sum)
    return rowarr
          
resullt = RowWiseSum(A)
for i in range(len(resullt)):
    print(resullt[i])

print("Column Wise:")

def ColumnWiseSum(Mat):
    colarr = []
    for i in range(3):
        sum=0
        for j in range(3):
            sum+= A[j][i]
        colarr.append(sum)
    return colarr
          
resullt = ColumnWiseSum(A)
for i in range(len(resullt)):
    print(resullt[i],end=" ")


#problem 8
print()
print("Problem 8")


def SortedMerge(Arr1, Arr2):
    combinearr = Arr1 + Arr2
    for i in range(len(combinearr)):
        mini = i
        
        for j in range(i,len(combinearr)):
            if combinearr[mini] > combinearr[j]:
                mini = j
                
        temp = combinearr[i]
        combinearr[i] = combinearr[mini]
        combinearr[mini] = temp
        
    return combinearr


print(SortedMerge(Array,arr))

#problem 9
print()
print("Problem 9")

def PalindromRecursive(str):
    if(len(str)<=1):
        return True
    elif str[0]!=str[-1]:
        return False
    else:
        return PalindromRecursive(str[1:-1])


result = PalindromRecursive("ata")
if result:
    print("It is Palindrome")
else:
    print("Not Palindrome")
    
    
#problem 10
print("Problem 10:")

Arr = [10, -1, 9, 20, -3, -8, 22, 9, 7]

def Sort10(Arr):
  Arr.sort()
  return Arr

print(Sort10(Arr))




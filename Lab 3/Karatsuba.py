import sys
import time


def multiply(num1, num2, base):
    sumArray = []
    additionTens = 1

    for i in range(len(num1) - 1, -1, -1):
        carry = 0
        multiplyTens = 1
        sum1 = 0
        for j in range(len(num2) - 1, -1, -1):
            num = int(num1[i]) * int(num2[j]) + carry
            sum1 = sum1 + (multiplyTens * (int(num) % base))
            carry = int(num) // base
            multiplyTens = multiplyTens * 10
        sum1 = sum1 + (carry * multiplyTens)
        sum1 = sum1 * additionTens
        additionTens = additionTens * 10
        sumArray.append(str(sum1))

        maxLength = max(len(num) for num in sumArray)
        sumArray = [num.zfill(maxLength) for num in sumArray]

    answer = ""

    for i in range(len(sumArray)):
        print(sumArray[i])

    print("--------------------")
    carry = 0
    for i in range(maxLength - 1, -1, -1):
        sum2 = 0
        for num in sumArray:
            sum2 += int(num[i])
        sum2 += carry
        carry = sum2 // base
        answer = str((sum2 % base)) + answer
    if carry > 0:
        answer = str(carry) + answer

    return answer

def Multiply_integer(num1, num2):


    sumArray = []
    additionTens = 1

    for i in range(len(str(num1)) - 1, -1, -1):
        carry = 0
        multiplyTens = 1
        sum1 = 0
        num3 = num2
        for j in range(len(str(num2)) - 1, -1, -1):

            num = (num1 % 10) * (num3 % 10) + carry
            num3 = num3 // 10
            sum1 = sum1 + (multiplyTens * (int(num) % 10))
            carry = num // 10
            multiplyTens = multiplyTens * 10
        sum1 = sum1 + (carry * multiplyTens)
        sum1 = sum1 * additionTens
        additionTens = additionTens * 10
        num1 = num1 // 10
        sumArray.append(str(sum1))

        maxLength = max(len(num) for num in sumArray)
        sumArray = [num.zfill(maxLength) for num in sumArray]

    answer = ""

    carry = 0
    for i in range(maxLength - 1, -1, -1):
        sum2 = 0

        for num in sumArray:
            sum2 += int(num[i])
        sum2 += carry
        carry = sum2 // 10
        answer = str((sum2 % 10)) + answer
    if carry > 0:
        answer = carry + answer

    return answer


def Multiply_string(num1, num2):

    sumArray = []
    additionTens = 1

    for i in range(len(num1) - 1, -1, -1):
        carry = 0
        multiplyTens = 1
        sum1 = 0
        for j in range(len(num2) - 1, -1, -1):
            num = int(num1[i]) * int(num2[j]) + carry
            sum1 = sum1 + (multiplyTens * (int(num) % 10))
            carry = int(num) // 10
            multiplyTens = multiplyTens * 10
        sum1 = sum1 + (carry * multiplyTens)
        sum1 = sum1 * additionTens
        additionTens = additionTens * 10
        sumArray.append(str(sum1))

        maxLength = max(len(num) for num in sumArray)
        sumArray = [num.zfill(maxLength) for num in sumArray]

    answer = ""

    carry = 0
    for i in range(maxLength - 1, -1, -1):

        sum2 = 0
        for num in sumArray:
            sum2 = sum2 + int(num[i])

        sum2 = sum2 + carry
        carry = sum2 // 10
        answer = str((sum2 % 10)) + answer
    if carry > 0:
        answer = str(carry) + answer

    return answer

def Visualize_Karatsuba(num1, num2):
    print(num1)
    print(num2)
    print("--------------------")
    sumArray = []
    additionTens = 1

    for i in range(len(num1) - 1, -1, -1):
        carry = 0
        multiplyTens = 1
        sum1 = 0
        for j in range(len(num2) - 1, -1, -1):
            num = int(num1[i]) * int(num2[j]) + carry
            sum1 = sum1 + (multiplyTens * (int(num) % 10))
            carry = int(num) // 10
            multiplyTens = multiplyTens * 10
        sum1 = sum1 + (carry * multiplyTens)
        sum1 = sum1 * additionTens
        additionTens = additionTens * 10
        sumArray.append(str(sum1))

        maxLength = max(len(num) for num in sumArray)
        sumArray = [num.zfill(maxLength) for num in sumArray]

    answer = ""

    for i in range(len(sumArray)):
        print(sumArray[i])

    print("--------------------")
    carry = 0
    for i in range(maxLength - 1, -1, -1):
        sum2 = 0
        for num in sumArray:
            sum2 += int(num[i])
        sum2 += carry
        carry = sum2 // 10
        answer = str((sum2 % 10)) + answer
    if carry > 0:
        answer = str(carry) + answer

    return answer

def compareSize(num1, num2):
    if len(str(num1)) >= len(str(num2)):
        return  len(str(num1))
    else:
        return len(str(num2))
def Multiply_Recursive(num1, num2):
    if int(num1) < 10 or int(num2) < 10:
        return int(num1) * int(num2)

    # Calculate the number of digits in x and y
    size = compareSize(num1,num2)
    sizeHalf = size // 2

    # Split x and y into a, b, c, and d
    a = str(int(num1) // 10 ** sizeHalf)
    b = str(int(num1) % 10 ** sizeHalf)
    c = str(int(num2) // 10 ** sizeHalf)
    d = str(int(num2) % 10 ** sizeHalf)

    # Recursive calls
    ac = Multiply_Recursive(a, c)
    ad = Multiply_Recursive(a, d)
    bc = Multiply_Recursive(b, c)
    bd = Multiply_Recursive(b, d)

    # Combine the results using the Karatsuba formula
    result = (10 ** (2 * sizeHalf) * ac) + (10 ** sizeHalf * (ad + bc)) + bd


    return result


def Karatsuba_Recursive(num1, num2):
    if int(num1) < 10 or int(num2) < 10:
        return int(num1) * int(num2)

    # Calculate the number of digits in x and y
    size = compareSize(num1,num2)
    sizeHalf = size // 2

    # Split x and y into a, b, c, and d
    a = str(int(num1) // 10 ** sizeHalf)
    b = str(int(num1) % 10 ** sizeHalf)
    c = str(int(num2) // 10 ** sizeHalf)
    d = str(int(num2) % 10 ** sizeHalf)

    e = int(a) + int(b)
    f = int(c) + int(d)
    # Recursive calls
    ac = Karatsuba_Recursive(a, c)
    abcd = Karatsuba_Recursive(e, f)
    bd = Karatsuba_Recursive(b, d)

    # Combine the results using the Karatsuba formula
    result = (10 ** (2 * sizeHalf) * ac) + (10 ** sizeHalf * (abcd - ac - bd)) + bd

    return result

def Multiply2(num1, num2):
    sumArray = []
    additionTens = 1

    for i in range(len(num1) - 1, -1, -1):
        carry = 0
        multiplyTens = 1
        sum1 = 0
        for j in range(len(num2) - 1, -1, -1):
            num = int(num1[i]) * int(num2[j]) + carry
            sum1 = sum1 + (multiplyTens * (int(num) % 2))
            carry = int(num) // 2
            multiplyTens = multiplyTens * 10
        sum1 = sum1 + (carry * multiplyTens)
        sum1 = sum1 * additionTens
        additionTens = additionTens * 10
        sumArray.append(str(sum1))

        maxLength = max(len(num) for num in sumArray)
        sumArray = [num.zfill(maxLength) for num in sumArray]

    answer = ""

    for i in range(len(sumArray)):
        print(sumArray[i])

    print("--------------------")
    carry = 0
    for i in range(maxLength - 1, -1, -1):
        sum2 = 0
        for num in sumArray:
            sum2 += int(num[i])
        sum2 += carry
        carry = sum2 // 2
        answer = str((sum2 % 2)) + answer
    if carry > 0:
        answer = str(carry) + answer

    return answer


def Multiply16(num1, num2):
    sumArray = []
    additionTens = ''

    for i in range(len(num1) - 1, -1, -1):
        carry = '0'

        sum1 = ''
        for j in range(len(num2) - 1, -1, -1):
            num = int(hexaNumbers(num1[i])) * int(hexaNumbers(num2[j])) + int(hexaNumbers(carry))
            sum1 =  NumbersHexa(int(num) % 16) + sum1
            carry = NumbersHexa(int(num) // 16)

        sum1 = carry + sum1
        sum1 = sum1 + additionTens
        additionTens = additionTens + '0'
        sumArray.append(str(sum1))

        maxLength = max(len(num) for num in sumArray)
        sumArray = [num.zfill(maxLength) for num in sumArray]

    answer = ""

    print("--------------------")
    carry = '0'
    for i in range(maxLength - 1, -1, -1):
        sum2 = 0
        for num in sumArray:
            sum2 += hexaNumbers((num[i]))
        sum2 += hexaNumbers(carry)
        carry = NumbersHexa(sum2 // 16)
        answer = NumbersHexa((sum2 % 16)) + answer
    if hexaNumbers(carry) > 0:
        answer = NumbersHexa(carry) + answer

    return answer

def hexaNumbers(num):
    if num == '1':
        return 1
    elif num == '2':
        return 2
    elif num == '3':
        return 3
    elif num == '4':
        return 4
    elif num == '5':
        return 5
    elif num == '6':
        return 6
    elif num == '7':
        return 7
    elif num == '8':
        return 8
    elif num == '9':
        return 9
    elif num == 'A':
        return 10
    elif num == 'B':
        return 11
    elif num == 'C':
        return 12
    elif num == 'D':
        return 13
    elif num == 'E':
        return 14
    elif num == 'F':
        return 15
    elif num == '0':
        return 0

def NumbersHexa(num):
    if num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    elif num == 0:
        return '0'




def validation(num, base):
    check = True
    for i in range(len(num)):
        if int(hexaNumbers(num[i])) >= base:
            check = False
            break

    if check == False:
        print("Enter a valid Number for the Base you chose")
        sys.exit()
    return check


base = input("Enter base System: ")
num1 = input("Enter 1st Number: ")
validation(num1, int(base))
num2 = input("Enter 2nd Number: ")
validation(num2, int(base))


print("--------------------")

#start = time.time()
#print(Multiply_integer(int(num2), int(num1)))
#end = time.time()
#t = end - start
#print(t)
#print()

#start = time.time()
#print(Multiply_string(num2, num1))
#end = time.time()
#t = end - start
#print(t)
#print()

#start = time.time()
#print(Visualize_Karatsuba(num2, num1))
#end = time.time()
#t = end - start
#print(t)
#print()

#start = time.time()
#print(Multiply_Recursive(num1, num2))
#end = time.time()
#t = end - start
#print(t)
#print()

#start = time.time()
#print(Karatsuba_Recursive(num1, num2))
#end = time.time()
#t = end - start
#print(t)
#print()

#start = time.time()
#print(Multiply2(num1, num2))
#end = time.time()
#t = end - start
#print(t)
#print()


#start = time.time()
#print(Multiply2(num1, num2))
#end = time.time()
#t = end - start
#print(t)
#print()


start = time.time()
print(Multiply16(num1, num2))
end = time.time()
t = end - start
print(t)
print()



print("--------------------")



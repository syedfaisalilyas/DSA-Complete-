def multiplication(a, b,isInt):

    if isInt:
        str_a = str(a)
        str_b = str(b)
    else:
        str_a=a
        str_b=b

    len_a = len(str_a)
    len_b = len(str_b)
        
    partial_products = [0] * (len_a + len_b)


    for i in range(len_a -1,-1,-1):
       for j in range(len_b - 1,-1,-1):
            product = int(str_a[i]) * int(str_b[j])
            partial_products[i + j + 1] += product

       
    carry = 0
    for i in range(len(partial_products) - 1, -1, -1):
       total = partial_products[i] + carry
       partial_products[i] = total % 10
       carry = total // 10

    result_str = ''.join(map(str, partial_products))
           
    result_str = result_str.lstrip('0')
    return result_str
   
    

print("MULTIPLICATION OF INTEGERS:",multiplication(12,3,True))
print("MULTIPLICATION OF STRING:",multiplication("12","12",False))
   
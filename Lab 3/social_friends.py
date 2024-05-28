

def another(array):
    arr=[]
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i][1]>=array[j][0] and array[i][0]<=array[j][1]:
                arr.append((i+1,j+1))
          
    return arr    

def friendSlower(array):
    arr=[]
    for i in range(0,len(array)-1):
        # for j in range(i+1,len(array)):
            if array[i][1]>=array[i+1][0] and array[i][0]<=array[i+1][1]:
                arr.append((i+1,i+2))
          
    return arr    
    
     
        
array=[[1,4],[2,5],[7,9],[9,10],[6,10]]
result=another(array)
print(result)



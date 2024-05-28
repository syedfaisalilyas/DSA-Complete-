


def friendSlower(array2d):
    friendsArray = []
    for i in range(len(array2d)):
        for j in range(i+1,len(array2d)):
            if array2d[i][1] >= array2d[j][0] and array2d[j][1] >= array2d[i][0]:
                tpl = (i+1,j+1)

                friendsArray.append(tpl)

    return friendsArray





users = input("Enter number of Users: ")
array2d = [[0 for i in range(int(2))] for i in range(int(users))]
for i in range(int(users)):
    enter = input("Enter entry time of student " + str(i + 1) +  ": " )
    leave = input("Enter leave time of student " + str(i + 1) + ": " )
    array2d[i][0] = int(enter)
    array2d[i][1] = int(leave)

print(friendSlower(array2d))

'''
def recursiveFriendSlower(array2d, i, j, friendsArray):
    # Base case: If we have reached the end of the array, return the result.
    if i == len(array2d) - 1 and j == len(array2d):
        return friendsArray

    # Check if the conditions are met for the current pair (i, j).
    if array2d[i][1] >= array2d[j][0] and array2d[j][1] >= array2d[i][0]:
        friendsArray.append((i + 1, j + 1))  # Adjust indices by 1 to match the original function.

    # Increment indices to move to the next pair.
    if j < len(array2d) - 1:
        return recursiveFriendSlower(array2d, i, j + 1, friendsArray)
    elif i < len(array2d) - 2:
        return recursiveFriendSlower(array2d, i + 1, i + 2, friendsArray)
    else:
        # We have reached the end of the array without finding more pairs.
        return friendsArray

def friendSlower(array2d):
    return recursiveFriendSlower(array2d, 0, 1, [])

# Example usage:
users = 4  # Replace this with the desired number of users
array2d = [[0 for _ in range(users)] for _ in range(users)]
# Fill array2d with your data
result = friendSlower(array2d)
print(result)

'''
def maxDistance(array, k):
   
   if sum(array) <= k:
       return sum(array)
   else:
       return max(maxDistance(array[1:], k), maxDistance(array[:-1], k))

print("max sum is:")
print(maxDistance([1,3,5,7,12] , 15))


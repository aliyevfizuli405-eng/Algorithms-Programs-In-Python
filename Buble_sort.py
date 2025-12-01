Fizuli=[2,4,5,1,6,9]

#sorting elements algorithm for every array
def Buble_sort(arr):
   b=len(arr)
   for i in range(b-1):
      for j in range(b-1):
       if arr[j]>arr[j+1]:
           arr[j],arr[j+1]=arr[j+1],arr[j]
   print(arr)
Buble_sort(Fizuli)

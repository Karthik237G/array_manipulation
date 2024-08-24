#sorting a 1dimn array 
import numpy as np
arr=np.array([3,2,0,1])
print(np.sort(arr))

#converting the array into a list and sorting
import array as arr
arra=arr.array('i',[10,15,2,3,8,9])
sortarr=arra.tolist()
sortarr.sort()
sortarr=arr.array('i',sortarr)
print(sortarr)

#sorting in desending order
array=[10,40,50,1,3,5]
array.sort(reverse=True)
print(array)

#sorting a 3d array
import numpy as np
arr=np.array([[3,2,1],[4,5,6],[9,8,6]])
sortarr=np.sort(arr,axis=-1)
print(sortarr)

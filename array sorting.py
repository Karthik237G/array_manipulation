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

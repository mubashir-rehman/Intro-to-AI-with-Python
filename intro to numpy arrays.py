import numpy as np

#Q1
# list = []
# print("enter numbers please")
# for x in range(0,5):
#     list.append(int(input()))
# list=np.array(list)
# indexes=np.argwhere(list==0)
# print(indexes)

#Q2
# matrixX=np.diag([1,2,3,4,5])
# print(matrixX)

#Q3
array1=np.arange(16).reshape(4,4)
print("Q3\n",array1)
newArray=array1[:,[-1,2,1,0]]
print(newArray)

#Q4
array1[0,:]=1
print("Q4\n",array1)

#Q5
array1[:,[-1]]=0
print("Q5\n",array1)

#Q6
#np.dtype(array1,'int')
np.savetxt('data.txt', array1, fmt='%d')
array2 = np.loadtxt('data.txt', dtype=int)
print("Q6\n",array2)

#Q7
x=np.arange(4).reshape(2,2)
# np.append()
# np.reshape(x,(4,4))
y=np.arange(16).reshape(4,4)
z=x[:,:,np.newaxis,np.newaxis]*y
print("Q7\n",z)

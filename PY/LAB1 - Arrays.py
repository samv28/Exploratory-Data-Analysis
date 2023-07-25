import numpy as np
my_list = [1,2,3]
print(my_list)
print(np.array(my_list))


#aARRAY
my__matrix = [[1,2,3],[4,5,6],[5,6,7]]
print(my__matrix)
np.array(my__matrix)
print(np.array(my__matrix))

#aARANGE
print(np.arange(0,10))

#a(start,end,step)
print(np.arange(0,11,2))

#afirst 50 odd numbers
print(np.arange(1,102,2))


#azeros and one
print(np.zeros(3))
print(np.zeros((6,9)))
print(np.ones(4))
print(np.ones((4,5)))


#alinspace
print(np.linspace(0,10,3))
print(np.linspace(0,10,50))
print(np.linspace(0,100,25))

#aeye
print(np.eye(7))

#arandom
print(np.random.rand(2))
print(np.random.rand(5))
print(np.random.rand(9,6))

#arandn
print(np.random.randn(2))
print(np.random.randn(5,5))

#arandint
print(np.random.randint(1,100))
print(np.random.randint(1,100,10))

#aarray attributes and methods
arr=np.arange(25)
ranarr=np.random.randint(0,50,10)
print(arr)
print(ranarr)

#areshape
print(arr.reshape(5,5))

#amax min argmax argmin
print(ranarr)
print(ranarr.max())
print(ranarr.argmax())
print(ranarr.min())
print(ranarr.argmin())

#ashape
print(arr.shape)
print(arr.reshape(1,25))
print(arr.reshape(1,25).shape)
print(arr.reshape(25,1))
print(arr.reshape(25,1).shape)

#adtype data type
print(arr.dtype)

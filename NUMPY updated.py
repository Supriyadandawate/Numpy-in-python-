#!/usr/bin/env python
# coding: utf-8

# #### Importing the NumPy libarary
# 

# In[1]:


import numpy as np


# In[2]:


list1=[1,2,3,4,5]
print(list1)
type(list1)


# In[3]:


# converting list to Numpy array
arr = np.array(list1)
print(arr)
type(arr)


# In[4]:


listarray = np.array([[1,2,3],[5,5,8],[4,6,9]])
print(listarray)
listarray.size # Number of element in an array


# In[5]:


listarray.dtype #checking the data type of the values in the array


# In[6]:


arr = np.array([1,2,3,4,5])
print("1D Array:")
print(arr)
arr.shape


# #### Creating a 2D array(Matrix)

# In[7]:


arr_2d = np.array([[1,2,3],[4,5,6]])
print("2D Array:")
print(arr_2d)
arr_2d.shape # the Number of Rows and columns an array


# In[8]:


a = np.array([[1,2,3,2],[2,5,82,7],[5,8,7,5]], dtype=np.int32)
print(a)
a.shape


# #### Creating a 3D array 

# In[9]:


# Create a 3D array with dimensions(2,3,4)
# 2 matrices(Layers),3 rows , and 4 columns 
arr_3d = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]], 
                   [[13,14,15,16],[17,18,19,20],[21,22,23,24]]],
                    dtype=float)
print(arr_3d)
print("Shape:",arr_3d.shape)


# In[10]:


arr_3d.ndim #Number of Dimensions


# In[11]:


zeros_3d = np.zeros((2,3,4))
zeros_3d


# In[12]:


ones_3d = np.ones((2,3,4))
ones_3d


# In[13]:


random_3d = np.random.random((2,3,4))
random_3d


# #### Creating a Zero-filled array 

# In[14]:


zeros = np.zeros((2,3)) #2x3 array of zeros
print("Zero-filled Array")
print(zeros)


# In[15]:


zeros.dtype


# In[16]:


zeros.shape


# #### Creating an array of ones 

# In[17]:


ones = np.ones((3,3)) #3x3 array of ones
print("Ones-filled Array:")
print(ones)


# #### Creating  an array of a Particular value 

# In[18]:


array_of_threes =np.full((5,4),3) #5x4 array filled with 3 
print(array_of_threes)


# #### Indentify matrix

# In[19]:


# Create a 45x45 indentity matrix 

ide = np.identity(45)
# the diagonal elements are set to 1 , with all other element being 0.

print(ide)
ide.shape


# In[21]:


ide.size


# In[23]:


ide.dtype


# In[24]:


# Create an 8x8 identity matrix
eye_matrix = np.eye(8)
# you can specify the number of row and columns or shift the diagonal.
print(eye_matrix)


# #### Create a numpy array with random values

# In[29]:


# Create a 3x4 array with random float values between 0 and 1 
b=np.random.random((3,4))
b


# #### Create a random integer values array within a specific range

# In[ ]:





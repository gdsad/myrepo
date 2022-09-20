import numpy as np

a = np.arange(6)
a
type(a)
a.shape
a.dtype

# aa = a[np.newaxis, :]
aa = a[:, np.newaxis]
aa
type(aa)
aa.shape
aa.dtype

# ----
x = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float64)
x
type(x)
x.dtype
x.shape
x[1]
x[:,0]


#  ------------------------
w = np.linspace(0,10,25)
w
w.shape
len(w)
w.dim()
w2 = w[w<5]

w3 = 22
w4 = 23

w = 5
q = 6
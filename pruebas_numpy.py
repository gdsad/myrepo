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


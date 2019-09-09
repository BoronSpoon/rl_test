import numpy as np
a = np.array([[1,0],[1,1]])
b = np.array([[0,0],[1,1]])
c = np.array([a,b])
mask1 = np.array([[1,0],[0,1]])
mask2 = np.array([[0,1],[1,0]])
print(np.apply_over_axes(np.sum,c*mask1,[1,2])[:,0,0], np.apply_over_axes(np.sum,c*mask2,[1,2]))

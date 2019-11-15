from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import cv2
import matplotlib

#fileName = '/delapan/20190508_230410.jpg'
fileName = '/rgbobj.bmp'

img = matplotlib.pyplot.imread("/content/drive/My Drive/datafont"+fileName, format=None)

fig, ax = plt.subplots()
im = ax.imshow(img)
ax.axis('off')
plt.show()


[M,N,c] = img.shape

imgRed = np.zeros((M,N), dtype=np.uint8)
imgGreen = np.zeros((M,N), dtype=np.uint8)
imgBlue = np.zeros((M,N), dtype=np.uint8)

for i in range(M):
  for j in range(N):
    valR = img[i,j,0]
    valG = img[i,j,1]
    valB = img[i,j,2]
    imgRed[i,j]   = valR
    imgGreen[i,j] = valG
    imgBlue[i,j]  = valB
    

fig = plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(imgRed,cmap=cm.gray)
plt.subplot(1, 3, 2)
plt.imshow(imgGreen,cmap=cm.gray)
plt.subplot(1, 3, 3)
plt.imshow(imgBlue,cmap=cm.gray)


X1 = np.arange(0, M, 1)
Y1 = np.arange(0, N, 1)
X2, Y2 = np.meshgrid(X1, Y1)

fig = plt.figure(figsize=(15, 5))

elevVal = 30
azimVal = None

# Plot the surface.
ax = fig.add_subplot(1, 3, 1, projection='3d')
elev = elevVal  
azim = azimVal 
ax.view_init(elev, azim)
surf = ax.plot_surface(X2, Y2, imgRed, cmap=cm.Reds_r,
                       linewidth=0, antialiased=False)

ax = fig.add_subplot(1, 3, 2, projection='3d')
elev = elevVal  
azim = azimVal 
ax.view_init(elev, azim)
surf = ax.plot_surface(X2, Y2, imgGreen, cmap=cm.Greens_r,
                       linewidth=0, antialiased=False)

ax = fig.add_subplot(1, 3, 3, projection='3d')
elev = elevVal  
azim = azimVal 
ax.view_init(elev, azim)
surf = ax.plot_surface(X2, Y2, imgBlue, cmap=cm.Blues_r,
                       linewidth=0, antialiased=False)



plt.show()

import numpy as np
import matplotlib.pyplot as plt

from skimage.transform import iradon
from matplotlib.font_manager import FontProperties
fname = '/home/pai4090/anaconda3/lib/python3.11/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf'
myfont = FontProperties(fname=fname)



filename = '/home/pai4090/断层成像/5/ParallelBeam_DetectorFlatData.raw'
fid = open(filename, 'rb')
A = np.fromfile(fid, dtype=np.ushort).reshape(1, 512)

filename = '/home/pai4090/断层成像/5/ParallelBeam_ProjectionDara.raw'
fid = open(filename, 'rb')
B = np.fromfile(fid, dtype=np.ushort).reshape(360,512)

A = A.T
B = B.T

plt.figure(1)
plt.imshow(B, cmap='gray')
plt.title('data')
plt.show()  
# plt.figure()
# plt.imshow(A, cmap='gray')
# plt.title('data')
# plt.show()  

I_bright_mean = np.mean(A)

# 平场校正
I_sample_dark = B
I_bright_dark = np.tile(A, (1, 360))

I = (I_sample_dark / I_bright_dark) * I_bright_mean
I_noflat = I_sample_dark.copy()

# 坏点补偿
I_nobad = I.copy()
I[99, :] = (I[97, :] * 0.3 + I[98, :] * 0.7 + I[100, :] * 0.7 + I[101, :] * 0.3) * 0.5
I[219, :] = (I[217, :] * 0.3 + I[218, :] * 0.7 + I[220, :] * 0.7 + I[221, :] * 0.3) * 0.5

I_noflat[99, :] = (I_noflat[97, :] * 0.3 + I_noflat[98, :] * 0.7 + I_noflat[100, :] * 0.7 + I_noflat[101, :] * 0.3) * 0.5
I_noflat[219, :] = (I_noflat[217, :] * 0.3 + I_noflat[218, :] * 0.7 + I_noflat[220, :] * 0.7 + I_noflat[221, :] * 0.3) * 0.5

# 对数操作
I_nolog = I.copy()
I0 = np.max(np.max(I))
I = np.log(I / I0)

I0 = np.max(np.max(I_noflat))
I_noflat = np.log(I_noflat / I0)

I0 = np.max(np.max(I_nobad))
I_nobad = np.log(I_nobad / I0)

# 反投影重建
data = iradon(I, theta=list(range(360)), filter_name='ramp', interpolation='linear')
noflat = iradon(I_noflat, theta=list(range(360)), filter_name='ramp', interpolation='linear')
nobad = iradon(I_nobad, theta=list(range(360)), filter_name='ramp', interpolation='linear')
nolog = iradon(I_nolog, theta=list(range(360)), filter_name='ramp', interpolation='linear')

#显示结果
plt.figure(2)
plt.imshow(data, cmap='gray')
plt.title('重建结果',fontproperties=myfont)
plt.figure(3)
plt.imshow(noflat, cmap='gray')
plt.title('无平场校正',fontproperties=myfont)
plt.figure(4)
plt.imshow(nobad, cmap='gray')
plt.title('无坏点补偿',fontproperties=myfont)
plt.figure(5)
plt.imshow(nolog, cmap='gray')
plt.title('无对数操作',fontproperties=myfont)
plt.show()
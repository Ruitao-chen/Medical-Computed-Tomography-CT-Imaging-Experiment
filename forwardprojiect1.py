
import numpy as np
import matplotlib.pyplot as plt
import phantominator
from phantominator import shepp_logan



def forward_projection(theta, N, N_d):
    point = np.array([1, 0.005, 0.005, 0.5, 0, 0])
    theta_num = len(theta)
    P = np.zeros((N_d, theta_num))
    rho = point[0]
    ae = 0.5 * N * point[1]
    be = 0.5 * N * point[2]
    xe = 0.5 * N * point[3]
    ye = 0.5 * N * point[4]
    alpha = point[5]
    alpha = alpha * np.pi / 180
    theta = np.array(theta) * np.pi / 180
    TT = np.arange(-(N_d - 1) / 2, (N_d - 1) / 2 + 1)

    for k1 in range(theta_num):
        P_theta = np.zeros(N_d)
        for k2 in range(1):  # 修改此处
            a = (ae * np.cos(theta[k1] - alpha)) ** 2 + (be * np.sin(theta[k1] - alpha)) ** 2
            temp = a - (TT - xe * np.cos(theta[k1]) - ye * np.sin(theta[k1])) ** 2
            ind = temp > 0
            P_theta[ind] += rho * (2 * ae * be * np.sqrt(temp[ind])) / a
        P[:, k1] = P_theta

    return P

N = 256
theta = np.arange(0, 360, 1)
I = shepp_logan(N)  # 实现phantom函数生成头部图像的代码
N_d = int(2 * np.ceil(np.linalg.norm(np.array(I.shape) - np.floor((np.array(I.shape) - 1) / 2) - 1)) + 3)
P = forward_projection(theta, N, N_d)

plt.figure()
plt.imshow(P, cmap='gray')
plt.colorbar()
plt.title('point 360° Parallel Beam Projection')
plt.show()



theta1 = np.arange(0, 45, 1)
N_d = 2 * np.ceil(np.linalg.norm(np.array(I.shape) - np.floor((np.array(I.shape) - 1) / 2) - 1)) + 3
P1 = forward_projection(theta1, N, int(N_d))

plt.figure()
plt.imshow(P1, cmap='viridis')
plt.colorbar()
plt.title('point 45° Parallel Beam Projection')
plt.show()


theta2 = np.arange(0, 300, 1)
N_d = 2 * np.ceil(np.linalg.norm(np.array(I.shape) - np.floor((np.array(I.shape) - 1) / 2) - 1)) + 3
P2 = forward_projection(theta2, N, int(N_d))

plt.figure()
plt.imshow(P2, cmap='hot')
plt.colorbar()
plt.title('point 300° Parallel Beam Projection')
plt.show()
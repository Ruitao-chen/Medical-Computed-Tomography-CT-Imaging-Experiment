import numpy as np
import matplotlib.pyplot as plt
import phantominator
from phantominator import shepp_logan


def forward_projection(theta_proj, N, N_d):
    shep = np.array([[1,       0.69,      0.92,         0,         0,            0],      
                     [-0.8,      0.6624,    0.8740,         0,   -0.0184,           0],         
                     [-0.2,      0.1100,    0.3100,      0.22,          0,        -18],   
                     [-0.2,      0.1600,    0.4100,      -0.22,      0,            18],        
                     [0.1,       0.2100,     0.2500,          0,      0.35,         0],       
                     [0.1,       0.0460,     0.0460,          0,       0.1,         0],        
                     [0.1,       0.0460,     0.0460,          0,       0.1,         0],       
                     [0.1,       0.0460,     0.0230,      -0.08,    -0.605,         0],       
                     [0.1,       0.0230,     0.0230,          0,     -0.606,         0],       
                     [0.1,       0.0230,     0.0460,       0.06,     -0.605,         0]])

    theta_num = len(theta_proj)
    P = np.zeros((int(N_d), theta_num))
    rho = shep[:, 0]
    ae = 0.5 * N * shep[:, 1]
    be = 0.5 * N * shep[:, 2]
    xe = 0.5 * N * shep[:, 3]
    ye = 0.5 * N * shep[:, 4]
    alpha = shep[:, 5]
    alpha = alpha * np.pi / 180
    theta_proj = theta_proj * np.pi / 180
    TT = np.arange(-(N_d - 1) / 2, (N_d - 1) / 2 + 1)

    for k1 in range(theta_num):
        P_theta = np.zeros(int(N_d))
        for k2 in range(len(xe)):
            a = (ae[k2] * np.cos(theta_proj[k1] - alpha[k2]))**2 + (be[k2] * np.sin(theta_proj[k1] - alpha[k2]))**2
            temp = a - (TT - xe[k2] * np.cos(theta_proj[k1]) - ye[k2] * np.sin(theta_proj[k1]))**2
            ind = temp > 0
            P_theta[ind] += rho[k2] * (2 * ae[k2] * be[k2] * np.sqrt(temp[ind])) / a
        P[:, k1] = P_theta

    P_min = np.min(P)
    P_max = np.max(P)
    P = (P - P_min) / (P_max - P_min)
    return P

N = 256
theta = np.arange(0, 180, 1)
I = shepp_logan(N) # Replace with your phantom generation code

N_d = 2 * np.ceil(np.linalg.norm(np.array(I.shape) - np.floor((np.array(I.shape) - 1) / 2) - 1)) + 3
P = forward_projection(theta, N, int(N_d))


plt.figure()
plt.imshow(I, cmap='gray')
plt.title('256x256 Head Phantom')
plt.figure()
plt.imshow(P, cmap='gray')
plt.colorbar()
plt.title('180° Parallel Beam Projection')


theta1 = np.arange(0, 45, 1)
N_d = 2 * np.ceil(np.linalg.norm(np.array(I.shape) - np.floor((np.array(I.shape) - 1) / 2) - 1)) + 3
P1 = forward_projection(theta1, N, int(N_d))

plt.figure()
plt.imshow(P1, cmap='viridis')
plt.colorbar()
plt.title('45° Parallel Beam Projection')
plt.show()


theta2 = np.arange(0, 300, 1)
N_d = 2 * np.ceil(np.linalg.norm(np.array(I.shape) - np.floor((np.array(I.shape) - 1) / 2) - 1)) + 3
P2 = forward_projection(theta2, N, int(N_d))

plt.figure()
plt.imshow(P2, cmap='viridis')
plt.colorbar()
plt.title('300° Parallel Beam Projection')
plt.show()
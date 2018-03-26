import matplotlib.pyplot as plt
import scipy.io as scio
import os
import glob


for mat_file in glob.glob('ImsAndSegs/*.mat'):
    img = scio.loadmat(mat_file)
    plt.figure(mat_file.split(os.sep)[1].replace('.mat',''))
    plt.subplot(2,2,1)
    plt.imshow(img['Im'])
    plt.subplot(2,2,2)
    plt.imshow(img['Seg1'])
    plt.subplot(2,2,3)
    plt.imshow(img['Seg2'])
    plt.subplot(2,2,4)
    plt.imshow(img['Seg3'])
    plt.show()

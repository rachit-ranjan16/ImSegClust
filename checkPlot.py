import scipy.io as scio
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import spectral as sp


pavia = {'rgb': scio.loadmat('PaviaRGB.mat')['PaviaRGB'],
         'color_map' : scio.loadmat('PaviaColorMap.mat')['PaviaColorMap'],
         'ground_truth' : scio.loadmat('PaviaGrTruth.mat')['PaviaGrTruth'],
         'ground_truth_mask' : scio.loadmat('PaviaGrTruthMask.mat')['PaviaGrTruthMask'],
         'hyperimage' : scio.loadmat('PaviaHyperIm.mat')['PaviaHyperIm'],
         'wavelengths' : scio.loadmat('PaviaWavelengths.mat')['PaviaWavelengths'],
        }
sanbar = {'rgb': scio.loadmat('SanBarRGB.mat')['SanBarRGB'],
          'wavelengths': scio.loadmat('SanBarWavelengths.mat')['WaveLengths'],
          'hyperimage': scio.loadmat('SanBarHyperIm.mat')['SanBarIm88x400'],
         }

plt.figure(100)
plt.title('Pavia RGB')
plt.imshow(pavia['rgb'])
plt.figure(101)
plt.title('Pavia ColorMap')
plt.imshow(pavia['color_map'])
plt.figure(102)
plt.title('Pavia Ground Truth')
plt.imshow(pavia['ground_truth'])
plt.figure(103)
plt.title('Pavia Ground Truth Mask')
plt.imshow(pavia['ground_truth_mask'])
plt.figure(104)
plt.title('Pavia Wavelengths')
plt.imshow(pavia['wavelengths'])
plt.show()

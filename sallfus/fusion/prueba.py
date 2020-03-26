from broveyCPU import fusion_images
import skimage.io

m = skimage.io.imread('D:/Users/Andres/Downloads/1024rgb.tif', plugin='tifffile')
p = skimage.io.imread('D:/Users/Andres/Downloads/1024pan.tif', plugin='tifffile')

res = fusion_images(m,p,'D:/Users/Andres/Documents/figLib',True)

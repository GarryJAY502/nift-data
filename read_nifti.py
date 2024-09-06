import matplotlib
from matplotlib import pylab as plt
import nibabel as nib
from nibabel import nifti1
from nibabel.viewers import OrthoSlicer3D

img_path='LYJ/10071200/flip_T2_ax_label1_2.nii.gz'
img=nib.load(img_path)
print(img)
#print(img.header['db_name'])  #显示header 当中db_name
#有些可能图片是四维的
width,height,queue=img.dataobj.shape
OrthoSlicer3D(img.dataobj).show()

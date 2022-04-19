import unittest
from PIL import Image
import numpy as np
from scipy.interpolate import interp2d

img = np.array(Image.open('unittests/test.tiff'))

corners = np.array([[40,40],
    [40,img.shape[1]-40],
    [img.shape[0]-40,40],
    [img.shape[0]-40,img.shape[1]-40]])
  

    
def macbeth_find(chart_corners,n_x,n_y):  
    #create normalized chart between 0-1
    xs = np.linspace(0,1,n_x,n_y)
    ys = np.linspace(0,1,n_y)
    xx,yy = np.meshgrid(xs,ys)
    grid = np.array([xx.flatten(),yy.flatten()]).T
    corners = np.array([[0,0],[0,1],[1,0],[1,1]])
    
    fx = interp2d(corners[:,0],corners[:,1],chart_corners[:,0],kind='linear' )
    fy = interp2d(corners[:,0],corners[:,1],chart_corners[:,1],kind='linear' )
   
    output_list =[]
    for i in range(grid.shape[0]):
          output_list.append((fx(grid[i,0],grid[i,1]),fy(grid[i,0],grid[i,1])))
    output_list = np.array(output_list,dtype=int).reshape(-1,2)
    return output_list

grid = macbeth_find(corners,22,32)

def sample_image(output_list,img):
 
    w = [img[output_list[i,0]-5:output_list[i,0]+5,
        output_list[i,1]-5:output_list[i,1]+5, :]
        for i in range(output_list.shape[0])]
    samples = np.mean(np.array(w).reshape(output_list.shape[0],100,3),axis=1,)
    return samples

class TestMacbethSampler(unittest.TestCase):
    def test_macbeth_sample(self):
        actual = np.unique(sample_image(grid,img), axis = 0).shape
        expected = np.unique(img.reshape(-1,3),axis=0).shape
        self.assertEqual(actual, expected)

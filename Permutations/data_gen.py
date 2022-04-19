


from Nuke_Scripts.RAW_encoder import kelvins
from importEXR.read import readEXR
from RGB_Sampling.chart_locater import sample_image, macbeth_find, wb_grid
import glob
import numpy as np
import pandas as pd

columns = ["input WB", "Red","Green", "Blue", 'output WB', "output Red", "output Green", "output Blue"]


def init_data():
    k= [str(i) for i in kelvins]
    wb_data =[]
    for i in k:
        print(i)
        subset = sorted(glob.glob('EXR_Data/' + i +'*.exr'))
        data =[readEXR(x) for x in subset]
        dataset= np.array([sample_image(macbeth_find((wb_grid).astype(int),22,32),e,) for e in data]).reshape(-1,3)

        wb_data.append([dataset,(float(i)-2000)/5000])
    return wb_data

def permute_data(arr):
    full_data = []
    for i in arr:
      a = i[0]
      b =  np.tile([i[1]],(a.shape[0],1))
      c =np.concatenate((b,a), axis=1)
      full_data.append(c)

    full_data = np.array(full_data).reshape(-1,4)
    joined = []
    for i in arr:
      a = np.tile(i[0],(len(arr),1))
      b =  np.tile([i[1]],(a.shape[0],1))
      c =np.concatenate((b,a), axis=1)
      d = np.concatenate((full_data,c),axis=1)
      joined.append(d)
    joined = np.array(joined).reshape(-1,8)
    df = pd.DataFrame(data= joined, columns= ["input WB",
        "Red","Green", "Blue", 'output WB', "output Red",
        "output Green", "output Blue"])
    return df
    
    

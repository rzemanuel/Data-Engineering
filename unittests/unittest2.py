import unittest
import pandas as pd
import numpy as np


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
    df = pd.DataFrame(data=joined, columns= ["input WB",
  "Red","Green", "Blue", 'output WB', "output Red",
   "output Green", "output Blue"])
    return df
   
sample_input_data = [
    [np.array([[1,0,0],
              [0,1,0],
              [0,0,1]]) , .5],
    [np.array([[1,2,0],
              [0,1,2],
              [5,0,1]]) , .2],
    [np.array([[1,2,8],
              [2,1,2],
              [5,-4,1]]) , .9],
    ]


class TestMacbethSampler(unittest.TestCase):
    def test_permute(self):
        actual = len(permute_data(sample_input_data))
        expected = len(sample_input_data)**2*(sample_input_data[0][0].shape[0])
        self.assertEqual(actual, expected)
import tensorflow as tf
import sqlite3
import pandas as pd

def sql2numpy():


    conn = sqlite3.connect('White_Balance.db')
    sql_query_X = pd.read_sql_query ('''
                              SELECT [input WB], Red, Green,Blue,[output WB] FROM WB_TABLE_SP5600
                               ''', conn)
    sql_query_Y = pd.read_sql_query ('''
                              SELECT [output Red], [output Green],[output Blue] FROM WB_TABLE_SP5600
                               ''', conn)
    X = pd.DataFrame(sql_query_X,).to_numpy()
    Y = pd.DataFrame(sql_query_Y,).to_numpy()
    return X,Y

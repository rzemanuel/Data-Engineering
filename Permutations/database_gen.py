import sqlite3
import pandas as pd
from sqlalchemy import create_engine

def sql_create(df):
    engine = create_engine('sqlite:///White_Balance.db')
    df.to_sql("WB_Table_SP5600", engine)

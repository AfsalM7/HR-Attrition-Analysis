import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
password = os.getenv('DB_PASSWORD')

df = pd.read_csv('../HR_Attrition.csv')

engine = create_engine(f'mysql+pymysql://root:{password}@localhost/hr_attrition')

df.to_sql('employee_attrition', con=engine, if_exists='replace', index=False)

print("Data loaded successfully into MySQL!")
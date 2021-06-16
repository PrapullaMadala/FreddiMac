import os
import pandas as pd
from sqlalchemy import create_engine

# accessing source data files
file_list = []
if 'historical_data_2013' in os.listdir('.'):
    for file in os.listdir('historical_data_2013'):
        if file.endswith('.txt'):
            file_list.append(os.path.abspath('historical_data_2013/'+file))
            file_list.sort()

# Dataframe Colum Names 
columns = [
    'CREDIT_SCORE', 'FIRST_PAYMENT_DATE',
    'FIRST_TIME_HOMEBUYER_FLAG','MATURITY_DATE',
    'METROPOLITAN_STATISTICAL_AREA','MORTGAGE_INSURANCE_PERCENTAGE',
    'NUMBER_OF_UNITS','OCCUPANCY_STATUS',
    'ORIGINAL_COMBINED_LOAN_TO_VALUE_CLTV','ORIGINAL_DEBT_TO_INCOME_DTI',
    'ORIGINAL_UPB','ORIGINAL_LOAN_TO_VALUE_LTV',
    'ORIGINAL_INTEREST_RATE','CHANNEL',
    'PREPAYMENT_PENALTY_MORTGAGE_PPM_FLAG','AMORTIZATION_TYPE',
    'PROPERTY_STATE','PROPERTY_TYPE',
    'POSTAL_CODE','LOAN_SEQUENCE_NUMBER',
    'LOAN_PURPOSE','ORIGINAL_LOAN_TERM',
    'NUMBER_OF_BORROWERS','SELLER_NAME',
    'SERVICER_NAME','SUPER_CONFIRMING_FLAG',
    'PRE-HARP_LOAN_SEQUENCE_NUMBER','PROGRAM_INDICATOR',
    'HARP_INDICATOR','PROPERTY_VALUATION_METHOD',
    'INTEREST_ONLY_INDICATOR'
    ]

#creating dataframe with all the data from source dataset
df = pd.DataFrame()
for file in file_list:
    print(file)
    frame = pd.read_csv(file, sep='|', names=columns)
    df = df.append(frame, ignore_index=True)
print(os.environ['SHELL'])
print(os.environ.get('AWS_SECRET_ACCESS_KEY'))
if "RDS_HOSTNAME" in os.environ:
    print('true')

print(dict(os.environ)['RDS_HOSTNAME'])
# RDS (MySQL) Instance details
try:
    HOST = os.environ['RDS_HOSTNAME']
    USER = os.environ['RDS_USERNAME']
    PASSWORD = os.environ['RDS_PASSWORD']
    PORT = os.environ['RDS_PORT']
    DATABASE = os.environ['RDS_DB_NAME']
except KeyError:
    print('This Environment variable is not avilable')


db = 'mysql+mysqlconnector://' + USER +':'+ PASSWORD + '@' + HOST + ':'+ PORT + '/' + DATABASE
engine = create_engine(db)  
print('engine name', engine)  

df.to_sql(name='loans', con=engine, if_exists='replace', index=False, chunksize=100000)

import pandas as pd
print('pandas: {}'.format(pd.__version__))
import numpy as np
print('numpy: {}'.format(np.__version__))
import seaborn as sns
print('seaborn: {}'.format(sns.__version__))
import geopy as geo
print('geopy: {}'.format(geo.__version__))
import datetime

import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import powerlaw
from geopy import distance

def two_d_format(x):
    if x > 9:
        return str(x)
    return '0' + str(x)

# Process automation
for year in range(18, 19):
    for month in range(1, 13):
        print('Month: ' + str(month))
        for day in range(1, 32):
            file_path = str(year) + '_' + two_d_format(month) + '/' + '20' + str(year) + '-' + two_d_format(month) + '-' + two_d_format(day) + 'istdaten.csv'

            try:
                ## filepath2 = '18_01/2018-01-31istdaten.csv'
                df = pd.read_csv('./sbb_data/' + file_path, delimiter=';')
                df.columns

                # Drop anything that is no train ('Zug')
                df = df.drop(df[(df['PRODUKT_ID'] != 'Zug')].index)
                df = df.drop(df[(df['BETREIBER_ABK'] != 'SBB')].index)
                df.head()

                # Train's arrival is delayed
                df.loc[(df['ANKUNFTSZEIT'].notnull()) & (df['AN_PROGNOSE'].notnull()), 'ankunftsverspatung'] = (df['ANKUNFTSZEIT'] < df['AN_PROGNOSE'])
                df.head()

                # Train's departure is delayed
                df.loc[(df['ABFAHRTSZEIT'].notnull()) & (df['AB_PROGNOSE'].notnull()), 'abfahrtsverspatung'] = (df['ABFAHRTSZEIT'] < df['AB_PROGNOSE'])
                df.head()

                # Load all geopositions
                filepath_geo = './data/geo_pos.csv'
                geo_pos = pd.read_csv(filepath_geo, delimiter=';')

                # Check if all stations exist in the geo_pos dataframe
                exists = df['HALTESTELLEN_NAME'].drop_duplicates().isin(geo_pos['BEZEICHNUNG_OFFIZIELL'])
                print(exists.value_counts())
                if 'False' in exists.value_counts().index:
                    print('STOP!')
                    exit()

                dict_geo_pos = geo_pos.set_index('BEZEICHNUNG_OFFIZIELL').to_dict()['geopos']
                df['geopos'] = df['HALTESTELLEN_NAME'].map(dict_geo_pos)

                df.to_csv(path_or_buf='./new_data/' + file_path,sep=';',index=False) 
            except OSError:
                print('file ' + file_path + ' does not exist')
                continue

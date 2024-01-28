import pandas as pd
import os
import requests

df = pd.read_csv('/home/Test.xx/xxx.csv')
df.to_csv(f'{date}_xx_xx.csv', index=False)
path_1 = '/home/Test'
df_1.to_cs(os.path_1.join(path_1, f'{date}_xx_xx.csv'), index=False)

def select_item(df_1):
    df_0 = pd.DataFrame()
    for item in items:
        condition = (df_1['column_header_a'].str.contains(item) | df_1['b'].str.contains(item))
        df_ab = df_1[condition]
        if df_0.empty:
            df_0 = df_ab
        else:
            df_0 = pd.merge(df_0, df_ab.groupby('time').first(), on='time')
    return df_0


def add_data(df_a, df_b):
    df_all = pd.concat([df_a, df_b], axis=1) # vertical
    return df_all

def subtract(df):
    df['results'] = df['A'] - df['B']
    return df

def sum_all_data(df_all):
    df_sum = pd.DataFrame()
    df_sum['Total_all'] = df_all.iloc[:, 1:].sum(axis=1) # column
    df_total = pd.concat([df_total, df_sum], axis=1)
    return df_total

def combine_data_with_time(df):
    df_A = pd.concat([df.loc[df['column_name'] == 'condition', 'column_A'], df['time']], axis=1)
    df_B = pd.concat([df.loc[df['column_name'] == 'condition', 'column_B'], df['time']], axis=1)
    df_C = pd.concat([df.loc[df['column_name'] == 'condition', 'column_C'], df['time']], axis=1)
    df_merge = df_A.merge(df_B, on='time').merge(df_C, on='time')
    return

# value to column
def split_data(df_table):
    df_0 = pd.DataFrame()
    for item in items:
        df_table['column_name'] = df_table['column_name'].astype(str)
        df_v2c = df_table.loc[df_table['column_name'].str.contains(item)]
        rename_value2column = {'column_value': f'{item}-name'}
        df_v2c.rename(colums=rename_value2column, inplace=True)
        df_v2c = df_v2c[["time", f'{items}-name']]
        if df_0.empty:
            df_0 = df_v2c
        else:
            df_0 = pd.merge(df_0, df_v2c.groupby('time').first(), on='time')
    
def replace_name(df, column, replace_dict):
    df[column] = df[column].replace(replace_dict)

replace_rules = {
    'original_a': 'changed_a',
    'original_b': 'changed_b'
    }
replace_name(df, 'column_name', replace_rules)


# rename header
df.rename(columns={'original': 'changed'}, inplace=True)
# rename values in header
df.loc[df['column_name_a'] == 'ABCD', 'column_name_b'] = 'A'


df.columns # check header
df.columns.tolist()


def fetch_data_wb(url, params):
    params = {
        "date": DATE,
        "time": TIME
    }
    response = requests.get(url, params=params)
    json_dict = response.json()
    return json_dict

url = "https://www.abc.com"
time = ["A", "B"]
date = "2023-12-22"

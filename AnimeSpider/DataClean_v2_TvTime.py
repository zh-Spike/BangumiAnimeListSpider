import csv
import pandas as pd
d = pd.read_csv(r'Ex_Finalv2.csv')


def DateSplit(df, col):
    temp_df = df[col].str.split('/', expand=True)
    temp_df.columns = ["month", "day", "year"]
    df = pd.concat([df, temp_df], axis=1)
    df = df.drop("movie_time", axis=1)
    return df


data = DateSplit(d, col='movie_time')
data.to_csv(r'Movie_Time.csv', encoding='UTF-8')

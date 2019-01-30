import pandas as pd
import numpy as np

citi_bike = pd.read_csv("data/201811-citibike-tripdata.csv")
nov18_df = pd.DataFrame(citi_bike)
nov18_df.head(20)
nov18_df.dtypes
nov18_df['gender'] = nov18_df['gender'].map({0:'unknown', 1:'male', 2:'female'})
nov18_df.rename(columns={'tripduration': "trip duration (seconds)"}, inplace = True)
nov18_df.dtypes
nov18_df.isnull().any()
nov18_df.count()
nov18_df.dropna(how='any', inplace=True)
nov18_df.count()
nov18_df.head(20)
nov18_df.to_csv("data/clean_201811.csv", index=False)

dec_citi_bike = pd.read_csv("data/201812-citibike-tripdata.csv")
dec18_df = pd.DataFrame(dec_citi_bike)
dec18_df.head(20)
dec18_df.dtypes
dec18_df['gender'] = dec18_df['gender'].map({0:'unknown', 1:'male', 2:'female'})
dec18_df.rename(columns={'tripduration': "trip duration (seconds)"}, inplace = True)
dec18_df.dtypes
dec18_df.isnull().any()
dec18_df.count()
dec18_df.dropna(how='any', inplace=True)
dec18_df.count()
dec18_df.head(20)
dec18_df.to_csv("data/clean_201812.csv", index=False)

june_citi_bike = pd.read_csv("data/201806-citibike-tripdata.csv")
june18_df = pd.DataFrame(june_citi_bike)
june18_df.head(20)
june18_df.dtypes
june18_df['gender'] = june18_df['gender'].map({0:'unknown', 1:'male', 2:'female'})
june18_df.rename(columns={'tripduration': "trip duration (seconds)"}, inplace = True)
june18_df.dtypes
june18_df.isnull().any()
june18_df.count()
june18_df.to_csv("data/clean_201806.csv", index=False)

july_citi_bike = pd.read_csv("data/201807-citibike-tripdata.csv")
july18_df = pd.DataFrame(july_citi_bike)
july18_df.head(20)
july18_df.dtypes
july18_df['gender'] = july18_df['gender'].map({0:'unknown', 1:'male', 2:'female'})
july18_df.rename(columns={'tripduration': "trip duration (seconds)"}, inplace = True)
july18_df.dtypes
july18_df.isnull().any()
july18_df.count()
july18_df.to_csv("data/clean_201807.csv", index=False)

aug_citi_bike = pd.read_csv("data/201808-citibike-tripdata.csv")
aug18_df = pd.DataFrame(aug_citi_bike)
aug18_df.head(20)
aug18_df.dtypes
aug18_df['gender'] = aug18_df['gender'].map({0:'unknown', 1:'male', 2:'female'})
aug18_df.rename(columns={'tripduration': "trip duration (seconds)"}, inplace = True)
aug18_df.dtypes
aug18_df.isnull().any()
aug18_df.count()
aug18_df.dropna(how='any', inplace=True)
aug18_df.count()
aug18_df.head(20)
aug18_df.to_csv("data/clean_201808.csv", index=False)

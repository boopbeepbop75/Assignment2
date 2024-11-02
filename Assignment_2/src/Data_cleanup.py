import Utils as U
from Utils import data, clean_data
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
from datetime import datetime

current_year = datetime.now().year

def load_data():
    print("Loading Dataframe...")
    df = pd.read_csv(data)
    print(df.head())
    print("Missing values in each column:")
    print(df.isna().sum())
    # Drop rows with any missing values
    df['New_Price'] = df['New_Price'].fillna(0)
    df = df.dropna()
    #Since there's only 5847 rows (data points) I will be removing missing values instead of using mean replacement
    #I think I will just drop the New_Price column as a whole since it's missing data points in most all of the rows


    print('\nCleaning up units...')
    df['Power'] = df['Power'].str.replace(' bhp', '').astype(float)
    df['Engine'] = df['Engine'].str.replace(' CC', '').astype(float)
    df['Mileage'] = df['Mileage'].str.replace(' kmpl', '').str.replace(' km/kg', '').astype(float)
    df['New_Price'] = df['New_Price'].str.replace(' Lakh', '')#.astype(float)

    #Change categorical to numerical
    print("\nMapping Categorical columns to numerical columns...")
    fuel_map = {'Diesel': 0, 'Petrol': 1, 'Electric': 2}
    transmission_map = {'Manual': 0, 'Automatic': 1}
    df['Fuel_Type'] = df['Fuel_Type'].map(fuel_map)
    df['Transmission'] = df['Transmission'].map(transmission_map)

    #Create current age column
    print("\nCreating Current_Age column for each row...")
    df['Current_Age'] = current_year - df['Year']

    #Various functions
    print("Performing the various functions on the data...")

    # Select specific columns
    df_selected = df[['Year', 'Current_Age']]
    print(f"Selected Columns: {df_selected}")

    #Filtering
    df_filtered = df.query('Power > 100')
    print(f"Cars with power higher than 100: {df_filtered}")

    # Renaming
    df_renamed = df.rename(columns={'Current_Age': 'Car_Age'})
    print(f"Renamed column df: {df_renamed}")

    #Arrange / sort
    df_sorted = df.sort_values(by='Kilometers_Driven', ascending=False)
    print(f"df sorted in descending driven distance: {df_sorted}")

    #Summarize
    df_summary = df.groupby('Location')['Power'].mean().reset_index()
    print(f"Summarized df based on the locations purchased and the Power: {df_summary}")

    #I'm going to remove the New_Price column here since there was a task with it after the original data cleanup/deletion
    df = df.drop('New_Price', axis=1)

    print(f"/nDataframe dimension: Rows: {df.shape[0]}, columns: {df.shape[1]}")
    print(df.head())

    #Save cleaned up df to data_clean folder
    df.to_csv(clean_data, index=False)

if __name__ == "__main__":
    load_data()

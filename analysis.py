import pandas as pd

def load_data(filename):
 return pd.read_csv(filename)

def analyze_data(data):
 return data.describe()

def visualize_data(data):
 return data.plot(kind='bar')

import pandas as pd

data = pd.read_csv("C:\\Users\\Kshit\\Desktop\\KYC\\iit.csv")

# Convert 'OR' and 'CR' columns to numeric, ignoring invalid values
data['OR'] = pd.to_numeric(data['OR'], errors='coerce')
data['CR'] = pd.to_numeric(data['CR'], errors='coerce')

def filter_colleges_iit(data, gender, category, rank):
    filtered_df = data[(data['Gender'] == gender) & (data['Category '] == category) & ((data['OR'] <= rank) & (data['CR'] >= rank))]
    return filtered_df[['College', 'Branch ']]

# User inputs
gender = input("Enter your gender (M/F): ")
category = input("Enter your category: ")
rank = int(input("Enter your rank: "))

# Filtering colleges based on user inputs
filtered_colleges = filter_colleges_iit(data, gender, category, rank)
print(filtered_colleges)

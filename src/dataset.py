import pandas as pd

# Creating a dataframe
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'age': [25, 30, 35, 40],
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
}

df = pd.DataFrame(data)

df.head(2)  # Display the first few rows of the dataframe
df.info

df.replace({'city': {'New York': 'NYC', 'Los Angeles': 'LA', 'Chicago': 'CHI', 'Houston': 'HOU'}}, inplace=True)

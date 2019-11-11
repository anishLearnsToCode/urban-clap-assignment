import pandas as pd

# indexed_data = pd.read_csv("data-set.csv", index_col='provider_id')
data = pd.read_csv('data-set.csv')
dataFrame = pd.DataFrame(data)
unique_providers = dataFrame['provider_id'].unique()
number_of_unique_providers = unique_providers.size

# first = indexed_data.loc[unique_providers[1]]
# first.sort_values(['event_time'])
# print(first.loc[:, 'provider_id'])

result = pd.DataFrame(columns=['provider_id', 'date', 'start_time', 'end_time', 'total_seconds'])
result.loc[len(result)] = [100, 1, 2, 0, 10000]
print(result)

print(result.loc[100])
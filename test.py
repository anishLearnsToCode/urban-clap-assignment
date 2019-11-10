# Load the Pandas libraries with alias 'pd'
from datetime import datetime

import pandas as pd


def add_result(startTime, endTime, provider_id):
    print('func called')
    start_time = datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S.%f')
    end_time = datetime.strptime(endTime, '%Y-%m-%d %H:%M:%S.%f')
    result.loc[len(result)] = [provider_id, startTime, start_time.time(), end_time.time(), (end_time - start_time) * 60]
    return


indexed_data = pd.read_csv("data-set.csv", index_col='provider_id')
data = pd.read_csv('data-set.csv')
dataFrame = pd.DataFrame(data)
unique_providers = dataFrame['provider_id'].unique()
number_of_unique_providers = unique_providers.size

# first = unique_providers[0]
# print(first)
# print(indexed_data.loc[unique_providers[0]])
first = indexed_data.loc[unique_providers[1]]
first.sort_values(['event_time'])
# print(first)
# print((first.iloc[0, 2]))

# datetime_object = datetime.strptime((first.iloc[0, 2]), '%Y-%m-%d %H:%M:%S.%f')
# print(datetime_object.day)

result = pd.DataFrame(columns=['provider_id', 'date', 'start_time', 'end_time', 'total_seconds'])
# result.loc[len(result)] = [100, 1, 2, 0, 10000]
print(result)



isOnline = False
startTime = 0
endTime = 0

for provider_id, entry in first.iterrows():
    if 'True' in (str(entry['detail'])) or 'Action on Job' in (str(entry['detail'])):
        if isOnline is False:
            startTime = entry['event_time']
            isOnline = True
    else:
        if isOnline:
            endTime = entry['event_time']
            isOnline = False
            add_result(startTime, endTime, provider_id)


print(result)

for index, entry in result:
    print(index, entry)

# print(dataFrame.loc[: , 'detail'])

# providersMap = getProvidersMapFrom(dataFrame)
#
# for (int providerData : providersMap.getEnrySet()):
#     for (dateData : providersMap.getValue().getValueSet()) :

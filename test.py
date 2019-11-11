from datetime import datetime
import pandas as pd


def entry_does_not_exist(hour, provider, date):
    return hour in result[provider].loc[:, ]


def create_entry(provider, hour, date):
    result.loc[len(result)] = [provider, date, hour, hour + 1, 0]


def update_seconds(provider, date, hour, start_time, end_time):
    result.at[provider, 'total_seconds'] += 1000


def add_result(start_time, end_time, provider_id):
    start_time_stamp = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S.%f')
    end_time_stamp = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S.%f')

    start_hour = 8 if start_time_stamp.hour <= 8 else start_time_stamp.hour
    end_hour = 19 if end_time_stamp.hour >= 19 else end_time_stamp.hour

    for time in range(start_hour, end_hour + 1):
        if entry_does_not_exist(time, provider_id, start_time_stamp.date()):
            create_entry(provider_id, time, start_time_stamp.date())

        update_seconds(provider_id, start_time_stamp.date(), time, start_time_stamp, end_time_stamp)

    # result.loc[len(result)] = [provider_id, startTime, start_time_stamp.time(), end_time_stamp.time(), (end_time_stamp - start_time_stamp) * 60]
    return


def main():
    print('hello world')


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
print(first)
# print((first.iloc[0, 2]))

# datetime_object = datetime.strptime((first.iloc[0, 2]), '%Y-%m-%d %H:%M:%S.%f')
# print(datetime_object.day)

result = pd.DataFrame(columns=['provider_id', 'date', 'start_time', 'end_time', 'total_seconds'])
# result.loc[len(result)] = [100, 1, 2, 0, 10000]
# print(result)


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

# print(first['event_time'])
# print(result['date'])
# print(first['details'])

# for index, entry in result:
#     print(entry)

# print(dataFrame.loc[: , 'detail'])

# providersMap = getProvidersMapFrom(dataFrame)
#
# for (int providerData : providersMap.getEnrySet()):
#     for (dateData : providersMap.getValue().getValueSet()) :

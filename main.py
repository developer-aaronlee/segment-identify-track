import pandas as pd
import requests
import json

segment_identify = "https://api.segment.io/v1/identify"
segment_track = "https://api.segment.io/v1/track"

dev_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic api_key"
}

qa_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic api_key"
}

prod_headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic api_key"
}


df = pd.read_csv("result-37.csv")
# print(df)

df.fillna("", inplace=True)
isna_rows = df[df.isna().values.any(axis=1)]
# print(isna_rows)

all_data = df.to_numpy()
# print(all_data)

columns = df.columns
# print(columns)


def set_properties(num):
    properties = {}
    for i in range(1, 6):
        if i == 2:
            continue
        properties[columns[i]] = all_data[num][i]

    return properties


for x in range(11, len(all_data)):
    identify = {
        columns[0]: all_data[x][0],
        "traits": {
            columns[i]: all_data[x][i] for i in range(1, 3)
        }
    }

    identify_call = json.dumps(identify)
    # print(identify_call)

    track = {
        columns[0]: all_data[x][0],
        "event": "Marketing Opted In",
        "properties": set_properties(x),
        columns[6]: all_data[x][6]
    }

    track_call = json.dumps(track)
    # print(track_call)

    # response = requests.post(url=segment_identify, data=identify_call, headers=prod_headers)
    # print(f"Row {x + 1} identify call: {all_data[x][0]} Response:", response.json())
    #
    # response = requests.post(url=segment_track, data=track_call, headers=prod_headers)
    # print(f"      track call: {all_data[x][0]} Response:", response.json())

import requests
import pandas as pd
import numpy as np

r = requests.get("https://gtapp-api.rnoc.gatech.edu/api/v1/organizations")
data = r.json()

df = pd.DataFrame(data)
df = df[['name', 'category', 'moreInfoURL', 'logoURL', 'id', 'description', 'membership', 'meetingDetails',
         'websiteURL']]

# Add full description column, concatenating name and description
full_descs = []
for name, description in zip(df.name, df.description):
    full_desc = str(name) + "\n" + str(description)
    full_descs.append(full_desc)
df["full_desc"] = full_descs

df.to_csv("data.csv")
print("Database update successful.")

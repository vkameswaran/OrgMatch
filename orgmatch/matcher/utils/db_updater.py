import requests
import pandas as pd
import numpy as np

r = requests.get("https://gtapp-api.rnoc.gatech.edu/api/v1/organizations")
data = r.json()

df = pd.DataFrame(data)
df = df[['name', 'category', 'moreInfoURL', 'logoURL', 'id', 'description', 'membership', 'meetingDetails',
         'websiteURL']]

df.to_csv("data.csv")
print("Database update successful.")
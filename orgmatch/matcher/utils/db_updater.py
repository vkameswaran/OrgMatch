import requests
import pandas as pd
import numpy as np
import spacy
import pickle

nlp = spacy.load("en_core_web_sm")

r = requests.get("https://gtapp-api.rnoc.gatech.edu/api/v1/organizations")
data = r.json()

df = pd.DataFrame(data)
df = df[['name', 'category', 'moreInfoURL', 'logoURL', 'id', 'description', 'membership', 'meetingDetails',
         'websiteURL']]

# Add full description column, concatenating name and description
full_descs = []
for name, description in zip(df.name, df.description):
    full_desc = str(name) + "\n" + str(description)
    full_desc = " ".join([token.lemma_ for token in nlp(full_desc.lower()) if not token.is_stop])
    full_descs.append(full_desc)
df["full_desc"] = full_descs

df.to_csv("data.csv")
with open("data.pkl", 'wb') as fh:
    pickle.dump(df, fh)
print("Database update successful.")

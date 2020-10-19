import numpy as np
import pandas as pd
import spacy
import pickle
nlp = spacy.load("en_core_web_sm")

# orgs_df = pd.read_csv("matcher/utils/data.csv", index_col="Unnamed: 0")

with open("matcher/utils/data.pkl", 'rb') as f:
    orgs_df = pickle.load(f)
# Compare to given keywords

def rank_against_keywords(list_of_keywords):
    def search(desc_series):
        sims = []
        for desc in desc_series:
            sims.append(sum([
                desc.count(keyword.lemma_)
                for keyword in nlp(" ".join(list_of_keywords).lower())
                ]))
        return sims
    sorted_df = orgs_df
    sorted_df["match_results"] = search(sorted_df.full_desc)
    sorted_df = sorted_df.sort_values("match_results", ascending=False)
    return sorted_df

def rank_against_keyword(keyword):
    def search(desc_series):
        sims = []
        for desc in desc_series:
            sims.append(
                desc.count(nlp(keyword.lower())[0].lemma_)
                )
        return sims
    sorted_df = orgs_df
    sorted_df["match_results"] = search(sorted_df.full_desc)
    sorted_df = sorted_df.sort_values("match_results", ascending=False)
    return sorted_df

def get_results(df, num_results):
    temp_results = df.head(num_results)
    temp_results = temp_results[temp_results.match_results != 0]
    temp_results["new_url"] = temp_results["name"].apply(lambda x : "https://gatech.campuslabs.com/engage/organization/" + x.lower().replace("@", "").replace("'", "").replace("  ", " ").replace(" ", "-"))
    return temp_results.values

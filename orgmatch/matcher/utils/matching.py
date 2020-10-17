import pandas as pd

orgs_df = pd.read_csv("matcher/utils/data.csv", index_col="Unnamed: 0")

# Compare to given keywords

def rank_against_keywords(list_of_keywords):
    def search(desc_series):
        sims = []
        for desc in desc_series:
            sims.append(sum([desc.count(keyword.lower()) for keyword in list_of_keywords]))
        return sims
    sorted_df = orgs_df.sort_values("full_desc", ascending=False, key=search)
    return sorted_df

def rank_against_keyword(keyword):
    def search(desc_series):
        sims = []
        for desc in desc_series:
            sims.append(desc.count(keyword.lower()))
        return sims
    sorted_df = orgs_df.sort_values("full_desc", ascending=False, key=search)
    return sorted_df

def get_results(df, num_results):
    temp_results = df.head(num_results)
    return temp_results.values




def build_features(df):
    #Handle Missing values
    df["title"] = df["title"].fillna("").str.strip().str.lower().astype('string')
    df["listed_in"] = df["listed_in"].fillna("").str.strip().str.lower().astype('string')
    df["description"] = df["description"].fillna("").str.strip().str.lower().astype('string')

    return df






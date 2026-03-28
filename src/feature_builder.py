'''
Create combined_text column
'''


def build_features(df):
    title = df["title"].str.strip().astype('string')
    genres = df["listed_in"].str.strip().astype('string')
    description = df["description"].str.strip().astype('string')
    combined_text = title + " " + genres + " " + description
    df["combined_text"] = combined_text
    return df






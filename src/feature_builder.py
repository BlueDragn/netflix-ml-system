'''
Create combined_text column
'''


def build_features(df):
    #Handle Missing values
    df["title"] = df["title"].fillna("")
    df["listed_in"] = df["listed_in"].fillna("")
    df["description"] = df["description"].fillna("")


    title = df["title"].str.strip().str.lower().astype('string')
    genres = df["listed_in"].str.strip().str.lower().astype('string')
    description = df["description"].str.strip().str.lower().astype('string')

    combined_text = (
        title + " " + title + " " + title + " " +      # Strong boost title importance
        genres + " " + genres + " " +                  #boost genre importance
        description                                    #base info
)



    df["combined_text"] = combined_text
    return df






import pandas as pd

df = pd.read_csv('emotions_with_duplicates.csv')


def remove_duplicates(string_of_list_of_synonyms):
    string_of_list_of_synonyms = string_of_list_of_synonyms.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
    list_of_synonyms = string_of_list_of_synonyms.split(",")
    set_of_synonyms_without_duplicates = set(list_of_synonyms)
    list_of_synonyms_without_duplicates = list(set_of_synonyms_without_duplicates)
    string_of_list_of_synonyms_without_duplicates = str(list_of_synonyms_without_duplicates)
    return string_of_list_of_synonyms_without_duplicates


for i in range(0, len(df)):
    df.iloc[i, 2] = remove_duplicates(df.iloc[i, 2])

df.to_csv('emotions_without_duplicates.csv', index=False)

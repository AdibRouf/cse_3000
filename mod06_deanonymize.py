import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    match_columns = ["age", "zip3", "gender"]

    matches = anon_df.merge(
        aux_df,
        on=match_columns,
        how="inner"
    )

    matches = matches.drop_duplicates(
        subset=match_columns,
        keep=False
    )

    return matches[["anon_id", "name"]].rename(
        columns={"name": "matched_name"}
    )
    
    raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    return len(matches_df)/len(anon_df)

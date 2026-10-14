import pandas as pd

COLS_TO_ADD = [
    "AdjudicatedValue",
    "ResolutionType(AuthorKept ValidatorKept/Compromise)",
    "PostDiscussAgreementstatus(Yes/No)",
    "PostKeyEvidence",
    "Comments"
]

validation_df = pd.read_csv("eabbott9_validation_log.csv", delimiter=";")

full_df = validation_df.rename(columns={'KeyEvidence': 'PreKeyEvidence'})
for col in COLS_TO_ADD:
    full_df[col] = "N/A"

full_df.to_csv("full.csv", sep=";", index=False)

disagreement_df = full_df[full_df["PreDiscussAgreementstatus(Yes/No)"] == 'No']
disagreement_df.to_csv("eabbott9_disagreement_resolution.csv", sep=";", index=False)
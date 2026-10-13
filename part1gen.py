import pandas as pd
import os

if os.path.exists("part1.csv"):
    print("Part 1 CSV already exists!")
    exit(-1)

PARTNER = "dkim68"
MYSELF = "eabbott9"

VALIDATION_CSV_FIELDS = [
    "HasRecovered",
    "WhyRecovered",
    "ActivityPattern",
    "Currentstatus",
    "RecentThemes",
]

PART_1_COLS = [
    "WOCProjectID",                         # "Project" column, github link
    "ProjectOwnerNetID",                    # dkim68
    "ValidatorNetID",                       # eabbott9
    "Field",                                # VALIDATION_CSV_FIELDS
    "AuthorValue",                          # value partner put for Field
    "ValidatorValue",                       # value you would put for Field
    "PreDiscussAgreementstatus(Yes/No)",    # AuthorValue == ValidatorValue?
    "KeyEvidence",                          # evidence for your value for Field
]

PART_2_COLS = [
    "AdjudicatedValue",                     # if disagree, which value did you pick
    "ResolutionType",                       # if disagree, why did you pick that
    "PostDiscussAgreementStatus",           # Fill this out after Discord call
    "Comments",                             # Fill this out yourself
]


df = pd.read_csv("dkim68_project_stats.csv", delimiter=";")
projects = df["Project"].unique().tolist()

part1df = pd.DataFrame(columns=PART_1_COLS)

for project in projects:
    for field in VALIDATION_CSV_FIELDS:
        value = df[df["Project"] == project][field].tolist()[0]
        part1df.loc[len(part1df)] = [
            project,
            PARTNER,
            MYSELF,
            field,
            value,
            "",
            "Yes",
            ""
        ]

part1df.to_csv("part1.csv", index=False, sep=";")
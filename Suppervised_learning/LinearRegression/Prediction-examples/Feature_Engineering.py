import pandas as pd
import numpy as np

# LOAD DATASET
df = pd.read_csv("verbo_data.csv")

# Removing unnecessary columns
columns_to_keep = [
    "payment_status",
    "is_cancelled",
    "price_per_night",
    "total_price",
    "nights",
    "listing_city",
    "checkin_date",
    "checkout_date"
]

df = df[columns_to_keep]

# DATA TYPE CASTING - NUMERIC COLUMNS
numeric_columns = [
    "price_per_night",
    "total_price",
    "nights",
]

for col in numeric_columns:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )


# Remove duplicated rows to prevent the same
df = df.drop_duplicates()

# Convert date strings into datetime objects so
df["checkin_date"] = pd.to_datetime(
    df["checkin_date"],
    errors="coerce"
)

df["checkout_date"] = pd.to_datetime(
    df["checkout_date"],
    errors="coerce"
)

# Invalid statuses are replaced with NaN and then imputed as "pending".
df["payment_status"] = (
    df["payment_status"]
    .astype(str)
    .str.lower()
    .str.strip()
)

df = pd.get_dummies(
    df,
    columns=["payment_status"],
    dtype=int
)


df["is_cancelled"] = (
    df["is_cancelled"]
    .astype(str)
    .str.lower()
    .str.strip()
)

cancel_map = {
    "true": 1,
    "yes": 1,
    "y": 1,
    "1": 1,
    "false": 0,
    "no": 0,
    "n": 0,
    "0": 0
}

df["is_cancelled"] = (
    df["is_cancelled"]
    .map(cancel_map)
    .astype(int)
)

df["is_cancelled"] = (
    df["is_cancelled"]
    .fillna(0)
)


# FEATURE ENGINEERING - CALCULATED NIGHTS
df["nights_calculated"] = (
    df["checkout_date"] -
    df["checkin_date"]
).dt.days

# DATA CLEANING - INVALID NIGHTS
df.loc[
    df["nights"] <= 0,
    "nights"
] = np.nan

# MISSING VALUE IMPUTATION - NIGHTS
df["nights"] = (
    df["nights"]
    .fillna(df["nights_calculated"])
)

# MISSING VALUE IMPUTATION - REMAINING NIGHTS
df["nights"] = (
    df["nights"]
    .fillna(df["nights"].median())
)

df["checkin_weekday"] = (
    df["checkin_date"]
    .dt.dayofweek
    .fillna(-1)
    .astype(int)
)

print('-----------------')
print(df["checkin_date"].isna().sum())

# FEATURE SELECTION
df.drop(
    columns=[
        "checkin_date",
        "checkout_date",
        "nights_calculated",
    ],
    inplace=True
)

# MISSING VALUE IMPUTATION - NUMERIC FEATURES
numeric_features = [
    "price_per_night",
    "total_price",
]

for col in numeric_features:
    df[col] = (
        df[col]
        .fillna(df[col].median())
    )

city_map = {
    "la": "los_angeles",
    "los angeles": "los_angeles",
    "los_angeles": "los_angeles",

    "nyc": "new_york",
    "new york": "new_york",
    "new_york": "new_york",

    "sf": "san_francisco",
    "san fran": "san_francisco",
    "san francisco": "san_francisco"
}

df["listing_city"] = (
    df["listing_city"]
    .astype(str)
    .str.lower()
    .str.strip()
    .replace(city_map)
)

# DATA CLEANING - CITY NAMES
df["listing_city"] = (
    df["listing_city"]
    .fillna("unknown")
    .str.lower()
    .str.strip()
)

df.drop(df[df["listing_city"] == "unknown"].index, inplace=True)

# # ONE-HOT ENCODING
# # Convert categorical variables into numerical
df = pd.get_dummies(
    df,
    columns=[
        "listing_city",
    ],
        dtype=int
)

# FEATURE SCALING (MIN-MAX NORMALIZATION)
scale_columns = [
    "price_per_night",
    "total_price",
    "nights",
]

for col in scale_columns:
    min_val = df[col].min()
    max_val = df[col].max()
    
    print('-----------')
    print(min_val, max_val)
    print(f"Column '{col}' - Min: {min_val}, Max: {max_val}")
    if max_val != min_val:
        df[col] = (
            (df[col] - min_val)
            / (max_val - min_val)
        )

# DATA SPLITTING
# 80% training data and 20% testing data.
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

split_index = int(len(df) * 0.8)

train_df = df[:split_index]
test_df = df[split_index:]

print("Training Shape:", train_df.shape)
print("Testing Shape:", test_df.shape)

print("\nColumns:")
print(df.columns.tolist())
print(df.info())
print("\nDataset Preview:")
print(df.head(20))
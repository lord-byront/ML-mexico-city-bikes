import pandas as pd

# Load both CSV files
ecobici_df = pd.read_csv("Resources/ecobici_stations.csv")
data_df = pd.read_csv("Resources/data-2025-03-28.csv")

# Merge on num_cicloe
merged_df = pd.merge(
    ecobici_df,
    data_df[["num_cicloe", "colonia", "alcaldia", "latitud", "longitud", "sitio_de_e", "estatus"]],
    on="num_cicloe",
    how="left"
)

# Format all string columns to title case
def title_case(s):
    if isinstance(s, str):
        return s.title()
    return s

for col in merged_df.select_dtypes(include='object').columns:
    merged_df[col] = merged_df[col].apply(title_case)

# Save to CSV
merged_df.to_csv("ecobici_merged.csv", index=False, encoding="utf-8-sig")

print("✅ File saved with proper capitalization: ecobici_merged.csv")


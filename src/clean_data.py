import pandas as pd
import config as cf
from loguru import logger

# clean tracker_master
df = pd.read_parquet(cf.path_data_raw + "tracker_master_raw.parquet")

for col in ["Price", "Shares", "Value", "Expected Yield","Risk","Comision","Spain","Europe","US","EM","Int","Delta index"]:
    df[col] = df[col].str.replace(r"[€,%]", "", regex=True)
    df[col] = pd.to_numeric(df[col], errors='coerce')

for col in ["Expected Yield","Spain","Europe","US","EM","Int"]:
    df[col] = df[col].fillna(0)

df.to_parquet(cf.path_data_processed + "tracker_master_processed.parquet")
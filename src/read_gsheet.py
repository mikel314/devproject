import gspread
import pandas as pd
import config as cf


def read_gsheet(credentials, filename, sheetname):
    # Autenticación con Google Sheets
    gc = gspread.service_account(filename=credentials)

    # Abrir el documento de Google Sheets por nombre
    spreadsheet = gc.open(filename)

    # Seleccionar la pestaña (tab) por nombre
    worksheet = spreadsheet.worksheet(sheetname)

    # Obtener todos los valores de la hoja
    data = worksheet.get_all_records()

    # Convertir a DataFrame de Pandas
    df = pd.DataFrame(data)
    df = df.astype(str)

    return df


# Read master data from Google Sheets
tracker_master = read_gsheet(cf.cred_file, "Tracker", "Master")
print(tracker_master.head)

tracker_master.to_parquet(cf.path_data_raw + "tracker_master.parquet")
# df = pd.read_parquet("data.parquet", engine="pyarrow")
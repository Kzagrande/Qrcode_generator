import sys
project_root = "C:\\Users\\casag\\Qrcode_generator"
sys.path.insert(0, project_root)
import os
from src.qr_code_generator.google_sheet_auth import GoogleSheetAuth
from typing import List
import pandas as pd
from src.interfaces.google_sheet_getter import GoogleSheetGetterInterface

class GoogleSheetGetter(GoogleSheetGetterInterface):
    def __init__(self):
        self.spreadsheet_id = "1BPJqdN2d_wTtJBktzWEtir0L1HkxMpGjTHqnSox7-c0"

    def get_sheet(self) -> str:  # Alterado o tipo de retorno para uma string
        excel_file = ""  # Inicialize a variável excel_file fora do bloco try
        try:
            auth = GoogleSheetAuth()
            self.service = auth.get_service()

            sheet = self.service.spreadsheets()
            result = (
                sheet.values()
                .get(
                    spreadsheetId=self.spreadsheet_id,
                    range="ATIVOS!A:R",
                )
                .execute()
            )
            values = result.get("values", [])
            print(values)

            if values:
                filtered_values = [
                    row for row in values if len(row) >= 1
                ]
                df = pd.DataFrame(filtered_values[1:], columns=filtered_values[0])
                download_path = os.path.expanduser("~") + "\\Downloads\\"
                excel_file = os.path.join(download_path, "hc.xlsx")
                df.to_excel(excel_file, index=False)
                print(f"Arquivo 'hc.xlsx' salvo em {excel_file}")
            else:
                print("No data found.")
        except Exception as exception:
            print('error', exception)

        return excel_file  # Retorne a variável excel_file

if __name__ == "__main__":
    getter = GoogleSheetGetter()
    result = getter.get_sheet()
    print("Excel file:", result)

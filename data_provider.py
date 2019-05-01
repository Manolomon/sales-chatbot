import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import config

class DataProvider:
    """
    Data manager. 
    Deals with the connection to the Google Sheets 
    API and the data extraction
    """

    def __init__(self, obj_cells, past_cells):
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://www.googleapis.com/auth/spreadsheets.readonly',
            'https://www.googleapis.com/auth/drive.readonly']
            
        creds = ServiceAccountCredentials.from_json_keyfile_name(config.API_KEY_FILENAME, scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open(config.SHEET_NAME).sheet1

        # Extract the data from the cells of interest
        self.objetiveList = sheet.acell(obj_cells).value
        self.pastList = sheet.acell(past_cells).value

    def get_objectives(self):
        return self.objetiveList

    def get_past_entries(self):
        return self.pastList

if __name__ == "__main__":
    data_prov = DataProvider('G5', 'H5')
    print(data_prov.get_objectives())
    print(data_prov.get_past_entries())

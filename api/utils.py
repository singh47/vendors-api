# excel file is already given in the directory
import pandas
import os
from datetime import datetime

EXCEL_FILE = 'vendor_data.xlsx'

def load_execl_data():
    excel_data = pandas.read_excel(os.path.abspath(EXCEL_FILE))
    #data = pandas.DataFrame(excel_data, columns=['vndr_nm'])
    return excel_data.to_records()

def string_to_date(date_string):
    if not isinstance(date_string, str):
        return date_string
    return datetime.strptime(date_string, "%d/%M/%Y").date()
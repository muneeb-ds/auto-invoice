import os
import openpyxl
from datetime import datetime
import calendar

class UpdateInvoice:
    def __init__(self) -> None:
        self.wb = openpyxl.load_workbook('invoice_template.xlsx')
        self.sheet = self.wb['Invoice']

    def format_date(self):
        today = datetime.today()
        date_updated = today.strftime("%d-%b-%Y")

        return today, date_updated

    def get_date_elements(self, date):
        month = date.strftime("%b")
        year = date.year

        max_day = calendar.monthrange(year, date.month)[1]

        return month, year, max_day
    
    def save_workbook(self, month, year):
        os.makedirs("invoices", exist_ok=True)
        self.wb.save(f"invoices/invoice_{month}_{year}.xlsx")

    def update_sheet(self):
        today, date_updated = self.format_date()
        month, year, max_day = self.get_date_elements(today)

        self.sheet['B1'] = f"INVOICE #{date_updated}"
        self.sheet['B11'] = f"Pay from 01-{month}-{year} to {max_day}-{month}-{year}"
        self.save_workbook(month, year)


from invoice import UpdateInvoice
from email_inv import EmailUpdate

def main():
    finance_email = 'syedmuneeb54@gmail.com'

    UpdateInvoice().update_sheet()
    EmailUpdate(finance_email).send()

if __name__ == "__main__":
    main()
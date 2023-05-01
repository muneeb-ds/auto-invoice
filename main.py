from argparse import ArgumentParser

from invoice import UpdateInvoice
from email_inv import EmailUpdate

def main():
    parser = ArgumentParser()
    parser.add_argument("--receiver",
                        help="email address that will receive the email",
                        required=True)
    args = parser.parse_args()

    UpdateInvoice().update_sheet()
    EmailUpdate(args.receiver).send()

if __name__ == "__main__":
    main()
from match_client import get_invoices_with_emails
from email_sender import send_invoice_email
from logger import log_email
from pathlib import Path

def main():
    print("Loading invoice data...")
    df = get_invoices_with_emails()

    for _, row in df.iterrows():
        client_name = row["client_name"]
        client_email = row["client_email"]
        invoice_number = row["invoice_number"]
        invoice_file = row["invoice_file"]

        invoice_path = Path(__file__).resolve().parents[1] / "data" / "invoices" / invoice_file

        try:
            send_invoice_email(
                to_email=client_email,
                client_name=client_name,
                invoice_number=invoice_number,
                invoice_path=invoice_path
            )
            log_email(client_name, client_email, invoice_number, "Success")

        except Exception as e:
            print(f"Failed to send invoice {invoice_number} to {client_email}: {e}")
            log_email(client_name, client_email, invoice_number, "Failed")

if __name__ == "__main__":
    main()
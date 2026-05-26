import smtplib
import ssl
from email.message import EmailMessage
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

print("USER:", os.getenv("EMAIL_USER"))
print("PASS:", os.getenv("EMAIL_PASS"))

def send_invoice_email(row):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")

    receiver_email = row["client_email"]
    client_name = row["client_name"]
    invoice_id = row["invoice_id"]
    file_name = row["file_name"]
    amount = row["amount"]

    invoice_path = "data/invoices/" + file_name

    if not os.path.exists(invoice_path):
        print("Missing PDF:", invoice_path)
        return False

    msg = EmailMessage()
    msg["Subject"] = "Invoice " + invoice_id
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.set_content(
        "Hi " + client_name + ",\n\n"
        "Please find attached your invoice " + invoice_id + ".\n"
        "Amount Due: $" + str(amount) + "\n\n"
        "Regards,\n"
        "Credit Team"
    )

    with open(invoice_path, "rb") as f:
        file_data = f.read()
        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="pdf",
            filename=file_name
        )

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)

        print("Sent:", invoice_id, "to", receiver_email)
        return True

    except Exception as error:
        print("Failed to send", invoice_id, ":", error)
        return False


def send_all_invoices():
    df = pd.read_csv("data/merged_output.csv")

    for index, row in df.iterrows():
        send_invoice_email(row)


send_all_invoices()
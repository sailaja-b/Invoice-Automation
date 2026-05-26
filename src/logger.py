import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path(__file__).resolve().parents[1] / "email_log.csv"

def log_email(client_name, client_email, invoice_number, status):
    file_exists = LOG_FILE.exists()

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        # Write header only once
        if not file_exists:
            writer.writerow(["timestamp", "client_name", "client_email", "invoice_number", "status"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            client_name,
            client_email,
            invoice_number,
            status
        ])

    print(f"Logged: {client_name} | {invoice_number} | {status}")
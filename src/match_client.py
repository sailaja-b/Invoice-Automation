import pandas as pd
from pathlib import Path

import pandas as pd

def load_clients():
    return pd.read_csv("data/clients.csv")

def load_invoices():
    return pd.read_csv("data/invoices.csv")

def get_invoices_with_emails():
    clients = load_clients()
    invoices = load_invoices()

    merged = invoices.merge(clients, on="client_id", how="left")
    return merged

# Run the merge
df = get_invoices_with_emails()
print(df)

# Save the merged file
df.to_csv("data/merged_output.csv", index=False)
print("Merged file saved to: data/merged_output.csv")
  

# Invoice-Automation

Problem: 
Finance teams often rely on manual steps to send invoices: checking CSV files, matching client IDs, attaching PDFs and sending emails individually.
This leads to delays, inconsistencies, and unnecessary workload.

Situation: 
The existing workflow required sending multiple invoices monthly, but the process was entirely manual.
There was no automated way to merge data, validate records or send emails in bulk.

Solution: 
I developed a Python automation system that:

Uses pandas to merge client and invoice datasets

Validates and cleans the data

Generates a single merged CSV output

Sends personalized invoice emails using SMTP

Attaches the correct PDF invoice for each client

Stores sensitive credentials in a .env file for security

This solution automates the entire workflow end‑to‑end, saving time and reducing human error.

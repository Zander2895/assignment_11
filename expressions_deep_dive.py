import re

def add_emails(existing_text, new_emails):
    updated_text = existing_text + ", " + ", ".join(new_emails)
    return updated_text

def extract_emails(text, exclude_domain):
    pattern = rf"\b[A-Za-z0-9._%+-]+@(?!{exclude_domain}\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    emails = re.findall(pattern, text)
    return emails

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

def interactive_add_emails():
    new_emails = []
    while True:
        new_email = input("Enter a new email address (or type 'done' to finish): ")
        if new_email.lower() == 'done':
            break
        new_emails.append(new_email)
    return new_emails

new_emails = interactive_add_emails()

updated_text = add_emails(text, new_emails)

exclude_domain = "exclude.com"
emails = extract_emails(updated_text, exclude_domain)

print("Extracted Emails:", emails)

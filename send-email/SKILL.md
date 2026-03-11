---
name: send-email
description: Send email through Gmail SMTP with optional file attachments. Use when the user wants to send an email, draft-and-send mail, or send a local file as an email attachment. Shared skill for agents on this machine; reads SMTP_USER and SMTP_PASS from a local env file.
---

# Send Email

Use the bundled Python script to send email through Gmail SMTP.

## Inputs

- `to_email`: recipient email address
- `subject`: subject line
- `body`: plain-text email body
- `attachment_path` (optional): absolute local file path to attach

## Procedure

1. Confirm the final recipient, subject, and body if the user has not already made them explicit.
2. Run `scripts/send_email.py` with the required flags.
3. If `attachment_path` is provided, pass it through unchanged and let the script validate it.
4. Report success or the exact failure.

## Command

From this skill directory, run:

```powershell
python .\scripts\send_email.py --to_email "<recipient>" --subject "<subject>" --body "<body>"
```

With attachment:

```powershell
python .\scripts\send_email.py --to_email "<recipient>" --subject "<subject>" --body "<body>" --attachment_path "C:\absolute\path\file.pdf"
```

## Notes

- The script reads credentials only from a local env file (not checked in).
- The env file must contain `SMTP_USER=` and `SMTP_PASS=`.
- Gmail SMTP host: `smtp.gmail.com`, port `587`, STARTTLS.
- Attachment path must be an existing absolute path.

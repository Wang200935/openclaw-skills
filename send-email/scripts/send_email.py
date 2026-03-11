import argparse
import mimetypes
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

ENV_PATH = Path(r"C:\Users\wang\.openclaw_email.env")
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


def load_env_file(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Env file not found: {path}")
    data = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        data[key.strip()] = value.strip()
    return data


def build_message(sender: str, to_email: str, subject: str, body: str, attachment_path: str | None) -> EmailMessage:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_path:
        p = Path(attachment_path)
        if not p.is_absolute():
            raise ValueError("attachment_path must be an absolute local path")
        if not p.exists() or not p.is_file():
            raise FileNotFoundError(f"Attachment not found: {p}")
        mime_type, _ = mimetypes.guess_type(str(p))
        if mime_type:
            maintype, subtype = mime_type.split("/", 1)
        else:
            maintype, subtype = "application", "octet-stream"
        with p.open("rb") as f:
            msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=p.name)
    return msg


def send_email(to_email: str, subject: str, body: str, attachment_path: str | None) -> None:
    env = load_env_file(ENV_PATH)
    smtp_user = env.get("SMTP_USER", "").strip()
    smtp_pass = env.get("SMTP_PASS", "").strip()
    if not smtp_user or not smtp_pass:
        raise RuntimeError("SMTP_USER or SMTP_PASS missing in env file")

    msg = build_message(smtp_user, to_email, subject, body, attachment_path)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send email with optional attachment via Gmail SMTP")
    parser.add_argument("--to_email", required=True)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--body", required=True)
    parser.add_argument("--attachment_path", required=False)
    args = parser.parse_args()

    send_email(
        to_email=args.to_email,
        subject=args.subject,
        body=args.body,
        attachment_path=args.attachment_path,
    )
    print("EMAIL_SENT")

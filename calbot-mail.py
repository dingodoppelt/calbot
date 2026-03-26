#!/usr/bin/env python3
import email
import sys
import subprocess
from email.policy import default
from dotenv import load_dotenv
import os

load_dotenv()
user = os.environ["user"]
password = os.environ["password"]
url = os.environ["url"]
allowed_sender = os.environ["allowed_sender"]
target_filename = os.environ["target_filename"]

def upload_bytes_with_curl(data: bytes):
    proc = subprocess.Popen(
        [
            "curl",
            "-k",
            "-u", f"{user}:{password}",
            "-X", "PUT",
            "-H", "Content-Type: text/calendar",
            "--data-binary", "@-",
            url
        ],
        stdin=subprocess.PIPE,
    )
    stdout, stderr = proc.communicate(input=data)
    if proc.returncode != 0:
        print("calling curl failed", file=sys.stderr)

def process_email():
    msg = email.message_from_binary_file(sys.stdin.buffer, policy=default)

    sender = msg['From']

    if allowed_sender.lower() not in sender.lower():
        print(f"Sender {sender} not known. Discarding email.", file=sys.stderr)
        return

    for part in msg.walk():
        if not part.get_content_type() == 'text/calendar':
            continue
        filename = part.get_filename()
        if filename and filename == target_filename:
            payload = part.get_payload(decode=True)
            upload_bytes_with_curl(payload)

if __name__ == "__main__":
    process_email()

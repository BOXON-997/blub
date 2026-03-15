#! /usr/bin/env python3
# Author: Smell my Tards
# -*- coding: latin-1 -*- 
# email_harvester project in python

import re 
import json
import sys

from pathlib import Path

EMAIL_REGEX = re.compile(r'''(?:(?:[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*)
|"(?:\\.|[^"\\])*")
@
(?:(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}
|\[(?:IPv6:[A-Fa-f0-9:]+|[0-9.]+)\])''',
re.IGNORECASE | re.VERBOSE
)

def extract_emails_from_files(file: str):
    try:
        with Path(file).open("r", encoding="utf-8") as f:
            contents = f.read()
    except (OSError, FileNotFoundError) as e:
        print(f"Error reading {file}: {e}")
        return []

    return [m.group(0) for m in EMAIL_REGEX.finditer(contents)]

def create_and_read_json_file(json_data):
    import os
    OUTPUT_DIR = Path(__file__).resolve().parent / "output"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    json_path = OUTPUT_DIR / "output.json"

    try:
        with json_path.open("w", encoding="utf-8") as jwriter:
            json.dump(json_data, jwriter, indent=4)

    except (OSError, FileNotFoundError) as e:
        print(f"Error saving {json_path}: {e}") 

    # Read saved JSON data below:

    try:
        with json_path.open("r", encoding="utf-8") as jreader:
            loaded_data = json.load(jreader)

            print(loaded_data)

    except (OSError, FileNotFoundError) as e:
        print(f"Error reading {json_path}: {e}")


if __name__ == "__main__":
    files = sys.argv[1:]

    if not files:
        print("Usage: python script.py <file1> <file2> ...")
        sys.exit(1)

    email_db = {}
    emails = []
    for file in files:
        emails.extend(extract_emails_from_files(file))

    count = 0
    for email in emails:
        email_key_format = f"Email address {count}"
        email_db[email_key_format] = email
        count += 1

    create_and_read_json_file(email_db)








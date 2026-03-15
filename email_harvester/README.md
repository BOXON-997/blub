# Email Harvester (Python)

A simple command-line Python tool that scans one or more text files, extracts email addresses using a robust regular expression, removes duplicates, and saves the results to a JSON file.

This project demonstrates practical usage of:

* Regular expressions (`re`)
* File handling
* JSON serialization (`json`)
* Command-line arguments (`sys.argv`)
* Path handling with `pathlib`

---

# Features

* Extracts email addresses from text files
* Supports multiple input files
* Removes duplicate emails automatically
* Saves results to a structured JSON file
* Creates an output directory automatically
* Prints extracted emails to the console

---

# Project Structure

```
email_harvester/
│
├── harvester.py
├── email_data.txt
└── output/
    └── output.json
```

| File                 | Description                                       |
| -------------------- | ------------------------------------------------- |
| `harvester.py`       | Main email harvesting script                      |
| `email_data.txt`     | Example input file containing emails              |
| `output/output.json` | Generated JSON output containing extracted emails |

---

# Requirements

* Python **3.8+**

No external dependencies are required.

---

# Installation

Clone the repository or download the script:

```
git clone https://github.com/yourusername/email-harvester.git
cd email-harvester
```

---

# Usage

Run the script and pass one or more files containing text:

```
python harvester.py <file1> <file2> ...
```

Example:

```
python harvester.py email_data.txt
```

You can also process multiple files:

```
python harvester.py file1.txt file2.txt logs.txt
```

---

# Example Output

Console output:

```
Found 3 unique email(s)

alice@example.com
bob@test.org
security@company.net
```

---

# JSON Output

The script generates a file:

```
output/output.json
```

Example:

```json
{
    "emails": [
        "alice@example.com",
        "bob@test.org",
        "security@company.net"
    ]
}
```

---

# How It Works

1. The script reads files provided via command-line arguments.
2. A regular expression scans file contents for valid email patterns.
3. Duplicate email addresses are removed.
4. Results are printed to the console.
5. Emails are saved to a JSON file for later use.

---

# Error Handling

The program gracefully handles:

* Missing files
* File read errors
* Invalid encodings

---

# Future Improvements

Possible upgrades include:

* Recursive directory scanning
* Multithreaded or multiprocessing file scanning
* CSV export
* Domain statistics
* CLI argument parsing using `argparse`
* Progress bars for large datasets
* Support for HTML parsing

---

# Educational Purpose

This project is intended as a learning exercise for:

* Python scripting
* Regex usage
* File system manipulation
* Data serialization

---

# License

MIT License

---

# Author

**Smell my Tards**

Python Developer


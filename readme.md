# WebLinkChecker

This script checks web links to see if they are valid. It prints out the HTTP status code for web requests made on each link.

# Getting Started

1. Clone repo
2. Create a virtual environment: ```python.exe -m venv /path/to/new/virtual/environment```
3. Install dependencies with: ```python.exe -m pip install -r requirements```

# Usage


```
Usage: python.exe webLinkChecker.py [OPTIONS] INPUT_FILE

Options:
  --status_code INTEGER  Specify what HTTP status code a response needs to be
                         for link to be printed out
  --help                 Show this message and exit.
  INPUT_FILE             A file containing links on seperate lines
```
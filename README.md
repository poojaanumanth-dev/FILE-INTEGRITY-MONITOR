# File Integrity Monitor

## Overview

The File Integrity Monitor is a Python-based cybersecurity project that monitors files inside a selected directory and detects unauthorized changes. It creates a baseline using SHA-256 hashes and continuously compares the current state of files against the baseline.

## Features

* Creates a baseline of file hashes
* Detects modified files
* Detects newly created files
* Detects deleted files
* Uses SHA-256 hashing for integrity verification
* Continuously monitors the selected directory

## Technologies Used

* Python 3
* hashlib
* os
* time
* datetime

## How It Works

1. The user selects a directory.
2. The program calculates the SHA-256 hash of every file.
3. These hashes become the baseline.
4. Every 10 seconds, the program scans the directory again.
5. If a file has changed, been deleted, or been added, the program reports the change.

## How to Run

1. Open Command Prompt.
2. Navigate to the project folder.

```bash
cd FILE-INTEGRITY-MONITOR
```

3. Run the program.

```bash
py App.py
```

4. Enter the directory you want to monitor.

Example:

```text
Enter directory to monitor:
C:\Users\Pooja\Documents\TestFolder
```

The program will continue monitoring the directory and display any detected changes.

## Example Output

```text
Creating baseline for: C:\Users\Pooja\Documents\TestFolder
Baseline created! Monitoring started...

Checking integrity...
✅ No changes detected.

Checking integrity...
🔴 MODIFIED: test.txt
🟢 NEW: report.pdf
❌ DELETED: notes.docx
```

## Future Improvements

* Save logs to a file
* Email notifications
* Real-time monitoring using watchdog
* GUI interface
* Export reports in CSV format

## Author

Pooja A

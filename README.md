Task 1:File-Integrity-Checker

COMPANY: CODTECH IT SOLUTIONS

NAME: RAYI NATASHA

INTERN ID: CT04DF12

DOMAIN: CYBER SECURITY AND ETHICAL HACKING

DURATION:4 WEEKS

MENTOR:NEELA SANTHOSH

OUTPUT:

![Image](https://github.com/user-attachments/assets/cbecdbdb-3285-4ebb-a274-5505abaf77c1)

## Project Overview

###  1. File Integrity Checker
- **Purpose**: Monitors a folder for changes using SHA-256 hashes.
- **Tech Used**: `hashlib`, `json`
- **Run**: Use Jupyter or VS Code to detect modified, added, or deleted files.

---> Description

This tool monitors changes in files by calculating and comparing SHA-256 hash values. It helps detect:

❌ Deleted files

⚠ Modified files

🔟 Newly added files

---> How to Run

Run the code in Jupyter Notebook or VS Code.

On first run, it creates a file (hashes.json) with SHA-256 hashes.

On second and subsequent runs, it compares hashes and alerts if any file is changed, removed, or added.

---> Inputs Required

Change the variable folder_to_monitor in the script:
folder_to_monitor = "test_files"
Replace test_files with the path of the folder you want to monitor.

##  How to Run All Projects
1. Clone or download this repository.
2. Open each `.ipynb` file in **Jupyter Notebook** or `.py` file in **VS Code**.
3. Follow instructions in each folder's `README.md`.

---

## Deployment Instructions
If submitting for review:
1. Ensure each project runs successfully.
2. Push to GitHub via terminal:
   ```bash
   git init
   git add .
   git commit -m 
   git remote add origin https://github.com/YourUsername/YourRepoName.git
   git push -u origin main

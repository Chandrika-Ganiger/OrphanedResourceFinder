
# Orphaned Resource Finder

## Introduction
Orphaned Resource Finder is a Python-based Azure cloud resource monitoring project that identifies potentially unused Azure resources.

## Problem Statement
Unused Azure resources can lead to unnecessary cloud expenses. Identifying these resources helps administrators monitor and manage cloud infrastructure efficiently.

## Objectives
- Identify unattached Azure managed disks.
- Identify unassociated Azure public IP addresses.
- Display associated and unassociated resources.
- Generate a CSV report of scanned resources.
- Help administrators review potentially unused resources.

## Technologies Used
- Microsoft Azure
- Python
- Azure SDK for Python
- Azure CLI
- Visual Studio Code
- Git and GitHub
- GitHub Actions

## Project Structure
```text
OrphanedResourceFinder/
├── src/
│   ├── azure_services.py
│   └── azure_connection.py
├── tests/
│   └── test_orphan_detection.py
├── reports/
│   └── orphaned_resources.csv
├── main.py
├── requirements.txt
└── README.md
```

## How It Works
1. Authenticates with Azure.
2. Retrieves managed disks and public IP addresses.
3. Checks their association status.
4. Identifies potential orphan candidates.
5. Generates a CSV report.

## Safety
This project uses read-only resource inspection. It does not automatically delete or modify Azure resources.

## Expected Outcome
A report containing associated resources and potential orphan candidates for further investigation.

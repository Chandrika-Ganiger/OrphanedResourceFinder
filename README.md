
# Orphaned Resource Finder

## 1. Introduction
Orphaned Resource Finder is a Python-based Azure monitoring tool that identifies potentially unused Azure cloud resources.

## 2. Problem Statement
Unused cloud resources can result in unnecessary costs. This project helps identify resources that may no longer be associated with active services.

## 3. Objectives
- Identify unattached Azure managed disks.
- Identify unassociated Azure public IP addresses.
- Display associated and potentially orphaned resources.
- Generate a CSV report.
- Provide a safe, read-only resource inspection approach.

## 4. Technologies Used
- Microsoft Azure
- Python
- Azure SDK for Python
- Azure CLI
- Visual Studio Code
- Git and GitHub
- GitHub Actions

## 5. Project Structure
```text
OrphanedResourceFinder/
├── src/
│   ├── azure_connection.py
│   └── azure_services.py
├── tests/
│   └── test_orphan_detection.py
├── reports/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 6. How It Works
1. Authenticates with Azure.
2. Retrieves managed disks and public IP addresses.
3. Checks their association status.
4. Identifies potential orphan candidates.
5. Generates a CSV report.

## 7. How to Run
Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Sign in to Azure:

```bash
az login
```

Run the project:

```bash
python main.py
```

## 8. Testing
Run the sample detection tests:

```bash
python tests/test_orphan_detection.py
```

## 9. Continuous Integration
GitHub Actions automatically runs the project tests when code is pushed to the main branch or a pull request is created.

## 10. Safety
The project identifies potential orphan candidates only. It does not automatically delete or modify Azure resources. Candidates must be reviewed before any cleanup decision.


## 11. Project Output

The Orphaned Resource Finder successfully connects to the Azure subscription and retrieves managed disks and public IP addresses.

The project displays:
- Attached and unattached managed disks.
- Associated and unassociated public IP addresses.
- Total counts of each resource category.
- Potential orphan candidates for further investigation.

It also generates a CSV report named `orphaned_resources.csv` in the `reports` folder. The report contains resource type, resource name, resource group, association status, IP address (where applicable), and resource ID.

The sample test data verifies the classification of both attached and unattached disks, and associated and unassociated public IP addresses.

## 12. Conclusion

The Orphaned Resource Finder provides a simple and effective way to identify potentially unused Azure managed disks and public IP addresses.

By using Python and the Azure SDK, the project automates resource inspection and generates a structured CSV report. GitHub Actions provides automated testing whenever code changes are pushed.

The project follows a read-only approach and does not automatically delete or modify resources. This helps administrators identify resources that require further review before taking cleanup decisions, supporting better cloud resource management and cost awareness.


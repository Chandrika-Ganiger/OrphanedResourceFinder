import csv
from pathlib import Path


import subprocess

from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

# Step 1: Get Azure subscription ID
subscription_id = subprocess.check_output(
    "az account show --query id -o tsv",
    shell=True,
    text=True
).strip()

# Step 2: Authenticate with Azure
credential = DefaultAzureCredential()

# Step 3: Connect to Azure services
compute_client = ComputeManagementClient(
    credential, subscription_id
)

network_client = NetworkManagementClient(
    credential, subscription_id
)

print("Connected to Azure successfully!")

# Step 4: Create separate lists for disks
attached_disks = []
unattached_disks = []

# Retrieve all managed disks
disks = compute_client.disks.list()

for disk in disks:
    if disk.managed_by is None:
        unattached_disks.append(disk)
    else:
        attached_disks.append(disk)

# Step 5: Create separate lists for public IPs
associated_ips = []
unassociated_ips = []

# Retrieve all public IP addresses
public_ips = network_client.public_ip_addresses.list_all()

for ip in public_ips:
    if ip.ip_configuration is None:
        unassociated_ips.append(ip)
    else:
        associated_ips.append(ip)

# Step 6: Display attached disks
print("\n========== ATTACHED DISKS ==========")

for disk in attached_disks:
    print("Disk name:", disk.name)
    print("Status: Attached")
    print("------------------------")

# Step 7: Display unattached disks
print("\n========== UNATTACHED DISKS ==========")

for disk in unattached_disks:
    print("Disk name:", disk.name)
    print("Status: Potential orphan candidate")
    print("------------------------")

# Step 8: Display associated public IPs
print("\n========== ASSOCIATED PUBLIC IPs ==========")

for ip in associated_ips:
    print("IP name:", ip.name)
    print("IP address:", ip.ip_address)
    print("Status: Associated")
    print("------------------------")

# Step 9: Display unassociated public IPs
print("\n========== UNASSOCIATED PUBLIC IPs ==========")

for ip in unassociated_ips:
    print("IP name:", ip.name)
    print("IP address:", ip.ip_address)
    print("Status: Potential orphan candidate")
    print("------------------------")

# Step 10: Final summary
print("\n========== FINAL SUMMARY ==========")

print("Attached disks:", len(attached_disks))
print("Unattached disks:", len(unattached_disks))
print("Associated public IPs:", len(associated_ips))
print("Unassociated public IPs:", len(unassociated_ips))

print("\nResource scan completed!")

# Step 11: Generate CSV report

report_folder = Path("reports")
report_folder.mkdir(exist_ok=True)

report_file = report_folder / "orphaned_resources.csv"

with open(report_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # CSV column headings
    writer.writerow([
        "Resource Type",
        "Resource Name",
        "Resource Group",
        "Status",
        "IP Address",
        "Resource ID"
    ])

    # Write disk information
    for disk in attached_disks:
        writer.writerow([
            "Managed Disk",
            disk.name,
            disk.id.split("/")[4],
            "Attached",
            "",
            disk.id
        ])

    for disk in unattached_disks:
        writer.writerow([
            "Managed Disk",
            disk.name,
            disk.id.split("/")[4],
            "Potential orphan candidate",
            "",
            disk.id
        ])

    # Write public IP information
    for ip in associated_ips:
        writer.writerow([
            "Public IP",
            ip.name,
            ip.id.split("/")[4],
            "Associated",
            ip.ip_address,
            ip.id
        ])

    for ip in unassociated_ips:
        writer.writerow([
            "Public IP",
            ip.name,
            ip.id.split("/")[4],
            "Potential orphan candidate",
            ip.ip_address,
            ip.id
        ])

print("\nCSV report generated successfully!")
print("Report location:", report_file)

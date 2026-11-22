
# Sample public IP resources for testing

public_ips = [
    {"name": "IP-Associated", "ip_configuration": "network-config-123"},
    {"name": "IP-Unassociated", "ip_configuration": None}
]

associated_ips = []
unassociated_ips = []

for ip in public_ips:
    if ip["ip_configuration"] is None:
        unassociated_ips.append(ip)
    else:
        associated_ips.append(ip)

print("ASSOCIATED PUBLIC IPs:")

for ip in associated_ips:
    print(ip["name"], "- Associated")

print("\nUNASSOCIATED PUBLIC IPs:")

for ip in unassociated_ips:
    print(ip["name"], "- Potential orphan candidate")

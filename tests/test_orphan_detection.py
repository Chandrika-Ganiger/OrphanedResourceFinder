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

# Verify the classification
assert len(associated_ips) == 1
assert len(unassociated_ips) == 1

assert associated_ips[0]["name"] == "IP-Associated"
assert unassociated_ips[0]["name"] == "IP-Unassociated"

print("All orphan detection tests passed!")
print("All orphan detection tests passed!")
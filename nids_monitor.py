from datetime import datetime

def detect_intrusion(source_ip, destination_ip, protocol, status):
    print("\n===== NETWORK INTRUSION DETECTION SYSTEM =====")
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("Source IP:", source_ip)
    print("Destination IP:", destination_ip)
    print("Protocol:", protocol)

    if status == "suspicious":
        print("ALERT: Suspicious activity detected!")
    else:
        print("Status: Normal network activity")

    print("=============================================")


# Sample test event
detect_intrusion(
    "192.168.1.10",
    "192.168.1.1",
    "TCP",
    "suspicious"
)

detect_intrusion(
    "192.168.1.15",
    "192.168.1.1",
    "UDP",
    "normal"
)
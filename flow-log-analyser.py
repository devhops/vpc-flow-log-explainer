def parse_flow_log(flow_log_entry):
    # Split the flow log entry into individual fields
    fields = flow_log_entry.split(" ")

    # Extract information from the fields
    version = fields[0]
    account_id = fields[1]
    network_interface_id = fields[2]
    source_ip = fields[3]
    destination_ip = fields[4]
    source_port = fields[5]
    destination_port = fields[6]
    protocol = fields[7]
    packets = fields[8]
    bytes_transferred = fields[9]
    start_time = fields[10]
    end_time = fields[11]
    action = fields[12]
    status = fields[13]

    # Convert protocol number to protocol name
    protocols = {"6": "TCP", "17": "UDP", "1": "ICMP"}
    protocol_name = protocols.get(protocol, "Unknown")

    # Convert timestamps to human-readable format
    import datetime
    start_time = datetime.datetime.fromtimestamp(int(start_time))
    end_time = datetime.datetime.fromtimestamp(int(end_time))

    # Construct the summary explanation
    summary = (
        f"Flow Log Version: {version}\n"
        f"Originating AWS Account ID: {account_id}\n"
        f"Network Interface ID: {network_interface_id}\n"
        f"Source IP: {source_ip}\n"
        f"Destination IP: {destination_ip}\n"
        f"Source Port: {source_port}\n"
        f"Destination Port: {destination_port}\n"
        f"Protocol: {protocol_name}\n"
        f"Packets Transferred: {packets}\n"
        f"Bytes Transferred: {bytes_transferred}\n"
        f"Start Time: {start_time}\n"
        f"End Time: {end_time}\n"
        f"Action: {action}\n"
        f"Status: {status}"
    )

    return summary

# Ask the user to input the flow log entry
flow_log_entry = input("Enter the flow log entry: ")

# Parse and print the summary explanation
summary = parse_flow_log(flow_log_entry)
print(summary)

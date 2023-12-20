import socket

# Define the monitoring station's IP address and port
monitoring_station_ip = '92.11.22.33'  # Replace with the monitoring station's IP address
monitoring_station_port = 2222  # Replace with the monitoring station's port

# Format your SIA-DC09 alarm event data
sia_dc09_event = '61E30137"SIA-DCS"0001L0#100001[#100001|Nri0/BA0001][https://download.samplelib.com/mp4/sample-5s.mp4$

# Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the monitoring station
tcp_socket.connect((monitoring_station_ip, monitoring_station_port))

# Send the SIA-DC09 alarm event data
tcp_socket.sendall(sia_dc09_event.encode())

# Close the socket
tcp_socket.close()

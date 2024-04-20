import star_scan.scanner as scanner

#
ip_address = '192.168.81.50'
start_port = 1
end_port = 1000
scanner.scan_host(ip_address, start_port, end_port)

#
scanner.scan_range(ip_address, start_port, end_port)
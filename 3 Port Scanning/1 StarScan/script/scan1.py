import star_scan.scanner as scanner

ip_address = '127.0.0.1'
start_port = 1
end_port = 1000
scanner.scan_host(ip_address, start_port, end_port)
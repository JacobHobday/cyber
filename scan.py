import socket 

def scan_port(target, port): 
    try: 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        sock.settimeout(1)
        result = sock.connect_ex((target, port)) 
        if result == 0: 
            print(f"Port {port} is open") 
            sock.close() 
    except socket.error: print(f"Couldn't connect to {target}") 

def scan_target(target): 
    print(f"Scanning target {target}") 
    for port in range(1, 1025): 
        scan_port(target, port)
    
if __name__ == "__main__": 
    target_ip = input("Enter target IP: ") 
    scan_target(target_ip)        
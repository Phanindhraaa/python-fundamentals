def parse_log_line(line):
    parts = line.split(" ")
    date = parts[0]
    level = parts[1].replace(":", "")
    message = " ".join(parts[2:])

    return {
        "date" : date,
        "level" : level,
        "message" : message
    }

print(parse_log_line("2024-06-01 ERROR: Something went wrong")) 

def apache_log_line(line):
    parts = line.split(" ")
    ip = parts[0]
    date = parts[3].strip("[]")
    method = parts[4]
    path = parts[5]
    status = parts[6]
    return {
        "ip": ip,
        "date": date,
        "method": method,
        "path": path,
        "status": status
    }

print(apache_log_line("192.168.1.1 - - [20/Dec/2025:10:30:45] GET /index.html 200"))

def parse_docker_log(line):
    parts = line.split(" ")
    time = parts[0]
    container_id = parts[1].split("=")[1]
    status = parts[2].split("=")[1]

    return {
        "time": time,
        "container_id": container_id,
        "status": status
    }

print(parse_docker_log("2025-12-20T10:30:45.123Z container_id=abc123 status=running"))

import json

def parse_json_line(line):
    data = json.loads(line)
    return data

print(parse_json_line('{"timestamp":"2025-12-20","level":"INFO","user":"admin","action":"login"}'))

def check_server_status(status_code):
    if status_code == 200:
        return "Healthy"
    elif status_code == 404:
        return "not found"
    elif status_code == 500:
        return "error"
    else:
        return "unknown"
    
print(check_server_status(200))  # Healthy
print(check_server_status(500))  



def validate_port(port):
    if 1 <= port <= 65535:
        return True
    return False
print(validate_port(8080))  # True  # error
print(validate_port(70000))  # False


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"
print(format_time(3661))  # 01:01:01


def check_disk_usage(used, total):
    usage_percent = (used / total) * 100
    if usage_percent < 70:
        return "Healthy"
    elif 70 <= usage_percent < 90:
        return "Warning"
    else:
        return "Critical"

print(check_disk_usage(500, 1000))  # Healthy   

    

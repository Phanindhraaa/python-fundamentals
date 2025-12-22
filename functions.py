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

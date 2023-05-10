import datetime
import random
import json
import os
import time
import requests


def err_source_generator():
    error_sources = [
        "com.example.MyClass",
        "com.example.MyController",
        "com.example.MyService",
        "com.example.MyApplication"
    ]
    return random.choice(error_sources)


def err_message_generator():
    error_messages = [
        "Invalid input",
        "Unexpected error occurred",
        "Service temporarily unavailable",
        "Database connection failed",
        "Resource not found",
        "Unauthorized access",
        "Request timeout exceeded",
        "Internal server error"
    ]
    return random.choice(error_messages)


def err_type_generator():
    error_types = [
        "ObjectNull",
        "OutOfMemoryError",
        "IllegalArgumentException",
        "IllegalStateException",
        "ClassCastException",
        "NullPointerException",
        "Undefined object error",
        "DateTimeException",
        "SecurityException",
    ]

    return random.choice(error_types)


def generate_error_message():
    http_error_codes = [400, 401, 403, 404, 500, 502, 503, 504]

    num_lines = random.randint(4, 12)
    lines = []

    for i in range(num_lines):
        code_line = random.randint(15, 180)

        if i == 0:
            error_code = random.choice(http_error_codes)
            lines.append(
                f"ERROR {error_code}: {err_message_generator()} {err_type_generator()} at {err_source_generator()} line {code_line}")
        else:
            lines.append(
                f"{err_type_generator()} at {err_source_generator()} line {code_line} {err_message_generator()}")

    return " ".join(lines)


def log_generator():
    log_levels = ["WARNING", "INFO", "DEBUG", "ERROR"]
    log_level = random.choice(log_levels)

    if log_level == "ERROR":
        log_message = generate_error_message()
    else:
        log_message = f"This is a {log_level} level log message."

    log = {
        "timestamp": (datetime.datetime.now(datetime.timezone.utc).isoformat()),
        "log_level": log_level,
        "log_message": log_message
    }
    json_log = json.dumps(log)
    return json_log


def log_sender(log, session, url):
    headers = {'Content-Type': 'application/json'}
    response = session.post(url, data=log, headers=headers)
    if response.ok:
        print('Logs sent successfully.')
    else:
        print('Error sending logs:', response.text)


def main():
    url = os.environ.get('ELASTIC_URL')
    log_duration = os.environ.get('LOG_DURATION')
    with requests.Session() as session:
        while True:
            try:
                base_url = url.split('/', 3)[:3]
                base_url = '/'.join(base_url)
                response = session.get(base_url)
                if response.status_code == 200:
                    log = log_generator()
                    print(log)
                    log_sender(log, session, url)
                else:
                    print('Error getting URL:', url)
            except requests.exceptions.RequestException as e:
                print('Error while attempting to reach the Elastic endpoint. Please check the Elastic endpoint:',
                      base_url, e)
            if log_duration is not None:
                duration = int(log_duration)
                time.sleep(duration)


if __name__ == '__main__':
    main()

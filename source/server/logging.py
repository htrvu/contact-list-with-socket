import datetime

log_file_path = 'log.txt'
log_queue = []

def set_log_file_path(path):
    global log_file_path
    log_file_path = path

def log(message):
    global log_queue
    current_time = datetime.now().strftime("%b %d %Y %H:%M:%SS")
    log_queue.append(f'{current_time} {message}')

def save():
    global log_queue

    with open(log_file_path, 'a') as fp:
        fp.writelines(log_queue)

    log_queue = []
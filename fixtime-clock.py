import time

def start_timer():
    """Starts a 10-minute timer."""
    duration = 10
    print(f'Starting {duration} minute timer...')
    time.sleep(duration * 60)
    print('Time is up!')

if __name__ == '__main__':
    start_timer()

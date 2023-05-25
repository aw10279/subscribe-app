import time

def start_timer(duration):
    """Starts a timer for the specified duration in minutes."""
    print(f'Starting {duration} minute timer...')
    time.sleep(duration * 60)
    print('Time is up!')

if __name__ == '__main__':
    duration = int(input('How many minutes do you want to focus for? '))
    start_timer(duration)

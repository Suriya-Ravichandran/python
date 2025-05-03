import sys
import time
import itertools

def loading_animation(message="Loading", duration=5):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(f'\r{message} {next(spinner)}')
        sys.stdout.flush()
        time.sleep(0.1)    

def progress_bar(total, prefix='Logout', length=40, fill='█'):
    for i in range(total + 1):
        percent = int(100 * (i / total))
        filled_length = int(length * i // total)
        bar = fill * filled_length + '-' * (length - filled_length)
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}%')
        sys.stdout.flush()
        time.sleep(0.05)  # Simulate work





# # Example usage
# if __name__ == "__main__":
#     loading_animation("Fetching Dog Faces", duration=4)

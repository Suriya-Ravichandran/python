# # import os
# import platform
# # os.remove("hello.py")
# # print(os.uname())

# print(platform.system())
# print(platform.processor())

# import psutil
# import time
# import os

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

# try:
#     while True:
#         clear_screen()
#         print(f"{'PID':<10} {'Name':<25} {'CPU %':>10}")
#         print("-" * 50)

#         # Refresh CPU percent stats
#         for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
#             try:
#                 print(f"{proc.info['pid']:<10} {proc.info['name'][:25]:<25} {proc.info['cpu_percent']:>10.2f}")
#             except (psutil.NoSuchProcess, psutil.AccessDenied):
#                 continue

#         time.sleep(1)  # update every second

# except KeyboardInterrupt:
#     print("\nExiting...")

# import os 

# os.kill(2560)

import psutil

def kill_chrome_processes():
    chrome_killed = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'chrome' in proc.info['name'].lower():
                print(f"Killing PID {proc.info['pid']}: {proc.info['name']}")
                psutil.Process(proc.info['pid']).terminate()  # or use .kill() for force kill
                chrome_killed += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    if chrome_killed == 0:
        print("No Chrome processes found.")
    else:
        print(f"Killed {chrome_killed} Chrome process(es).")

kill_chrome_processes()


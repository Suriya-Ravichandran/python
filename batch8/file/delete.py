# import os

# # os.remove("Hello.txt")

# print(os.name)


import platform

print(platform.system())        # OS name (e.g., 'Windows', 'Linux', 'Darwin')
print(platform.release())       # OS version/release (e.g., '10', '5.15.0-75-generic')
print(platform.version())       # Detailed version string
print(platform.machine())       # Machine type (e.g., 'x86_64')
print(platform.processor())     # Processor info

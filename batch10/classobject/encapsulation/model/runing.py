import os
import time

# ASCII frames of a dog running (very simplified)
frames = [
    r"""
    __      _
o'')}____//
 `_/      )
 (_(_/-(_/
""",
    r"""
     __     _
o'')}____//
 `_/     )
 (_(_/-(_/
""",
    r"""
      __    _
o'')}____//
 `_/    )
 (_(_/-(_/
"""
]

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Animate
try:
    while True:
        for frame in frames:
            clear()
            print(frame)
            time.sleep(0.2)
except KeyboardInterrupt:
    clear()
    print("Animation stopped.")

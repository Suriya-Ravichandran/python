import pyfiglet
import random

class InstagramBanner:
    # ANSI color codes
    COLORS = [
        "\033[31m",  # Red
        "\033[32m",  # Green
        "\033[33m",  # Yellow
        "\033[34m",  # Blue
        "\033[35m",  # Magenta
        "\033[36m",  # Cyan
        "\033[91m",  # Bright Red
        "\033[92m",  # Bright Green
        "\033[93m",  # Bright Yellow
        "\033[94m",  # Bright Blue
        "\033[95m",  # Bright Magenta
        "\033[96m",  # Bright Cyan
    ]

    RESET = "\033[0m"  # Resets the color

    def display_banner(self):
        # Generate ASCII banner
        ascii_banner = pyfiglet.figlet_format("Instagram")

        # Pick a random color
        color = random.choice(self.COLORS)

        # Print colored banner
        print(f"{color}{ascii_banner}{self.RESET}")

# # Run the banner display
# if __name__ == "__main__":
#     banner = InstagramBanner()
#     banner.display_banner()


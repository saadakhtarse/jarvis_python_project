import subprocess
import sys

def turn_wifi_on():
    try:
        if sys.platform.startswith('win'):  # For Windows
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=enable"], check=True)
        elif sys.platform.startswith('darwin'):  # For macOS
            subprocess.run(["networksetup", "-setairportpower", "en0", "on"], check=True)
        elif sys.platform.startswith('linux'):  # For Linux
            subprocess.run(["nmcli", "radio", "wifi", "on"], check=True)
        else:
            print("Unsupported platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

def turn_wifi_off():
    try:
        if sys.platform.startswith('win'):  # For Windows
            subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", "admin=disable"], check=True)
        elif sys.platform.startswith('darwin'):  # For macOS
            subprocess.run(["networksetup", "-setairportpower", "en0", "off"], check=True)
        elif sys.platform.startswith('linux'):  # For Linux
            subprocess.run(["nmcli", "radio", "wifi", "off"], check=True)
        else:
            print("Unsupported platform.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Example usage
# turn_wifi_on()  # Turn on Wi-Fi
# turn_wifi_off()  # Turn off Wi-Fi

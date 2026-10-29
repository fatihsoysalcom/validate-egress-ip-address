import urllib.request
import urllib.error

def get_public_egress_ip():
    """
    Fetches the public egress IP address of the machine running this script.
    This simulates an application making an outbound connection to a third-party service.
    """
    ip_check_url = "https://icanhazip.com/" # A simple service that returns the client's IP address

    print(f"Attempting to determine the public egress IP by connecting to: {ip_check_url}")
    try:
        # Make an HTTP GET request to the external service.
        # The source IP of this request is the egress IP of the machine.
        with urllib.request.urlopen(ip_check_url, timeout=5) as response:
            public_ip = response.read().decode('utf-8').strip()
            return public_ip
    except urllib.error.URLError as e:
        print(f"Error fetching IP: {e.reason}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    current_egress_ip = get_public_egress_ip()

    if current_egress_ip:
        print(f"\n--- Egress IP Validation ---")
        print(f"The public egress IP address of this machine is: {current_egress_ip}")

        # The article mentions 104.28.152.116 as an example IP for validation.
        # This part simulates checking if the current egress IP matches a whitelisted IP.
        expected_whitelisted_ip = "104.28.152.116"
        print(f"Expected (whitelisted) IP address from the article: {expected_whitelisted_ip}")

        if current_egress_ip == expected_whitelisted_ip:
            print(f"Validation SUCCESS: The current egress IP matches the expected whitelisted IP.")
        else:
            print(f"Validation FAILED: The current egress IP ({current_egress_ip}) does NOT match the expected whitelisted IP ({expected_whitelisted_ip}).")
            print(f"This could indicate a network configuration change or an unexpected egress route.")
    else:
        print("Could not determine the public egress IP address.")
        print("Please check your internet connection or firewall settings.")

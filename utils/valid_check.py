import re

def check_valid_url(url):
    """
    Check if the given URL is valid.

    : url [list]:    The URL string to check
    : return [Boolean]: True if the URL is valid, otherwise False
    """
    # Define the regular expression for a valid URL
    url_regex = re.compile(
        r'^(https?|ftp):\/\/'  # Protocol (http, https, ftp)
        r'(([A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # Domain name
        r'localhost|'  # Localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # Or IPv4 address
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # Or IPv6 address
        r'(?::\d+)?'  # Optional port number
        r'(\/?|[\/?]\S+)$', re.IGNORECASE)  # Path

    # Use the regular expression to match the given URL
    return re.match(url_regex, url) is not None
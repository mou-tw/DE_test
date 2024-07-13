
import requests
import time

def request_with_retries(url, headers = {}):
    """
    Request a URL with up to three retries if the status code is not 200.
    Waits for 5 seconds between each retry. Raises an error if all retries fail.

    :param url: The URL to request
    :param headers: headers used to request
    :return: The response object if the request is successful
    :raises: Exception if the request fails after three retries
    """
    c = 1  
    wait_time = 5  # seconds


    while c <= 3:
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response
            else:
                print(f"Attempt {c}: Status code {response.status_code}")
        except requests.RequestException as e:
            print(f"Attempt {c}: Request failed with exception {e}")

        print(f"Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)
        c+=1
    
    raise Exception(f"Failed to get a successful response from {url} after {c} retries.")

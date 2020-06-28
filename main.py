from data_structures.datacenter import Datacenter
import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    try:
        s = requests.Session()
        retries = Retry(total=max_retries, backoff_factor=delay_between_retries)
        a = HTTPAdapter(max_retries=retries)
        s.mount(url, a)
        payload = {'timeout': 1}
        response = s.get(url, params=payload)
        data = response.json()
        return data
    except requests.ConnectionError as e:
        print("Error connecting to endpoint: ", e)
    except json.decoder.JSONDecodeError as e:
        print("Error getting data: ", e)
    except Exception as e:
        print("Error: ", e)


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]


if __name__ == '__main__':
    main()

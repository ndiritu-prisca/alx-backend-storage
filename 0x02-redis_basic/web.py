#!/usr/bin/env python3
"""A module for get_page"""

import requests
import redis


def get_page(url: str) -> str:
    """
    A function that uses the requests module to obtain the HTML content of a
    particular URL and returns it.
    """
    client = redis.Redis()

    count_key = f"count:{url}"

    access_count = client.get(count_key)
    if access_count is None:
        client.set(count_key, 1, ex=10)  
    else:
        access_count = int(access_count.decode('utf-8'))
        access_count += 1
        client.set(count_key, access_count, ex=10)

    response = requests.get(url)

    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to fetch content from {url}"

# Example usage
if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/https://example.com"
    html_content = get_page(url)
    print(f"HTML Content for {url}:\n{html_content}")

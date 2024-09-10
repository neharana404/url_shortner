# -*- coding: utf-8 -*-
import requests


class Codec:
    """
    This class uses the TinyURL API for URL shortening.

    I chose TinyURL because it is a simple, reliable, and free API that doesn't require an API key for basic usage but requires an API key for some of its advanced features.
    It's widely used, has minimal setup, and provides direct access to the short URL through a simple GET request.
    """

    def __init__(self):
        # Dictionary to store short and long URLs
        self.url_dict = {}

    # This method encodes (shortens) a long URL using the TinyURL API
    def encode(self, long_url: str) -> str:
        # Check if the long URL is already encoded
        for short_url, url in self.url_dict.items():
            if url == long_url:
                return short_url  # If the URL is already in the dictionary, return the existing short URL

        # Make API request to TinyURL to shorten the URL
        try:
            api_url = f'http://tinyurl.com/api-create.php?url={long_url}'
            response = requests.get(api_url)

            # Check if the API request was successful
            if response.status_code == 200:
                short_url = response.text  # The response text is the shortened URL

                # Store the long URL and short URL in the dictionary
                self.url_dict[short_url] = long_url
                return short_url
            else:
                print("Error: Could not shorten the URL")
                return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    # This method decodes (returns the original URL from) a short URL
    def decode(self, short_url: str) -> str:
        return self.url_dict.get(short_url, None)


# Example usage
codec = Codec()

long_urls = [
    "https://www.ssctech.com/solutions/client-communications",
    "https://www.github.com",
    "https://www.nytimes.com",
    "https://www.stackoverflow.com",
    "https://www.wikipedia.org"
]

for long_url in long_urls:
    short_url = codec.encode(long_url)
    decoded_url = codec.decode(short_url)

    print(f"Original URL: {long_url}")
    print(f"Short URL: {short_url}")
    print(f"Decoded URL: {decoded_url}")
    print("-" * 30)

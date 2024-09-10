# -*- coding: utf-8 -*-
import random

class Codec:
    def __init__(self):
        # Dictionary to store short and long URLs
        self.url_dict = {}
        self.string_length = 6  # Shortened URL will be 6 characters long
        self.letters = ('abcdefghijklmnopqrstuvwxyzABCDEF'
                        'GHIJKLMNOPQRSTUVWXYZ0123456789')

    # This method generates a unique short URL
    def generate_short_url(self):
        # ISSUE: The original version could lead to infinite recursion if a duplicate short URL was generated.
        # FIX: Added a loop to ensure the generated short URL is unique without recursion.

        while True:
            short_url = ''.join(random.choice(self.letters) for _ in range(self.string_length))
            if short_url not in self.url_dict:
                return short_url

    # This method encodes (shortens) a long URL
    def encode(self, long_url: str) -> str:
        # ISSUE: The original version incorrectly handled URL overwriting and had a typo in the function call.

        # The typo in the original version of the encode method was that the code tried to call generate_short_url() without referencing self.
        # In Python, when calling a method inside a class, you need to use self.method_name() to refer to that method within the instance.
        # The original code was simply calling generate_short_url(), which would raised a NameError because the method was not correctly referenced.

        # FIX: Check if the long URL already exists and return its short URL. Otherwise, generate and store a new one.

        # Check if the long URL is already encoded
        for short_url, url in self.url_dict.items():
            if url == long_url:
                return short_url  # If the URL is already in the dictionary, return the existing short URL

        # Generate new short URL and store it
        short_url = self.generate_short_url()
        self.url_dict[short_url] = long_url
        return short_url

    # This method decodes (returns the original URL from) a short URL
    def decode(self, short_url: str) -> str:
        # ISSUE: The original version could throw an error if the short URL wasn't found.
        # FIX: Return None if the short URL doesn't exist instead of throwing an error.

        return self.url_dict.get(short_url, None)


# Example usage
codec = Codec()

# Test encoding and decoding with 1000 URLs

for i in range(5): # Change 5 to 1000
    long_url = f"http://ssc.com/{i}"
    short_url = codec.encode(long_url)
    decoded_url = codec.decode(short_url)

    print(f"Original URL: {long_url}")
    print(f"Short URL: {short_url}")
    print(f"Decoded URL: {decoded_url}")
    print("-" * 30)

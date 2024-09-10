# URL Shortener Service with TinyURL API Integration

This project implements a URL shortening service that uses the **TinyURL** API to generate short URLs from long URLs. The service stores both the original and shortened URLs in memory for later retrieval. The project demonstrates how to integrate a third-party API for URL shortening and provides an example of encoding and decoding URLs using Python.

## Features
- Uses the **TinyURL** API to shorten URLs.
- Encodes (shortens) long URLs and stores them in memory.
- Decodes shortened URLs back to their original form.
- Tested with real-world URLs.

## Why TinyURL API?
The **TinyURL** API was chosen because:
- It's simple and reliable for basic URL shortening.
- No API key is required for the basic service.
- It supports a straightforward GET request to generate short URLs.

## Prerequisites
You will need Python 3.x installed on your machine.

The project uses the `requests` package to make HTTP requests. Install it using the steps below.

## Setup

1. **Clone the repository** or download the files to your local machine.
   
2. **Install dependencies**:

   First, navigate to the project directory and run the following command to install the required package:

   ```bash
   pip install -r requirements.txt

3. **You can run the project by executing the Python script in the terminal:**
   
   ```bash
    python question_1.py
    python question_2.py

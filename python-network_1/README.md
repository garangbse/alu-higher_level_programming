# Python Network #1

Scripts to handle HTTP requests and responses using `requests` and `urllib` packages in Python.

### 0-hbtn_status.py
- Fetches URL: https://alx-intranet.hbtn.io/status using `urllib` package
- Shows different ways to manipulate response data
- Displays response type, content, and UTF-8 content

### 1-hbtn_header.py
- Takes URL as argument and sends request using `urllib`
- Displays `X-Request-Id` value from response header
- Handles URL parsing and header extraction

### 2-post_email.py
- Sends POST request to URL with email parameter
- Takes URL and email as command line arguments
- Displays response body decoded in UTF-8

### 3-error_code.py
- Sends request to URL and handles HTTP error codes
- Uses `urllib.error` to manage exceptions
- Prints error code if request fails

### 4-hbtn_status.py
- Fetches URL using `requests` package
- Shows response format with `requests` library
- Displays response type and content

### 5-hbtn_header.py
- Gets `X-Request-Id` from response header using `requests`
- Takes URL as command line argument
- Simpler implementation than urllib version

### 6-post_email.py
- POST request with email parameter using `requests`
- Takes URL and email as arguments
- Shows response body text

### 7-error_code.py
- Handles HTTP errors with `requests`
- Prints error code for failed requests
- Uses status_code attribute of response

### 8-json_api.py
- Sends POST request with letter parameter
- Processes JSON response
- Handles different response cases

### 10-my_github.py
- Uses Github API to display user ID
- Authenticates using Basic Authentication
- Takes username and token as arguments

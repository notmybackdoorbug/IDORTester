import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = ""
resource_path = ""
valid_record_id = ""
test_record_id = ""
raw_cookies = ""

def defineVars():
    # Replace these variables with actual values
    base_url = input("Define base_url: ")  # Base URL of the APEX application
    resource_path = input("Define resource_path: ")  # Resource path of APEX page
    valid_record_id = input("Define a VALID record id: ")  # A valid record ID that belongs to the authenticated user
    test_record_id = input("Define a NON VALID/TEST record id: ") # A record ID to test for IDOR (not owned by the authenticated user)
    raw_cookies = input("Define Cookies: ")

def check_idor(record_id):
    session = requests.Session()
    # Ask the user for cookies (key=value format)
    
    # Convert raw cookies into a dictionary
    cookies = {}
    for cookie in raw_cookies.split(";"):
        key, value = cookie.strip().split("=")
        cookies[key] = value

    session.cookies.update(cookies)

    """Check if we can access a resource with a given ID."""
    url = f"{base_url}/f?p=103:{record_id}:2502149361534:::85::"
    response = session.get(url, verify=False)

    if response.status_code == 200:
        print(f"Record {record_id} is accessible. Possible IDOR vulnerability!")
        print(f"Response: {response.text[:500]}")  # Print part of the response (first 100 chars)
    else:
        print(f"Record {record_id} is not accessible. No IDOR detected.")

def test_idor():
    """Test with valid and test records."""
    print(f"Testing with valid record ID: {valid_record_id}")
    check_idor(valid_record_id)

    print(f"\nTesting with test record ID: {test_record_id}")
    check_idor(test_record_id)

if __name__ == "__main__":
    defineVars();
    test_idor()
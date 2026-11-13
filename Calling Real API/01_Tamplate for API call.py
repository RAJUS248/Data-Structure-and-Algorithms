# API call real time tamplate
# with free api url only

import requests

def api_call():
      
    try:

        url = "PUBLIC_API_URL"
        
        response = requests.get(url).json()

        return response

    except Exception:
        return None


res = api_call()

if res:
    print(res.keys())
    # Extract required information here

else:
    print("API error")



# with api key

import requests

def api_call():

    try:

        api_key = "YOUR_API_KEY"

        url = f"API_URL?key={api_key}"

        response = requests.get(url).json()

        return response

    except Exception:
        return None


res = api_call()

if res:
    print(res.keys())
    # Extract required information here

else:
    print("API error")


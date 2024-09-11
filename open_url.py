import requests

def open_url():
    url = "https://navigation.xunda.nyc.mn/"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully opened {url}")
        else:
            print(f"Failed to open {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    open_url()

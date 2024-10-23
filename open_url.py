import requests

def open_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully opened {url}")
        else:
            print(f"Failed to open {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while opening {url}: {e}")

if __name__ == "__main__":
    urls = [
        "https://navigation.xunda.nyc.mn/",
        "https://boke.xunda.nyc.mn/"
       
    ]
    
    for url in urls:
        open_url(url)

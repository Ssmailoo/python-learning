import requests

def test_post():
    url = "https://httpbin.org/post"
    
    data = {
        "nama": "Ismail",
        "kota": "Makassar",
        "tujuan": "AI Engineer"
    }
    
    response = requests.post(url, json=data)
    
    print(f"Status: {response.status_code}")
    print(f"Data yang dikirim: {response.json()['json']}")

test_post()
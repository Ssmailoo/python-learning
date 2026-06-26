'''import requests

def ambil_profil_github(username):
    try:
        response = requests.get(f"https://api.github.com/users/{username}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"Username: {data['login']}")
            print(f"Public Repos: {data['public_repos']}")
            print(f"Followers: {data['followers']}")
            print(f"Following: {data['following']}")
        elif response.status_code == 404:
            print("User tidak ditemukan")
        else:
            print(f"Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("Tidak ada koneksi internet")

ambil_profil_github("Ssmailoo")'''

import requests

username = "Ssmailoo"

url = f"https://api.github.com/users/{username}"

response = requests.get(url)

print(response.status_code)
print(response.text)

data = response.json()

profile = {
    "login": data['login'],
    "company": data['company'] or "Tidak ditentukan",
    "location": data['location'] or "Tidak ditentukan",
    "html_url": data['html_url']
}

print("Username:", profile['login'])
print("Company:", profile['company'])
print("Lokasi:", profile['location'])
print("GitHub:", profile['html_url'])
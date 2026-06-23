import requests

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

ambil_profil_github("Ssmailoo")

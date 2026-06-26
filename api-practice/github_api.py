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
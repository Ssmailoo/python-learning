import json

data = {
    "username": "Ssmailoo",
    "public_repos": 1,
    "followers": 0
}

with open("api-practice/github_data.json", "w") as f:
    json.dump(data, f, indent=2)

print("Data berhasil disimpan")

with open("api-practice/github_data.json", "r") as f:
    loaded = json.load(f)

print(f"Data berhasil dimuat: {loaded['username']}")
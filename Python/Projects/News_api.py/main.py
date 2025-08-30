import requests
query = input("What are you intereseted to read today? \n")
api ="2cccd47249c446a3211245065e"
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-06-06&sortBy=publishedAt&apiKey={api}"
print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]
for index, article in enumerate(articles):
    print(index+1,article["title"], article["url"])
    print("\n********************************\n")
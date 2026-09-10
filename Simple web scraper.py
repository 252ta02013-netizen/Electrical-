import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    print("\n===== PAGE TITLE =====")

    print(soup.title.string if soup.title else "No title")

    print("\n===== HEADINGS =====")

    for heading in soup.find_all(["h1", "h2", "h3"]):
        print(heading.get_text(strip=True))

else:
    print("Unable to access website.")

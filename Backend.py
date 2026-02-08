import requests
from bs4 import BeautifulSoup

url = "https://www.investor.gov/protect-your-investments/fraud/how-avoid-fraud/red-flags-investment-fraud-checklist"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

article = soup.find("article", class_="node--type-page")

red_flags = []

# Find images by ALT text (this is the key fix)
for img in article.find_all("img", alt="small red flag"):
    p = img.find_parent("p")
    if p:
        img.extract()  # remove icon
        text = p.get_text(strip=True)
        if text:
            red_flags.append(text)

for i, flag in enumerate(red_flags, 1):
    print(f"{i}. {flag}")


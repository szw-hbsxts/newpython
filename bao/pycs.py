import requests
url = "https://www.aoopuff.com/products/gray-solid-crew-neck-long-sleeve-sweatshirts-1"

html = requests.get(url)

print(html)
print(html.text)

from bs4 import BeautifulSoup
import requests

# 1. ویب سائٹ کا لنک
url = "https://quotes.toscrape.com/"

# 2. ویب سائٹ سے پیج کا ڈیٹا منگوانا
response = requests.get(url)

# 3. چیک کرنا کہ ریکوئسٹ کامیاب رہی یا نہیں (Status Code 200 کا مطلب کامیابی ہے)
if response.status_code == 200:
  # 4. ایچ ٹی ایم ایل کو پارس کرنا
  soup = BeautifulSoup(response.text, "html.parser")

  # 5. تمام اقوال اور مصنفین کو تلاش کرنا
  # اس ویب سائٹ پر ہر قول 'div' جس کی کلاس 'quote' ہو کے اندر ہوتا ہے
  quotes_divs = soup.find_all("div", class_="quote")

  print("--- ویب سائٹ سے نکالے گئے اقوال ---\n")

  # 6. ایک ایک کرکے ہر قول اور مصنف کو الگ کرنا اور پرنٹ کرنا
  for index, item in enumerate(quotes_divs, 1):
    # قول کا متن
    quote_text = item.find("span", class_="text").text
    # مصنف کا نام
    author = item.find("small", class_="author").text

    print(f"{index}. قول: {quote_text}")
    print(f"   مصنف: {author}")
    print("-" * 50)

else:
  print(
      f"ویب سائٹ ڈیٹا حاصل کرنے میں ناکام رہی۔ اسٹیٹس کوڈ: {response.status_code}"
  )
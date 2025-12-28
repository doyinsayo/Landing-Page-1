from requests_html import HTMLSession
import json
import time

# Initialize an HTML session (renders JavaScript)
session = HTMLSession()

# Blog homepage and fallback articles
BASE_URL = "https://www.mechaniconthego.com.ng"
START_ARTICLES = [
    "https://www.mechaniconthego.com.ng/blog/4187f246-ceef-48ca-8ea5-81ed955f6ea7",
    "https://www.mechaniconthego.com.ng/blog/45bc5622-0c53-4cf4-ab07-37ddebe66654",
    "https://www.mechaniconthego.com.ng/blog/7473eb27-2e65-4664-8222-882713c0ed0d",
    "https://www.mechaniconthego.com.ng/blog/99bbc314-9395-4136-9a60-92de363b94d3",
    "https://www.mechaniconthego.com.ng/blog/be071d3e-a3d5-4bda-a464-757ec5a3281c",
    "https://www.mechaniconthego.com.ng/blog/d601b893-7b09-4ae9-abb9-656bc3f8cdba",
    "https://www.mechaniconthego.com.ng/blog/e65ec6f0-5f80-4a5b-956d-c0b6e01718f1",
    "https://www.mechaniconthego.com.ng/blog/f7e0762e-0ee5-4909-b1be-89368dd3b027",
    "https://www.mechaniconthego.com.ng/blog/a26fee1d-dc03-4c71-a9f7-f6d9b9165e0e",
    "https://www.mechaniconthego.com.ng/blog/caebd52b-6eaa-41a8-a6d0-4f67d9939b2b",
    "https://www.mechaniconthego.com.ng/blog/7ac378ed-aba6-45bd-9386-6a4df163f1b6",
    "https://www.mechaniconthego.com.ng/blog/a1c450ed-3ae7-495b-af7d-0664db0722c0",
    "https://www.mechaniconthego.com.ng/blog/84837bf3-24f2-4108-8787-a2247e3a2f50",
    "https://www.mechaniconthego.com.ng/blog/be77bfa8-c80e-48b9-a1d5-9d4459e02e68",
    "https://www.mechaniconthego.com.ng/blog/bf0c0972-959f-4284-a732-95ffdfb232ed",
    "https://www.mechaniconthego.com.ng/blog/789f3bec-f9b4-443e-a7a3-87a088096683",
    "https://www.mechaniconthego.com.ng/blog/632e2de8-38c7-4e44-afef-f81fa1ae9fbf",
    "https://www.mechaniconthego.com.ng/blog/933b7ba8-5d8d-4d7c-9765-e2a9b44eba70",
    "https://www.mechaniconthego.com.ng/blog/a063668e-0d7e-4c6b-8e97-b2a566208ee4",
    "https://www.mechaniconthego.com.ng/blog/5f78f5e6-72a6-4394-bdca-666eec068e9e",
    "https://www.mechaniconthego.com.ng/blog/951874e2-1c33-46c2-8b28-ac621671a4f3",
    "https://www.mechaniconthego.com.ng/blog/a0b91e66-6832-4783-8ac8-7744bb129f42",
    "https://www.mechaniconthego.com.ng/blog/a50dbc37-6945-4d92-9c36-8256812fc803",
    "https://www.mechaniconthego.com.ng/blog/a8500542-12a9-4ff7-8bbe-f8638372aba2",
    "https://www.mechaniconthego.com.ng/blog/b09a6902-5284-4862-80f8-9a76be63c5b4",
    "https://www.mechaniconthego.com.ng/blog/cfcfce6e-5de2-442e-9625-adeffdc14a10",
    "https://www.mechaniconthego.com.ng/blog/dcb58a93-b83c-4635-94b7-2903ce2fba4c",
    "https://www.mechaniconthego.com.ng/blog/ffe325c4-090d-4581-bef9-c28b843347b9",
    "https://www.mechaniconthego.com.ng/blog/How-to-detect-and-prevent-oil-leaks-in-your-car-1699206471070",
    "https://www.mechaniconthego.com.ng/blog/How-to-Solve-The-Problem-of-A-Shaky-Steering-Wheel%3A-Including-Potential-Causes-1698930956349",
    "https://www.mechaniconthego.com.ng/blog/The-Importance-of-Tire-Maintenance-1698764721132",
    "https://www.mechaniconthego.com.ng/blog/Importance-of-Brake-Maintenance-and-Servicing-1698588162179",
    "https://www.mechaniconthego.com.ng/blog/Clean-Fuel%2C-Better-Performance%3A-Why-you-must-ensure-that-you-keep-your-fuel-clean-at-all-times-1698351364280",
    "https://www.mechaniconthego.com.ng/blog/Importance-of-Regular-Oil-Changes-1698151314536",
    "https://www.mechaniconthego.com.ng/blog/What-is-the-use-of-My-Car’s-Oil-Filter%3F-1697718532570",
    "https://www.mechaniconthego.com.ng/blog/Understanding-The-Car’s-Catalytic-Converter-1697542447386",
    "https://www.mechaniconthego.com.ng/blog/The-Car’s-Ignition-System%3A-A-Key-to-Smooth-Starts-1697342560618",
    "https://www.mechaniconthego.com.ng/blog/What-is-the-use-of-your-car’s-spark-plug%3F-1697106220634",
    "https://www.mechaniconthego.com.ng/blog/The-Check-Battery-Light%3A-Causes-and-Actions-1696926818553",
    "https://www.mechaniconthego.com.ng/blog/Engine-Oil-Viscosity%3A-All-you-need-to-know-1696329360313",
    "https://www.mechaniconthego.com.ng/blog/Understanding-the-Engine-Oil-Warning-Light-and-Check-Engine-Light-1695917303870",
    "https://www.mechaniconthego.com.ng/blog/Why-Do-Radiator-Fans-Fail%3F-1695455566574",
    "https://www.mechaniconthego.com.ng/blog/Car-Overheating%3A-Causes%2C-Symptoms%2C-and-Prevention-Tips-1695313508430",
    "https://www.machinerylubrication.com/Read/31395/engine-oils-filters",
    "https://www.machinerylubrication.com/Read/28383/automotive-lubricants-mechanics-system",
    "https://www.machinerylubrication.com/Read/30787/oil-change-signs",
    "https://www.cbac.com/media-center/blog/2020/july/10-tips-for-a-successful-oil-change/",
    "https://www.cbac.com/media-center/blog/2012/october/four-common-services-offered-at-auto-repair-cent/",
    "https://www.cbac.com/media-center/blog/2012/november/make-sure-youre-getting-quality-auto-parts/",
    "https://www.cbac.com/media-center/blog/2025/july/6-warning-signs-your-fuel-filter-needs-replaceme/",
    "https://carbon365.com/nigeria/blog/best-engine-oil/#:~:text=ensure%20optimal%20performance.-,2.,engine%20wear%20and%20sludge%20buildup."
]


def fetch_with_retry(url, retries=3, wait=5):
    """Attempts to fetch a URL with multiple retries and error handling."""
    for attempt in range(retries):
        try:
            print(f"🌐 Attempt {attempt+1}/{retries}: {url}")
            r = session.get(url, verify=False, timeout=20)
            r.html.render(timeout=40, sleep=2)
            return r
        except Exception as e:
            print(f"⚠️  Attempt {attempt+1} failed: {e}")
            if attempt < retries - 1:
                print(f"⏳ Retrying in {wait} seconds...")
                time.sleep(wait)
    print(f"❌ All retries failed for {url}")
    return None


def scrape_article(url):
    """Scrapes a single blog post (title + content)."""
    print(f"\n🔍 Scraping article: {url}")
    r = fetch_with_retry(url)

    if not r:
        return None

    # Extract title
    title = r.html.find("h1", first=True)
    title_text = title.text.strip() if title else "Untitled"

    # Extract paragraphs
    paragraphs = r.html.find("p")
    content_text = " ".join([p.text.strip() for p in paragraphs if p.text.strip()])

    print(f"✅ Done: {title_text[:60]}...")

    return {
        "url": url,
        "title": title_text,
        "content": content_text
    }


def main():
    print("🚀 Starting MechanicOnTheGo blog scraper...\n")

    results = []
    for url in START_ARTICLES:
        article = scrape_article(url)
        if article:
            results.append(article)
        time.sleep(2)  # polite delay between requests

    if results:
        with open("mechanic_articles.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print("\n🎉 Scraping complete! Saved as 'mechanic_articles.json'")
    else:
        print("\n⚠️ No articles scraped. Please check network or URLs.")


if __name__ == "__main__":
    main()

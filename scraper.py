# script to help scrape data from sites,blogs,etc

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time, random

# --------------------------
# Config
# --------------------------

# list of URLS to be scraped

URLS = [
    "https://blog.mechoautotech.com/2021/12/01/what-to-do-when-your-car-is-overheating/",
    "https://blog.mechoautotech.com/2023/02/15/what-is-routine-car-maintenance/",
    "https://blog.mechoautotech.com/2022/02/24/the-difference-between-car-maintenance-vs-tune-ups/",
    "https://blog.mechoautotech.com/2022/02/17/the-cost-of-diesel-car-maintenance/",
    "https://blog.mechoautotech.com/2022/01/06/best-car-cleaning-hacks-for-car-owners/",
    "https://blog.mechoautotech.com/2021/11/24/hot-weather-cause-vehicle-overheating/",
    "https://www.carmedis.com/best-auto-mechanic-workshop-in-lagos/",
    "https://www.carmedis.com/guide-to-finding-reliable-car-mechanics-in-nigeria/",
    "https://www.carmedis.com/vehicle-diagnostics-and-repair-in-lagos/",
    "https://www.carmedis.com/eco-friendly-jumpstarts-a-green-guide-for-reviving-your-car/",
    "https://www.carmedis.com/gearbox-repair-in-lagos/",
    "https://www.carmedis.com/why-wheel-alignment-balancing-matter-more-than-you-think/",
    "https://www.carmedis.com/emergency-essentials-a-quick-guide-to-jumpstarting-any-vehicle/",
    "https://www.carmedis.com/preventive-measures-keeping-your-battery-healthy-to-avoid-jumpstarts/",
    "https://suremech.com/contents/4119747",
    "https://smartdrive.com.ng/car-problems-in-nigeria/",
    "https://nigeriawide.com/car-maintenance-in-nigeria-essential-tips-for-longevity-on-nigerian-roads/",
    "https://thetorqueteam.com/automotive-diagnostics-process/",
    "https://www.howacarworks.com/",
    "https://carbon365.com/nigeria/blog/car-registration-process-in-nigeria/",
    "https://rynoauto.com/how-often-should-you-rotate-your-tires/",
    "https://rynoauto.com/why-you-should-always-buy-trusted-fuel-brands-in-nigeria/",
    "https://rynoauto.com/how-often-should-i-service-my-car/",
    "https://www.vanguardngr.com/2024/07/6-essential-safety-tips-for-driving-in-flood-conditions/",
    "https://suremech.com/contents/46681995",
    "https://hitechautomo.com/common-auto-repair-scams-and-how-to-avoid-them/",
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


]

USER_AGENTS = [
    # Chrome on Mac
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/117.0 Safari/537.36",
    
    # Chrome on Windows
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0 Safari/537.36",
    
    # Firefox
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0",
    
    # Safari on iPhone
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
]

# --------------------------
# Scraper Function
# --------------------------
def scrape_page(url):
    headers = {"User-Agent": random.choice(USER_AGENTS)}  # pick a random header
    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.find("h1")
        title = title.get_text(strip=True) if title else "No Title Found"

        paragraphs = [p.get_text(" ", strip=True) for p in soup.find_all("p")]
        content = " ".join(paragraphs)

        return {"url": url, "title": title, "content": content}
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return {"url": url, "title": None, "content": None}

# --------------------------
# Main
# --------------------------
if __name__ == "__main__":
    results = []
    for url in URLS:
        data = scrape_page(url)
        results.append(data)

        # Add random delay (2–6 seconds)
        delay = random.uniform(2, 6)
        print(f"⏳ Sleeping for {delay:.1f} seconds...")
        time.sleep(delay)

    df = pd.DataFrame(results)
    df.to_csv("car_articles_scraped.csv", index=False)
    print("✅ Scraping complete. Data saved to car_articles_scraped.csv")

import pandas as pd

# 🔹 Change this to your actual CSV file name
csv_file = "car_articles_scraped.csv"

try:
    # Load CSV
    df = pd.read_csv(csv_file)
    print("✅ File loaded successfully!")
    print("📄 Columns detected:", list(df.columns))

    # Open a new text file for writing
    with open("car_articles_formatted.txt", "w", encoding="utf-8") as f:
        for i, row in df.iterrows():
            title = str(row.get("title", "No title"))
            url = str(row.get("url", "No URL"))
            content = str(row.get("content", "No content"))

            f.write(f"===== ARTICLE {i+1} =====\n")
            f.write(f"Title: {title}\n")
            f.write(f"URL: {url}\n\n")
            f.write("Content:\n")
            f.write(f"{content}\n")
            f.write("\n" + "="*60 + "\n\n")

    print("🎉 Conversion complete! Check 'car_articles_formatted.txt'")
except Exception as e:
    print(f"⚠️ Error: {e}")

import json

with open("data/seo_data.json", "r") as f:
    seo_data = json.load(f)

def fetch_seo_metrics(keyword):
    """
    based on keyword it will return the metric if found else return default values
    """
    keyword = keyword.lower()
    return seo_data.get(keyword, {
        "search_volume": 10000,
        "keyword_difficulty": 0.4,
        "avg_cpc": 1.2
    })

if __name__ == "__main__":
    print(fetch_seo_metrics('home'))
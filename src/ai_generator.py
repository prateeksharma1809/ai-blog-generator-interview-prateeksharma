from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='../.env')
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_blog_post(keyword, seo_metrics):
    prompt = f"""
    Write a well-structured, SEO-optimized blog post targeting the keyword: "{keyword}".

    Include:
    - Begin with an engaging introduction that hooks the reader
    - Include 2 to 3 informative and well-formatted subheadings (H2 or H3 style)
    - Naturally incorporate the keyword and related terms for better SEO
    - Embed at least two product mentions with placeholder affiliate links like {{AFF_LINK_1}}, {{AFF_LINK_2}}
    - Write in a conversational, helpful tone to appeal to both users and search engines

    Use these keyword metrics to guide optimization:
    - Search Volume: {seo_metrics['search_volume']}
    - Keyword Difficulty: {seo_metrics['keyword_difficulty']}
    - Average CPC: {seo_metrics['avg_cpc']}

    Target length: ~1000 words
    Do not include a summary or meta-commentary about the post's SEO optimization or tone at the end. Conclude naturally, without reflective statements about the writing itself.
    """
    # print(prompt)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful SEO blog post writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )

    content = response.choices[0].message.content.strip()
    content = content.replace("{AFF_LINK_1}", "https://dummyurl1.com")
    content = content.replace("{AFF_LINK_2}", "https://dummyurl2.com")


    return content

if __name__ == "__main__":
    from seo_fetcher import fetch_seo_metrics
    keyword = "wireless earbuds"
    seo_metrics = fetch_seo_metrics(keyword)
    print(seo_metrics)

    # Generate blog post
    post = generate_blog_post(keyword, seo_metrics)

    # Print the result
    print("\n=== Generated Blog Post ===\n")
    print(post)
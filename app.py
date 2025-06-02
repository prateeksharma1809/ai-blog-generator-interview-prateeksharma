from flask import Flask, request, jsonify
from src.seo_fetcher import fetch_seo_metrics
from src.ai_generator import generate_blog_post
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
DAILY_KEYWORD = os.getenv("DAILY_KEYWORD", "Dummy")

app = Flask(__name__)
POST_DIR = "generated_posts"
os.makedirs(POST_DIR, exist_ok=True)

@app.route('/generate', methods=['GET'])
def generate():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Missing keyword"}), 400
    return jsonify(run_generation(keyword))

def run_generation(keyword):
    seo = fetch_seo_metrics(keyword)
    blog_post = generate_blog_post(keyword, seo)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{POST_DIR}/{keyword.replace(' ', '_')}_{timestamp}.md"
    with open(filename, "w") as f:
        f.write(blog_post)

    return {
        "keyword": keyword,
        "seo_metrics": seo,
        "saved_file": filename,
        "blog_post": blog_post
    }

def scheduled_job():
    print(f"[{datetime.now()}] Running scheduled job for '{DAILY_KEYWORD}'")
    run_generation(DAILY_KEYWORD)

# Start APScheduler
scheduler = BackgroundScheduler()
scheduler.add_job(scheduled_job, trigger="interval", days=1)
scheduler.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
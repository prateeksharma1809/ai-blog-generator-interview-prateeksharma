# ai-blog-generator-interview-prateeksharma

## AI-Powered Blog Post Generator with Daily Automation

This project is a Flask-based application that generates SEO-optimized blog posts using OpenAI. Given a keyword, it fetches mock SEO metrics, generates a structured blog post, and saves the result as a Markdown file. A built-in scheduler can auto-generate one post per day.

---

## Features

- REST API to generate blog posts via `GET /generate?keyword=...`
- AI-generated content using OpenAI (GPT-4o)
- Mocked SEO data (search volume, difficulty, CPC)
- Daily post generation via scheduler (APScheduler)
- Dockerized setup with local volume mount
- Affiliate link placeholders automatically replaced

---


## Technologies Used

- Python
- Flask
- OpenAI API
- APScheduler
- Docker
- dotenv

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/prateeksharma1809/ai-blog-generator-interview-prateeksharma.git
cd ai-blog-generator-interview-prateeksharma
```
### 2. Create .env file

add the Open AI API key in format below 

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

### 3. Build Docker image
```bash
docker build -t ai-blog-generator .
```

### 4. Run the app (with mounted volume)
```bash
docker run -p 5000:5000 --env-file .env -v "$(pwd)/generated_posts:/app/generated_posts" ai-blog-generator
```

---

## API Endpoint

### `GET /generate?keyword=<your_keyword>`

Generates a blog post using the given keyword and returns JSON with SEO metrics and file path.

**Example:**

```
http://localhost:5000/generate?keyword=wireless%20earbuds
```

---

### Scheduled Job (Daily Automation)

The app includes a built-in job that runs once per day and auto-generates a blog post using a predefined keyword.

To configure the keyword, set it in your `.env` file:

```env
DAILY_KEYWORD=wireless earbuds
```

The job is managed via [APScheduler](https://apscheduler.readthedocs.io/en/stable/), and the output is saved to the `generated_posts/` folder automatically.

You can change the frequency or behavior in `app.py` by modifying the scheduler settings.

---
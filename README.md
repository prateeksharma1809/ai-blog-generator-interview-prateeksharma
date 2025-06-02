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

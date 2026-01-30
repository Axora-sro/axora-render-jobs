Job template — how to use

This folder is a standalone job template you can copy to create new jobs.

Quick start (Windows PowerShell)

1. Copy `.env.example` to `.env` and edit values for local testing:
   copy .env.example .env

2. Create & activate venv:
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install deps and run:
   pip install -r requirements.txt
   python job_template.py

Testing

- Run unit tests with pytest:
  pip install -r requirements.txt
  pytest -q

Deploying to Render

- Build command: `pip install -r jobs/job_template/requirements.txt`
- Start command: `python jobs/job_template/job_template.py`
- Set environment variables in Render Dashboard (do NOT commit secrets to repo)

Copy this folder to make a new job, then update the script name and `requirements.txt` as needed.
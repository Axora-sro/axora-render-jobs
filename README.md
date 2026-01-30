# Render Jobs — Python

Overview

This repo template shows how to organize standalone Python jobs (each with its own `.env`) so they can be published to GitHub and run on Render as Cron/Job services.

Quick structure

```
/ (repo root)
├─ jobs/
│  ├─ job_example/
│  │  ├─ job_example.py    # standalone script
│  │  ├─ requirements.txt  # job-specific deps
│  │  └─ .env.example      # example env (commit)
├─ .gitignore
├─ render.yaml            # optional manifest to create jobs on Render
└─ README.md
```

Local dev

- Copy `jobs/job_example/.env.example` -> `jobs/job_example/.env` and fill secrets.
- Create a venv: `python -m venv .venv && .\.venv\Scripts\activate`
- Install: `pip install -r jobs/job_example/requirements.txt`
- Run: `python jobs/job_example/job_example.py`

GitHub & Render

- Add/commit the repo to GitHub.
- On Render, either:
  - Create a new Cron Job and point it to `python jobs/<job>/job.py`, or
  - Use the `render.yaml` manifest to declare jobs declaratively (see `render.yaml` for an example).
- Add production secrets in Render Dashboard (do NOT commit `.env` with real secrets).

Security

- Commit `.env.example` but add `.env` to `.gitignore`.
- Prefer Render environment variables for production secrets and keep the `.env` local only.

See below for file examples and a job template.

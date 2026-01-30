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

Deploying to Render — Step-by-step

Option A — Dashboard (manual)

1. Sign in to https://render.com and connect your GitHub account. Grant access to the `Axora-sro/axora-render-jobs` repo.
2. Click **New** → **Cron Job** (or **Background Job/Cron**).
3. Choose the repository `Axora-sro/axora-render-jobs` and branch `main`.
4. Fill in fields:
   - **Build command:** `pip install -r jobs/job_example/requirements.txt`
   - **Start command:** `python jobs/job_example/job_example.py`
   - **Schedule:** pick a cron expression or choose manual run for testing.
5. Add environment variables in Render Dashboard (Environment → Environment Variables). Do NOT commit secrets to the repo.
6. Run the job manually to verify logs.

Option B — Declarative (`render.yaml`)

1. The repo contains a `render.yaml` manifest with an example cron job named `job-example`.
2. The manifest declares the build and start commands and a sample environment key. **Do not** put secret values in `render.yaml` — use the Dashboard to set secrets after the job is created.
3. To apply the manifest, open Render Dashboard, go to **New** → **Import from GitHub**, select the repository and choose the option to import services from the manifest (or create the job manually and copy fields from `render.yaml`).

Troubleshooting & tips

- If build fails, inspect the build logs for missing packages and update `requirements.txt`.
- Use the Render job logs to debug runtime errors; look for the example startup message in logs: `This is example job — logs will show this message when it runs.`
- For production secrets, add them via the Dashboard and mark them as secret.

See `render.yaml` for a sample cron entry and adjust the schedule as needed.

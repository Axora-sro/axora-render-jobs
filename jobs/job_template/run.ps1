# PowerShell helper to run the job locally
Set-Location -Path "$PSScriptRoot"
if (-Not (Test-Path -Path ".venv")) {
    python -m venv .venv
}
. .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python job_template.py

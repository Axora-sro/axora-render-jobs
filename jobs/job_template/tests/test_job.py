import os
import importlib

from jobs.job_template import job_template


def test_main_success(monkeypatch):
    monkeypatch.setenv('EXAMPLE_KEY', 'ci_test')
    assert job_template.main() == 0


def test_run_without_env(monkeypatch):
    # Ensure code still returns success when env var missing
    monkeypatch.delenv('EXAMPLE_KEY', raising=False)
    assert job_template.main() == 0

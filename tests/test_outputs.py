import json
from pathlib import Path

def test_report_exists():
    """Criterion 1: The agent must write /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_schema():
    """Criterion 2: report.json contains exactly the required keys."""
    data = json.loads(Path("/app/report.json").read_text())
    assert {"total_requests", "unique_ips", "top_path"} <= data.keys()

def test_total_requests():
    """Criterion 3: total_requests equals the number of log lines (6)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["total_requests"] == 6

def test_unique_ips():
    """Criterion 4: unique_ips equals the count of distinct client IPs (3)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["unique_ips"] == 3

def test_top_path():
    """Criterion 5: top_path is the most frequently requested path (/index.html)."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data["top_path"] == "/index.html"

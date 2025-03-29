import subprocess
import sys
from pathlib import Path

import pytest


def test_cli_basic_usage(temp_project_dir):
    """Test basic CLI usage."""
    output_file = temp_project_dir / "output.txt"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sourcesnatcher",
            str(temp_project_dir),
            "-o",
            str(output_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_file.exists()
    content = output_file.read_text()
    assert "test.txt" in content
    assert "test.json" in content


def test_cli_with_debug(temp_project_dir):
    """Test CLI with debug output."""
    output_file = temp_project_dir / "output.txt"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sourcesnatcher",
            str(temp_project_dir),
            "-o",
            str(output_file),
            "--debug",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Generating tree for:" in result.stderr
    assert "Processing file:" in result.stderr


def test_cli_with_json_format(temp_project_dir):
    """Test CLI with JSON output format."""
    output_file = temp_project_dir / "output.json"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sourcesnatcher",
            str(temp_project_dir),
            "-o",
            str(output_file),
            "-f",
            "json",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_file.exists()
    import json

    with open(output_file) as f:
        data = json.load(f)
    assert "tree" in data
    assert "files" in data


def test_cli_with_config_file(temp_project_dir, config_file):
    """Test CLI with custom configuration file."""
    output_file = temp_project_dir / "output.txt"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sourcesnatcher",
            str(temp_project_dir),
            "-o",
            str(output_file),
            "--config",
            str(config_file),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_file.exists()
    content = output_file.read_text()
    assert "test.bin" not in content
    assert ".git" not in content


def test_cli_with_nonexistent_directory():
    """Test CLI with nonexistent directory."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "sourcesnatcher",
            "/nonexistent/directory",
            "-o",
            "output.txt",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "Error" in result.stderr

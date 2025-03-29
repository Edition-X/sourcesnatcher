from pathlib import Path

import pytest

from sourcesnatcher.capture_project import ProjectCapture


def test_project_capture_initialization():
    """Test that ProjectCapture initializes with default config."""
    capturer = ProjectCapture()
    assert capturer.config is not None
    assert "excluded_dirs" in capturer.config
    assert "excluded_files" in capturer.config
    assert "text_extensions" in capturer.config
    assert "include_files" in capturer.config


def test_project_capture_custom_config(sample_config):
    """Test that ProjectCapture accepts custom configuration."""
    capturer = ProjectCapture(sample_config)
    assert capturer.config == sample_config


def test_is_text_file_with_extension(temp_project_dir):
    """Test text file detection based on extensions."""
    capturer = ProjectCapture()

    # Should be text files
    assert capturer.is_text_file(str(temp_project_dir / "test.txt"))
    assert capturer.is_text_file(str(temp_project_dir / "test.json"))
    assert capturer.is_text_file(str(temp_project_dir / "test.py"))

    # Should not be text files
    assert not capturer.is_text_file(str(temp_project_dir / "test.bin"))


def test_is_text_file_with_include_files(temp_project_dir):
    """Test text file detection based on include_files list."""
    config = {
        "excluded_dirs": [],
        "excluded_files": [],
        "text_extensions": [],
        "include_files": ["test.bin"],
    }
    capturer = ProjectCapture(config)

    # Should be text file because it's in include_files
    assert capturer.is_text_file(str(temp_project_dir / "test.bin"))

    # Should not be text file
    assert not capturer.is_text_file(str(temp_project_dir / "test.txt"))


def test_check_dependencies():
    """Test dependency checking."""
    capturer = ProjectCapture()
    # This should not raise an exception if tree is installed
    capturer.check_dependencies()

import os
import pytest
from pathlib import Path

@pytest.fixture
def temp_project_dir(tmp_path):
    """Create a temporary project directory with sample files."""
    project_dir = tmp_path / "test_project"
    project_dir.mkdir()
    
    # Create sample files
    (project_dir / "test.txt").write_text("test content")
    (project_dir / "test.json").write_text('{"test": "content"}')
    (project_dir / "test.py").write_text('print("test")')
    (project_dir / "test.bin").write_bytes(b"binary content")
    
    # Create sample directories
    (project_dir / ".git").mkdir()
    (project_dir / "node_modules").mkdir()
    (project_dir / "src").mkdir()
    (project_dir / "src" / "test.py").write_text('print("src test")')
    
    return project_dir

@pytest.fixture
def sample_config():
    """Provide a sample configuration dictionary."""
    return {
        'excluded_dirs': ['.git', 'node_modules'],
        'excluded_files': ['test.bin'],
        'text_extensions': ['.txt', '.json', '.py'],
        'include_files': ['Makefile']
    }

@pytest.fixture
def config_file(temp_project_dir, sample_config):
    """Create a temporary config file."""
    import yaml
    config_path = temp_project_dir / "config.yaml"
    with open(config_path, 'w') as f:
        yaml.dump(sample_config, f)
    return config_path 
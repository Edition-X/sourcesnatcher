import pytest
from pathlib import Path
from sourcesnatcher.capture_project import ProjectCapture

def test_capture_structure_text_format(temp_project_dir):
    """Test capturing project structure in text format."""
    capturer = ProjectCapture()
    output_file = temp_project_dir / "output.txt"
    
    capturer.capture_structure(str(temp_project_dir), str(output_file))
    
    assert output_file.exists()
    content = output_file.read_text()
    
    # Should include text files
    assert "test.txt" in content
    assert "test.json" in content
    assert "test.py" in content
    
    # Should not include binary files
    assert "test.bin" not in content
    
    # Should not include excluded directories
    assert ".git" not in content
    assert "node_modules" not in content

def test_capture_structure_json_format(temp_project_dir):
    """Test capturing project structure in JSON format."""
    capturer = ProjectCapture()
    output_file = temp_project_dir / "output.json"
    
    capturer.capture_structure(str(temp_project_dir), str(output_file), format='json')
    
    assert output_file.exists()
    import json
    with open(output_file) as f:
        data = json.load(f)
    
    assert 'tree' in data
    assert 'files' in data
    assert 'test.txt' in data['files']
    assert 'test.json' in data['files']
    assert 'test.py' in data['files']

def test_capture_structure_yaml_format(temp_project_dir):
    """Test capturing project structure in YAML format."""
    capturer = ProjectCapture()
    output_file = temp_project_dir / "output.yaml"
    
    capturer.capture_structure(str(temp_project_dir), str(output_file), format='yaml')
    
    assert output_file.exists()
    import yaml
    with open(output_file) as f:
        data = yaml.safe_load(f)
    
    assert 'tree' in data
    assert 'files' in data
    assert 'test.txt' in data['files']
    assert 'test.json' in data['files']
    assert 'test.py' in data['files']

def test_capture_structure_with_custom_config(temp_project_dir, sample_config):
    """Test capturing project structure with custom configuration."""
    capturer = ProjectCapture(sample_config)
    output_file = temp_project_dir / "output.txt"
    
    capturer.capture_structure(str(temp_project_dir), str(output_file))
    
    assert output_file.exists()
    content = output_file.read_text()
    
    # Should not include files from excluded_files
    assert "test.bin" not in content
    
    # Should not include directories from excluded_dirs
    assert ".git" not in content
    assert "node_modules" not in content

def test_capture_structure_with_nonexistent_directory():
    """Test capturing project structure with nonexistent directory."""
    capturer = ProjectCapture()
    with pytest.raises(FileNotFoundError):
        capturer.capture_structure("/nonexistent/directory", "output.txt") 
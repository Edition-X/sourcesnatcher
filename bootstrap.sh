#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add shebang line to capture_project.py if it doesn't exist
if ! grep -q "^#!/usr/bin/env python3" "$SCRIPT_DIR/capture_project.py"; then
    echo "#!/usr/bin/env python3" | cat - "$SCRIPT_DIR/capture_project.py" > temp && mv temp "$SCRIPT_DIR/capture_project.py"
fi

# Make the script executable
chmod +x "$SCRIPT_DIR/capture_project.py"

# Create symbolic link in /usr/local/bin
sudo ln -sf "$SCRIPT_DIR/capture_project.py" /usr/local/bin/capture-project

echo "Setup complete! You can now use 'capture-project' from any directory."
echo "Usage: capture-project <directory-path> [--debug]" 
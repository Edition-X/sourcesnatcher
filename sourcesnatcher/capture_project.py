#!/usr/bin/env python3
import argparse
import json
import mimetypes
import os
import subprocess
import sys
from pathlib import Path
from shutil import which
from typing import Any, Collection, Dict, List, Optional, Set, cast

import yaml


class ProjectCapture:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize with default or custom configuration."""
        self.config: Dict[str, Any] = {
            "excluded_dirs": [
                ".git",
                ".terraform",
                "lib",
                "__pycache__",
                "venv",
                "node_modules",
                "autoload",
                "backup",
                "pack",
            ],
            "excluded_files": ["credentials.txt", ".gitignore"],
            "text_extensions": [
                ".yml",
                ".yaml",
                ".json",
                ".j2",
                ".conf",
                ".txt",
                ".md",
                ".py",
                ".gitignore",
            ],
            "include_files": [],  # Empty by default
        }
        if config:
            self.config.update(config)

    def is_text_file(self, file_path: str) -> bool:
        """
        Check if a file is a text file based on:
        1. If it's in the include_files list (if not empty)
        2. If it has a text extension
        3. If it has a text mime type
        """
        # Get just the filename
        filename = os.path.basename(file_path)

        # If include_files is not empty, only those files are considered text files
        include_files = cast(List[str], self.config["include_files"])
        if include_files:
            return filename in include_files

        # Otherwise, check extensions and mime type
        text_extensions = cast(List[str], self.config["text_extensions"])
        if any(filename.endswith(ext) for ext in text_extensions):
            return True

        # Check mime type only if not in text_extensions
        mime_type, _ = mimetypes.guess_type(file_path)
        return mime_type is not None and mime_type.startswith("text")

    def _should_include_file(self, file_path: str) -> bool:
        """
        Check if a file should be included in the output.
        """
        filename = os.path.basename(file_path)
        excluded_files = cast(List[str], self.config["excluded_files"])
        return filename not in excluded_files and self.is_text_file(file_path)

    def check_dependencies(self) -> None:
        if not which("tree"):
            raise RuntimeError(
                "The 'tree' command is not installed. Please install it first."
            )

    def capture_structure(
        self,
        startpath: str,
        output_file: str,
        format: str = "text",
        debug: bool = False,
    ) -> None:
        """
        Capture the structure and contents of a project directory.

        Args:
            startpath: Path to the project directory
            output_file: Path to save the output
            format: Output format ('text', 'json', or 'yaml')
            debug: Whether to print debug information
        """
        self.check_dependencies()

        if not os.path.exists(startpath):
            raise FileNotFoundError(f"Directory not found: {startpath}")

        # Special case handling
        if "log-restore-automation-tool" in startpath:
            startpath = os.path.join(startpath, "src")
            if not os.path.exists(startpath):
                raise FileNotFoundError(f"'src' directory not found in {startpath}")

        result: Dict[str, Any] = {"tree": "", "files": {}}

        def generate_tree(path: str, prefix: str = "") -> List[str]:
            """Generate a tree-like structure of the directory."""
            if debug:
                print(f"Generating tree for: {path}", file=sys.stderr)

            tree_lines = []
            entries = sorted(os.listdir(path))

            for i, entry in enumerate(entries):
                entry_path = os.path.join(path, entry)
                is_last = i == len(entries) - 1

                # Skip excluded directories
                if os.path.isdir(entry_path):
                    excluded_dirs = cast(List[str], self.config["excluded_dirs"])
                    if entry in excluded_dirs:
                        if debug:
                            print(
                                f"Skipping excluded directory: {entry}", file=sys.stderr
                            )
                        continue

                    # Add directory to tree
                    tree_lines.append(f"{prefix}{'└── ' if is_last else '├── '}{entry}")

                    # Recursively process subdirectory
                    extension = "    " if is_last else "│   "
                    tree_lines.extend(generate_tree(entry_path, prefix + extension))
                else:
                    # Skip non-text files
                    if not self._should_include_file(entry_path):
                        if debug:
                            print(f"Skipping non-text file: {entry}", file=sys.stderr)
                        continue

                    # Add file to tree
                    tree_lines.append(f"{prefix}{'└── ' if is_last else '├── '}{entry}")

            return tree_lines

        # Generate tree structure
        tree_lines: List[str] = [os.path.basename(startpath)]
        tree_lines.extend(generate_tree(startpath))
        result["tree"] = "\n".join(tree_lines)

        # Capture file contents
        processed_files: Set[str] = set()

        if debug:
            print("Capturing file contents...", file=sys.stderr)

        for root, dirs, files in os.walk(startpath):
            # Filter out excluded directories
            excluded_dirs = cast(List[str], self.config["excluded_dirs"])
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            # Filter and process files
            for file in files:
                file_path = os.path.join(root, file)
                if file_path in processed_files:
                    if debug:
                        print(
                            f"Skipping already processed file: {file}", file=sys.stderr
                        )
                    continue

                processed_files.add(file_path)

                if not self._should_include_file(file_path):
                    if debug:
                        print(f"Skipping file: {file}", file=sys.stderr)
                    continue

                if debug:
                    print(f"Processing file: {file_path}", file=sys.stderr)

                try:
                    with open(file_path, "r", errors="ignore") as f:
                        result["files"][
                            os.path.relpath(file_path, startpath)
                        ] = f.read()
                except Exception as e:
                    error_msg = f"Error reading file: {str(e)}"
                    result["files"][os.path.relpath(file_path, startpath)] = error_msg
                    if debug:
                        print(f"Error reading file {file_path}: {e}", file=sys.stderr)

        # Write output in specified format
        with open(output_file, "w") as f:
            if format == "json":
                json.dump(result, f, indent=2)
            elif format == "yaml":
                yaml.dump(result, f)
            else:  # text format
                f.write(result["tree"])
                for file_path, contents in result["files"].items():
                    f.write(f"\n\n# File: {file_path}\n\n{contents}")


def main():
    parser = argparse.ArgumentParser(
        description="Capture project structure and file contents"
    )
    parser.add_argument("directory", help="Project directory to capture")
    parser.add_argument(
        "--output",
        "-o",
        help="Output file name (default: <project_name>_contents.<format>)",
    )
    parser.add_argument(
        "--format",
        "-f",
        choices=["text", "json", "yaml"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug output")
    parser.add_argument("--config", help="Path to configuration file")

    args = parser.parse_args()

    # Load custom configuration if provided
    config = None
    if args.config:
        with open(args.config) as f:
            config = yaml.safe_load(f)

    # Generate output filename if not provided
    if not args.output:
        project_name = os.path.basename(os.path.normpath(args.directory))
        args.output = f"{project_name}_contents.{args.format}"

    try:
        capturer = ProjectCapture(config)
        print(f"Preparing to capture project structure for {args.directory}")
        capturer.capture_structure(args.directory, args.output, args.format, args.debug)
        print(f"Output saved to {args.output}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

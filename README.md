# Source Snatcher

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Source Snatcher is a powerful and flexible project structure analysis tool that captures and analyzes project directories with precision and efficiency. It's designed for developers, system administrators, and technical analysts who need to understand and document project structures.

## 🌟 Key Features

- **Intelligent Project Structure Capture**
  - Generates detailed directory trees using custom tree visualization
  - Smart file content extraction with configurable filters
  - Handles large projects efficiently with optimized processing

- **Multiple Output Formats**
  - Text format for human-readable output
  - JSON format for programmatic analysis
  - YAML format for configuration-friendly output

- **Advanced Configuration**
  - Customizable file and directory exclusions
  - Configurable text file detection
  - Flexible include/exclude patterns
  - Support for custom configuration files

- **Developer-Friendly Features**
  - Debug mode for troubleshooting
  - Graceful error handling
  - MIME type detection for text files
  - Special case handling for specific project types

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://gitlab.ocado.tech/d.kelly/sourcesnatcher.git
cd sourcesnatcher
```

2. Install dependencies:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

## 💡 Usage

### Basic Usage
```bash
capture-project /path/to/project
```

### Advanced Options

#### Debug Mode
```bash
capture-project /path/to/project --debug
```

#### Output Formats
```bash
# JSON output
capture-project /path/to/project --format json

# YAML output
capture-project /path/to/project --format yaml
```

#### Custom Output File
```bash
capture-project /path/to/project -o output.yaml -f yaml
```

#### Custom Configuration
```bash
capture-project /path/to/project --config my_config.yaml
```

## ⚙️ Configuration

Create a `config.yaml` file to customize the behavior:

```yaml
excluded_dirs:
  - .git
  - .terraform
  - lib
  - __pycache__
  - venv
  - node_modules
  - autoload
  - backup
  - pack

excluded_files:
  - credentials.txt
  - .gitignore

text_extensions:
  - .yml
  - .yaml
  - .json
  - .j2
  - .conf
  - .txt
  - .md
  - .py
  - .gitignore

include_files:
  - Makefile
  - inventory
  - ansible.cfg
```

## 🛠️ Development

### Prerequisites
- Python 3.8 or higher
- `tree` command-line tool
- pipenv for dependency management

### Development Setup
1. Install development dependencies:
```bash
pipenv install --dev
```

2. Run tests:
```bash
pytest
```

3. Format code:
```bash
black .
```

4. Type checking:
```bash
mypy .
```

## 📝 Output Format

The tool generates structured output containing:
- A tree representation of the project structure
- Contents of all relevant text files
- File paths relative to the project root
- Error messages for files that couldn't be read

### Example Output
```
project_root/
├── src/
│   ├── main.py
│   └── utils.py
└── tests/
    └── test_main.py

# File: src/main.py
def main():
    print("Hello, World!")

# File: src/utils.py
def helper():
    pass
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Thanks to all contributors who have helped shape Source Snatcher
- Inspired by the need for efficient project structure analysis
- Built with modern Python best practices

## 📞 Support

For support, please open an issue in the GitLab repository or contact the maintainers.

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.ocado.tech/d.kelly/sourcesnatcher.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.ocado.tech/d.kelly/sourcesnatcher/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

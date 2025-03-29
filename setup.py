from setuptools import setup, find_packages

setup(
    name="sourcesnatcher",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0.2",
    ],
    entry_points={
        'console_scripts': [
            'capture-project=capture_project:main',
        ],
    },
    python_requires=">=3.13",
) 
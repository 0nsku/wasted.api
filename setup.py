from setuptools import setup 

with open("requirements.txt") as f: 
    requirements = f.read().splitlines()

setup(
    name="wasted-api",
    version="1.0.0",
    description="A Python API wrapper for wasted api",
    author="0nsku",
    url="https://github.com/0nsku/wasted.api",
    install_requires=requirements,
    python_requires='>=3.8.0',
    project_urls = {
        "Documentation": "https://wasted.bio/docs"
    }
)

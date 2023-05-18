from setuptools import setup, find_packages
import os

# Read the contents of your README file
this_directory = os.path.dirname(os.path.realpath(__file__))
readme_path = os.path.join(this_directory, "docs", "README.md")

# Read the contents of the README file
with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

# Get requirements from requirements.txt to a list
with open(
    os.path.join(this_directory, "src/agent-llm/requirements.txt"), encoding="utf-8"
) as f:
    install_requires = f.read().splitlines()
requirements = []
for reqs in install_requires:
    if "--" not in reqs and ":" not in reqs and "#" not in reqs:
        requirements.append(reqs)
# Get version from version file in src/agent-llm/version
with open(os.path.join(this_directory, "src/agent-llm/version"), encoding="utf-8") as f:
    version = f.read().strip()

setup(
    name="agent-llm",
    version=version,
    description="An Artificial Intelligence Automation Platform. AI Instruction management from various providers, has an adaptive memory, and a versatile plugin system with many commands including web browsing. Supports many AI providers and models and growing support every day.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # This should match the format of your README
    author="Josh XT",
    author_email="josh@devxt.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.10",
    install_requires=requirements,
)

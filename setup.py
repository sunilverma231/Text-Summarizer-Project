import setuptools
from pathlib import Path

__version__ = "0.0.1"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "sunilverma"
SRC_REPO = "text_summarizer"
AUTHOR_EMAIL = "sunilverma00027@gmail.com"

this_directory = Path(__file__).parent
readme_path = this_directory / "README.md"

long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)


    
from setuptools import find_packages, setup

setup(
    name="diggerpy",
    version="0.1.0",
    author="SimCo92",
    author_email="s.colonna92@gmail.com",
    description="A Python client for the Discogs API",
    url="https://github.com/simco92/diggerpy",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.25.1",
    ],
    entry_points={
        "console_scripts": [
            "client = client.cli:main",
        ],
    },
)

# fast-crawl

`fast-crawl` is a lightweight and efficient web scraping tool built with Python, leveraging the awesome `crawl4ai`. It also leverages modern frameworks like FastAPI, Pydantic, and Uvicorn to provide a robust and scalable solution for scraping single or multiple web pages. With built-in support for headless browsers and logging via Loguru, `fast-crawl` is designed to be quick and developer-friendly and easy to extend. Whether you're scraping for data analysis, research, or automation, this project offers a quick and reliable way to get started.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi) ![Pydantic](https://img.shields.io/badge/pydantic-4A91A2?style=for-the-badge&logo=python&logoColor=white) ![Uvicorn](https://img.shields.io/badge/uvicorn-111111?style=for-the-badge&logo=uvicorn&logoColor=white) ![Loguru](https://img.shields.io/badge/loguru-FF9C00?style=for-the-badge&logo=python&logoColor=white)

![CodeQL](https://img.shields.io/badge/codeql-006F99?style=for-the-badge&logo=github-actions&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Apache License 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)

## Installation

> [!NOTE]
> Developed on `python 3.10.16`.

To get started, you can create a virtual environment using either `venv` or `conda`. Below are the steps for both methods using Python 3.10.

### Using `venv` (Linux)

1. Ensure Python 3.10 is installed on your system.
2. Create a virtual environment:
   ```bash
   python3.10 -m venv fastcrawl
   ```
3. Activate the virtual environment:
   ```bash
   source fastcrawl/bin/activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Using `conda`

1. Ensure `conda` is installed on your system.
2. Create a new conda environment with Python 3.10:
   ```bash
   conda create --name fastcrawl python=3.10
   ```
3. Activate the conda environment:
   ```bash
   conda activate fastcrawl
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Both methods will set up an isolated environment for running the project.

### Setting Up Headless Browser and Dependencies

Ensure that your local machine is configured with a headless browser and all necessary dependencies for the code to run. You can use the following command to set up everything:

```bash
crawl4ai-setup
```

---

## Quickstart Example Scripts

run simple single page scraper:

```bash
python -m crawl_engine.example
```

this would return the markdown of the webpage of my favorite online instructor <a href="https://www.techwithtim.net/">tech with tim.</a>

run batch urls scraper:

```bash
python -m crawl_engine.crawl_engine
```

it scrapes 5 urls that is given inside by default. Tweak and play with them!

> [!IMPORTANT]
> API service is still broken, to be fixed soon! You are welcome to contribute.

---

## Collaborate & Contribute

Bug reports, issues, forks and pull requests are always welcome!

---

## License

This project is available as open source under the MIT License. See the [LICENSE](./LICENSE) file for details.

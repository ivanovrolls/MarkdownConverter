# Resume Generator

This is a simple resume generator that converts a Markdown CV into a nicely formatted PDF and HTML resume using Jinja2 templates and Playwright for PDF rendering.

---

## Features

- Parses structured resume data from a Markdown (`.md`) file.
- Uses Jinja2 templating for flexible HTML resume design.
- Generates both HTML and PDF versions of the resume.
- Supports command-line argument to specify the Markdown CV file.
- Shows a progress bar during generation for better user experience.

---

## Requirements

- Python 3.7+
- Packages listed in `requirements.txt` (or install manually):

```bash
pip install jinja2 playwright tqdm
playwright install
```

---

## How to Run

Run the generator script from the command line, passing the path to your Markdown resume file as an argument:

```bash
python generator.py path/to/your_resume.md
```

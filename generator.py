import sys, time, tqdm
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from resume_data import cv_data
from playwright.sync_api import sync_playwright

#handle command line arguments
if len(sys.argv) != 2:
    print("Usage: python generator.py <markdown_file>")
    sys.exit(1)

md_path = Path(sys.argv[1])
if not md_path.exists():
    print(f"Markdown file {md_path} does not exist.")
    sys.exit(1)

#loading bar
steps = [
    "Reading markdown...",
    "Parsing data...",
    "Rendering HTML template...",
    "Saving HTML file...",
    "Generating PDF...",
    "Cleaning up..."
]

for step in tqdm.tqdm(steps, desc="Generating Resume", ncols=80):
    time.sleep(0.5)  #simulate work being done


with open(md_path, "r") as file:
    md_text = file.read()

resume = cv_data(md_text)  # Parse the markdown text into structured data

env = Environment(loader=FileSystemLoader("templates")) #point jinja to the templates directory
template = env.get_template("resume_template.html") #load template file
output = template.render(**resume) #inject data into template
with open("output/output_resume.html", "w") as f: #output
    f.write(output)

with sync_playwright() as p: #use playwright to convert html to pdf by using browser rendering and exporting
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.set_content(output)
    page.pdf(path="output/output_resume.pdf", format="A4")
    browser.close()

print("Resume generated successfully! 📝") #confirmation message

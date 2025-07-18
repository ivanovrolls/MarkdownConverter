from jinja2 import Environment, FileSystemLoader
from resume_data import cv_data
from playwright.sync_api import sync_playwright

with open("CV.md", "r") as file:
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

print("Resume generated successfully!") #confirmation message

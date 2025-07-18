from jinja2 import Environment, FileSystemLoader
from resume_data import data as resume

env = Environment(loader=FileSystemLoader("templates")) #point jinja to the templates directory
template = env.get_template("resume_template.html") #load template file
output = template.render(**resume) #inject data into template
with open("output_resume.html", "w") as f: #output
    f.write(output)

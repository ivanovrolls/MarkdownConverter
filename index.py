import markdown

with open('sample.md', 'r') as f:
    markdown_string = f.read()

html_string = markdown.markdown(markdown_string)

with open('sample.html', 'w') as f:
    f.write(html_string)
import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split('\n')

    for line in lines:
        if line.startswith('# '):
            return line[2:]

    raise ValueError('no title header found')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r') as file:
        content = file.read()

    with open(template_path, 'r') as file:
        template = file.read()

    contentHTML = markdown_to_html_node(content).to_html()
    title = extract_title(content)

    fullHTML = template.replace('{{ Title }}' , title).replace('{{ Content }}' , contentHTML)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(fullHTML)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)

        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

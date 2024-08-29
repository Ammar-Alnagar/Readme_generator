import os
import yaml
from jinja2 import Template
from src.file_handler import read_file, write_file

class ReadmeGenerator:
    def __init__(self, template_path, user_input_path):
        self.template = read_file(template_path)
        self.user_input = self.load_user_input(user_input_path)

    def load_user_input(self, path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

    def generate_readme(self, name):
        template = Template(self.template)
        content = template.render(name=name, **self.user_input)
        return content

    def save_readme(self, name, content, output_dir):
        filename = f"{name.lower().replace(' ', '_')}_README.md"
        output_path = os.path.join(output_dir, filename)
        write_file(output_path, content)
        print(f"README file generated: {output_path}")

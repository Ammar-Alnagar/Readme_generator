import os
from src.readme_generator import ReadmeGenerator

def main():
    template_path = 'templates/readme_template.md'
    user_input_path = 'user_input/additional_details.yaml'
    output_dir = 'output'

    generator = ReadmeGenerator(template_path, user_input_path)

    while True:
        name = input("Enter the project name (or 'q' to quit): ")
        if name.lower() == 'q':
            break

        readme_content = generator.generate_readme(name)
        generator.save_readme(name, readme_content, output_dir)

if __name__ == "__main__":
    main()

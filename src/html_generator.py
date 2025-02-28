# use jinja templates
# see https://atufashireen.medium.com/creating-templates-with-jinja-in-python-3ff3b87d6740

from jinja2 import Environment, FileSystemLoader


def generate_html(recipe: dict, template_name: str) -> str:
    file_loader = FileSystemLoader("../templates/recipe")
    env = Environment(loader=file_loader)
    template = env.get_template(f"{template_name}.html")
    return template.render(recipe=recipe, page_number=17, show_notes=False)

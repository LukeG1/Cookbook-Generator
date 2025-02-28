# take a recipe or book as input and make sure it's well formed
# give feedback as much as possilble
# optional samples?

import yaml
from pprint import pprint


# import markdown

# def markdown_to_html_inline(md_text):
#     # Convert using markdown, restricting to inline elements
#     return markdown.markdown(md_text, extensions=['markdown.extensions.extra'], output_format='html5').strip()

# # Example Usage
# md_text = "**Bold** and *italic* and [link](https://example.com)"
# html_output = markdown_to_html_inline(md_text)
# print(html_output)


# TODO: add error checking
# TODO: add inline markdown support
# TODO: handle my weird string syntax, kinda like f strings
# TODO: reformat ingredients into a nicer format, or ask that of the templater?
def interpret_recipe(name: str) -> dict:
    with open(f"../content/recipes/{name}.yaml") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None

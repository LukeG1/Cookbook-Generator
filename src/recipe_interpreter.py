# take a recipe or book as input and make sure it's well formed
# give feedback as much as possilble
# optional samples?

import yaml
from pprint import pprint


# TODO: add error checking
def open_recipe(name: str) -> dict:
    with open(f"../content/recipes/{name}.yaml") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None

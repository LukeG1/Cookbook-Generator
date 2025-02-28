# take a book file as input, generate a full book


# dumb version below
from recipe_interpreter import interpret_recipe
from html_generator import generate_html
from html_to_pdf import html_to_pdf

print("Interpreting recipe...")
recipe = interpret_recipe("chorizo_potato_tacos")
# print(recipe["meta"])
print("Generating html...")
html = generate_html(recipe, "my_original")

with open(f"../outputs/test.html", "w+") as file:
    file.write(html)

pdf = html_to_pdf("book_1", html)

print("Generating pdf...")

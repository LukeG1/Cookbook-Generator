# take a book file as input, generate a full book


# dumb version below
from recipe_interpreter import interpret_recipe
from html_generator import generate_html
from html_to_pdf import html_to_pdf

recipe = interpret_recipe("chorizo_potato_tacos")
html = generate_html(recipe, "my_original")
# pdf = html_to_pdf("book_1", html)

from weasyprint import HTML

HTML(string="<p>document</p>").write_pdf("../outputs/test.pdf", pdf_variant="pdf/a-3u")

# text_file = open("../outputs/test.html", "w+")
# text_file.write(html)
# text_file.close()

# print(recipe)

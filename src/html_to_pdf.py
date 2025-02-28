# temporary selenium way:

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.chrome.service import Service
import time
import base64
import os
import tempfile

print_options = PrintOptions()
print_options.page_width = 14.8
print_options.page_height = 21
print_options.scale = 1
print_options.orientation = "portrait"
print_options.background = True
print_options.margin_bottom = 0
print_options.margin_left = 0
print_options.margin_right = 0
print_options.margin_top = 0

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)


def html_to_pdf(output_name, html_str):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=True) as temp_html:
        temp_html.write(html_str)
        temp_html.flush()  # Ensure the content is written

        file_url = f"file://{temp_html.name}"
        driver.get(file_url)  # Load temporary HTML file

        pdfstr = driver.print_page(print_options)

        print("Saving pdf...")
        with open(f"../outputs/{output_name}.pdf", "wb+") as file:
            file.write(base64.b64decode(pdfstr))


# below is the better long term way:

# import requests


# # save the file or store in memory?
# # take into account other parameters like page size and stuff
# def html_to_pdf(dest_name: str, html: str):
#     files = {
#         "files": open("../outputs/test.html", "rb"),
#         "paperWidth": (None, "5.83"),
#         "paperHeight": (None, "8.27"),
#         "marginTop": (None, "0"),
#         "marginBottom": (None, "0"),
#         "marginLeft": (None, "0"),
#         "marginRight": (None, "0"),
#         "preferCssPageSize": (None, "false"),
#         "printBackground": (None, "true"),
#         "omitBackground": (None, "true"),
#         "landscape": (None, "false"),
#         "scale": (None, "1"),
#     }
#     response = requests.post(
#         "https://demo.gotenberg.dev/forms/chromium/convert/html",
#         files=files,
#         # "http://localhost:3000/forms/chromium/convert/html",
#         # files=files,
#     )

#     print(response.status_code)

#     with open("my.pdf", "wb") as f:
#         f.write(response.content)

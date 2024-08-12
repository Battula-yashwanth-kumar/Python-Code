# pip install lxml

from lxml import html

# Sample HTML
html_doc = """
<html>
  <head><title>The Dormouse's story</title></head>
  <body>
    <p class="title"><b>The Dormouse's story</b></p>
    <p class="story">Once upon a time there were three little sisters; and their names were
      <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
      <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
      <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
      and they lived at the bottom of a well.</p>
    <p class="story">...</p>
  </body>
</html>
"""

# Parse the HTML
tree = html.fromstring(html_doc)

# Find elements
title_element = tree.find(".//title")
print(f"Title: {title_element.text}")

# Modify elements
title_element.text = "New Title"

# Add new elements
new_element = html.Element("p", id="new_paragraph")
new_element.text = "This is a new paragraph."
tree.body.append(new_element)

# Print the modified HTML
print(html.tostring(tree, pretty_print=True).decode())


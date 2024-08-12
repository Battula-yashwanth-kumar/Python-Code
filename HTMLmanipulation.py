# pip install beautifulsoup4

from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html_doc, 'html.parser')

# Find elements
title_tag = soup.title
print(f"Title: {title_tag.string}")

# Modify elements
title_tag.string = "New Title"
print(f"Modified Title: {title_tag.string}")

# Add new elements
new_tag = soup.new_tag("p", id="new_paragraph")
new_tag.string = "This is a new paragraph."
soup.body.append(new_tag)

# Print the modified HTML
print(soup.prettify())


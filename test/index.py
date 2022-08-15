from re import compile
from bs4 import BeautifulSoup

with open("test/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title.string)
# print(title.text)

# .find() .find_all() Первый по спику, Все.

# page_h1 = soup.find("h1")
# print(page_h1)

# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)

# find_parent(), find_parents()
# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# .next_element, .previous_element
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_="post__title").find_next().text  
# print(next_el)

# find_next_sibling(), .find_previous_sibling()
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)
# next_sib = soup.find(class_="post__text").find_previous_sibling()
# print(next_sib)

# post_title = soup.find(class_="post__date").find_previous_sibling().find_next().text
# print(post_title)

# поиск по тексту
# find_a_by_text = soup.find("a", text = "Одежда для взрослых")
# print(find_a_by_text)

# find_a_by_text_2 = soup.find("a", text = compile("Одежда"))
# print(find_a_by_text_2)


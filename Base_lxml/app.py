from lxml import etree

# def print_tree(element, depth=0):
#     print("-" * depth + element.tag)

#     for child in element.iterchildren():
#         print(child, depth + 1)

tree = etree.parse("Base_lxml/web_page.html")

# root = tree.getroot()

# print_tree(root)

# title_element = tree.find("head/title")
# print(title_element.text)
# p_element = tree.find("body/p")
# print(p_element.text)

# list_items = tree.findall("body/ul/li")
# print(list_items)

# for li in list_items:
#     a = li.find("a")
#     if a is not None:
#         print(f"{li.text.strip()} {a.text}")
#     else:
#         print(li.text)

# title_element = tree.xpath("//title/text()")[0]
# print(title_element)

# p_elem = tree.xpath("//p/text()")[0]
# print(p_elem)

# list_items = tree.xpath("//ul/descendant::li")
# for li in list_items:
#     text = ''.join(map(str.strip, li.xpath("//text()")))
#     print(text)

html = tree.getroot()
title_element = html.cssselect("title")
print(title_element[0].text)

p_elem2 = html.cssselect("p")
print(p_elem2[0].text)
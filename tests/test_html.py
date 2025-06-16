import unittest
from html.parser import HTMLParser


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stylesheet_link_found = False

    def handle_starttag(self, tag, attrs):
        if tag == "link":
            attr_dict = dict(attrs)
            if attr_dict.get("rel") == "stylesheet" and attr_dict.get("href") == "style.css":
                self.stylesheet_link_found = True


class TestIndexHTML(unittest.TestCase):
    def test_stylesheet_link_present(self):
        with open("index.html", encoding="utf-8") as f:
            html = f.read()
        parser = LinkParser()
        parser.feed(html)
        self.assertTrue(parser.stylesheet_link_found,
                        "Tag <link rel='stylesheet' href='style.css'> não encontrada")


if __name__ == "__main__":
    unittest.main()

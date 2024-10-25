import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_multiple_props(self):
        # Test with multiple props
        node = HTMLNode(tag="a", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_props_to_html_with_single_prop(self):
        # Test with a single prop
        node = HTMLNode(tag="img", props={"src": "image.png"})
        self.assertEqual(node.props_to_html(), 'src="image.png"')

    def test_props_to_html_empty_props(self):
        # Test with no props
        node = HTMLNode(tag="div", props={})
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()

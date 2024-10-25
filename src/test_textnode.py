import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        # Test for equal text and type
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        # Test for inequality with different text
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_different_text_type(self):
        # Test for inequality with different text_type
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_equal_with_different_url(self):
        # Test for inequality with different URLs
        node = TextNode("Click Me", TextType.LINKS, url="http://test.com")
        node2 = TextNode("Click Me", TextType.LINKS, url="http://test.org")
        self.assertNotEqual(node, node2)

    def test_equal_with_url(self):
        # Test for equality when both nodes have the same URL
        node = TextNode("Click here", TextType.LINKS, url="http://test.com")
        node2 = TextNode("Click here", TextType.LINKS, url="http://test.com")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()

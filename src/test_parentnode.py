import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_multiple_children(self):
        # Test with multiple children (LeafNodes)
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        expected_html = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_no_tag(self):
        # Test with no tag (should raise ValueError)
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("b", "Bold text")])
            node.to_html()

    def test_to_html_with_no_children(self):
        # Test with no children (should raise ValueError)
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_to_html_with_nested_parent(self):
        # Test with nested ParentNode
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "More text"),
                    ]
                ),
                LeafNode("i", "italic text")
            ]
        )
        expected_html = '<div><p><b>Bold text</b>More text</p><i>italic text</i></div>'
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_with_props(self):
        # Test ParentNode with props and children
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
            ],
            {"class": "container"}
        )
        expected_html = '<div class="container"><b>Bold text</b>Normal text</div>'
        self.assertEqual(node.to_html(), expected_html)

if __name__ == "__main__":
    unittest.main()

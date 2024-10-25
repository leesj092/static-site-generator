import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html_with_tag_and_props(self):
        # Test rendering with tag and props
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_tag_no_props(self):
        # Test rendering with tag but no props
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')

    def test_to_html_no_tag(self):
        # Test rendering with no tag (raw text output)
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), 'This is raw text.')

    def test_value_is_required(self):
        # Test that value is required (should raise ValueError)
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_no_children_allowed(self):
        # Test that children are not allowed (should raise TypeError if children are set manually)
        node = LeafNode("p", "This is a leaf node")
        self.assertIsNone(node.children)

if __name__ == "__main__":
    unittest.main()

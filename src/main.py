from textnode import *
from leafnode import LeafNode

def main():
    textNode = TextNode('This is a text node', TextType.TEXT, 'https://www.boot.dev')
    print('in main')

def text_node_to_html_node(text_node):
    text_type_enum = TextType(text_node.text_type)
    match text_type_enum:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            if not text_node.url:
                raise ValueError('text node of type LINK needs a url')
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            if not text_node.url:
                raise ValueError('text node of type IMAGE needs a url')
            return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
        case _:
            raise Exception(f'Invlaid text type: {text_node.text_type}')

if __name__ == '__main__':
    main()

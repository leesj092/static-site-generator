from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue

        node_split = node.text.split(delimiter)
        for i in range(len(node_split)):
            if i % 2 == 0:
                if node_split[i] == '':
                    continue
                new_node = TextNode(node_split[i], TextType.TEXT)
                new_nodes.append(new_node)
            else:
                new_node = TextNode(node_split[i], text_type)
                new_nodes.append(new_node)

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

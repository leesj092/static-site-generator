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

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue

        text = node.text

        images = extract_markdown_images(node.text)

        if not images:
            new_nodes.append(node)

        for image in images:
            splits = text.split(f'![{image[0]}]({image[1]})')
            if splits[0] != '':
                new_nodes.append(TextNode(splits[0], TextType.TEXT))

            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = splits[1]

        if text != '':
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT.value:
            new_nodes.append(node)
            continue

        text = node.text
        print(f'text: {text}')

        links = extract_markdown_links(node.text)

        if not links:
            new_nodes.append(node)

        for link in links:
            splits = text.split(f'[{link[0]}]({link[1]})')
            print(f'splits: {splits}')
            if splits[0] != '':
                new_nodes.append(TextNode(splits[0], TextType.TEXT))

            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = splits[1]
            print(f'text is now: {text}')

        if text != '':
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)
    return matches

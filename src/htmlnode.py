class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html = ''

        if self.props:
            for prop in self.props:
                html += f' {prop}="{self.props[prop]}"'

        return html

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('Invalid HTML: leaf node has no value')
        if not self.tag:
            return self.value

        html = f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

        #if self.tag == 'img':
        #    html = html.replace('</img>', '')

        return html

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError('invalid HTML: parent node has no tag')
        if not self.children:
            raise ValueError('invalid HTML: parent node has no tag')

        children_html = ''
        for child in self.children:
            children_html += child.to_html()

        return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

    def __repr__(self):
            return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

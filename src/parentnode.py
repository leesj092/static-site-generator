from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        # no default bc I have a certain format in mind. dont judge
        if not children:
            raise ValueError('parent node must have children')

        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError('parent node must have tag')

        propHTML = self.props_to_html()

        if propHTML:
            html = f'<{self.tag} {propHTML}>'
        else:
            html = f'<{self.tag}>'

        html += ''.join([child.to_html() for child in self.children])

        html += f'</{self.tag}>'
        return html


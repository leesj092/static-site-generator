from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        # no default bc I have a certain format in mind. dont judge
        if not value:
            raise ValueError('leaf node must have value')

        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError('leaf node must have value')
        if not self.tag:
            return self.value

        propHTML = self.props_to_html()

        if propHTML:
            html = f'<{self.tag} {propHTML}>{self.value}</{self.tag}>'
        else:
            html = f'<{self.tag}>{self.value}</{self.tag}>'

        return html


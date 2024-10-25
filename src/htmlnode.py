class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(sefl):
        raise NotImplementedError()

    def props_to_html(self):
        html = ''

        if self.props:
            html = ' '.join([f'{key}="{value}"' for key, value in self.props.items()])

        return html

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

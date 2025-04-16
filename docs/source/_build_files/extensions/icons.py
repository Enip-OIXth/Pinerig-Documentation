from typing import Tuple, List

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.writers.html5 import HTML5Translator
from sphinx.util.docutils import SphinxRole


class bl_icon(nodes.container):
    pass


def visit_bl_icon(self: HTML5Translator, node: bl_icon):
    """Create a span element with associated CSS classes."""
    self.body.append(f'<span class="{" ".join(node["classes"])}"></span>')
    raise nodes.SkipNode()


class IconsRole(SphinxRole):
    """A interpreted text role to use icons in lines of text."""

    def run(self) -> Tuple[List[nodes.Node], List[nodes.system_message]]:
        path, classes = (self.text, "")
        if ";" in self.text:
            path, classes = self.text.split(";")[:2]
        class_list = [
            "bl-icons-{}".format(self.text),
        ]
        div = bl_icon(path, classes=class_list)
        return [div], []


def setup(app: Sphinx):
    app.add_role("bl-icon", IconsRole())
    app.add_node(bl_icon, html=(visit_bl_icon, None))

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

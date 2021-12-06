# -*- coding: utf-8 -*-
# This is free and unencumbered software released into the public domain.

from html.parser import HTMLParser

from docutils import nodes
from docutils.nodes import literal_block, raw
from sphinxcontrib.confluencebuilder.storage.translator import ConfluenceStorageFormatTranslator
from nbsphinx import AdmonitionNode, CodeAreaNode, FancyOutputNode

__version__='0.0.0-dev0'


class RawParser(HTMLParser):
    content = None

    def handle_starttag(self, tag: str, attrs):
        pass

    def handle_data(self, data: str):
        self.content = data

    def handle_endtag(self, attrs):
        pass


def visit_AdmonitionNode(self, node):
    if 'warning' in node['classes']:
        self.visit_warning(node)
    else:
        self.visit_note(node)


def depart_AdmonitionNode(self, node):
    if 'warning' in node['classes']:
        self.depart_warning(node)
    else:
        self.depart_note(node)


def _raw_to_literal_block(node: raw):
    parser = RawParser()
    parser.feed(node.rawsource)
    return literal_block(node.rawsource, parser.content)


def visit_CodeAreaNode(self: ConfluenceStorageFormatTranslator, node):
    child = node.children[0]
    if child.tagname == 'literal_block':
        child["language"] = "python"
        pass
    else:
        # ignore the latex node
        raw_node = [raw for raw in child.children if raw["format"] == "html"][0]
        output_literal = _raw_to_literal_block(raw_node)
        node.append(output_literal)
        pass


def depart_CodeAreaNode(self: ConfluenceStorageFormatTranslator, node):
    pass


def visit_FancyOutputNode(self : ConfluenceStorageFormatTranslator, node):
    pass


def depart_FancyOutputNode(self : ConfluenceStorageFormatTranslator, node):
    pass


def setup(app):
    app.require_sphinx('1.0')

    app.add_node(AdmonitionNode, confluence=
        (visit_AdmonitionNode, depart_AdmonitionNode), override=True)
    app.add_node(CodeAreaNode, confluence=
        (visit_CodeAreaNode, depart_CodeAreaNode), override=True)
    app.add_node(FancyOutputNode, confluence=
        (visit_FancyOutputNode, depart_FancyOutputNode), override=True)

# -*- coding: utf-8 -*-
# This is free and unencumbered software released into the public domain.
import os

extensions = [
    'nbsphinx',
    'sphinxcontrib.confluencebuilder',
    'sphinxcontrib.confluencebuilder_nbsphinx',
]

master_doc = 'index'
nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg'}",
    "--InlineBackend.rc=figure.dpi=96",
]
confluence_publish = True
confluence_publish_dryrun = False
confluence_space_key = os.getenv("CONFLUENCE_SPACE_KEY")
confluence_server_pass = os.getenv("CONFLUENCE_API_TOKEN")
confluence_server_url = os.getenv("CONFLUENCE_URL")
confluence_server_user = os.getenv("CONFLUENCE_USER")
confluence_page_hierarchy = True

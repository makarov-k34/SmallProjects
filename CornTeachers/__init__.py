"""Main entry point
"""
from pyramid.config import Configurator

import sys
sys.path.insert(0, 'CornTeachers')

def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("CornTeachers.views")
    return config.make_wsgi_app()


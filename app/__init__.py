# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.gene_info_controller import api as gene_info_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          version='1.0',
          title='Genes Suggestion API',
          description='A Genes Suggestion API'
          )

api.add_namespace(gene_info_ns, path='/gene_suggest')

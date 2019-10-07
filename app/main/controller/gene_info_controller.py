from flask import request
from flask_restplus import Resource

from ..util.dto import GeneSuggestDto
from ..service.gene_info_service import get_suggested_genes

api = GeneSuggestDto.api
_gene_info = GeneSuggestDto.gene_info


@api.route('')
class GenesList(Resource):
    @api.doc('suggested_genes')
    @api.marshal_list_with(_gene_info, envelope='data')
    @api.doc(
        params={
            'query': 'The Query typed by the user (e.g. BRC)',
            'specie': 'The specie (e.g. homo_sapiens)',
            'limit': 'Limit (Default: 10)'
        }
    )
    def get(self):
        """Genes Suggesting"""
        query = request.args.get('query')
        specie = request.args.get('specie')
        limit = request.args.get('limit')
        return get_suggested_genes(query, specie, limit)

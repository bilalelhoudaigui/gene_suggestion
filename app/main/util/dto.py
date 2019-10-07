from flask_restplus import Namespace, fields


class GeneSuggestDto:
    api = Namespace('GeneSuggest', description='Genes Information')
    gene_info = api.model('Gene suggest fields', {
        'display_label': fields.String(required=True, description='The name of the gene.'),
        'species': fields.String(required=True, description='The name of the species to which the gene belongs')
    })

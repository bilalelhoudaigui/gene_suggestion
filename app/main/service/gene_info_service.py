from app.main.model.gene_info import GeneSuggest
from flask_restplus import abort


def get_all_genes():
    return GeneSuggest.query.all()


def get_suggested_genes(query, specie, limit=10):
    if query is None or specie is None:
        abort(message="Error: The 'query' and 'specie' parameters are mandatory!")
    try:
        return GeneSuggest.query. \
            filter(GeneSuggest.display_label.startswith(query)). \
            filter_by(species=specie). \
            limit(limit).all()
    except Exception as e:
        abort(message="An Error has accured, please verify the filled parameters:"
                      " query={0}, specie={1}, limit={2}".format(query, specie, limit))

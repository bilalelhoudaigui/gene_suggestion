from .. import db


class GeneSuggest(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "gene_autocomplete"

    # 'primary_key=True' is added to avoid 'sqlalchemy.exc.ArgumentError'
    display_label = db.Column(db.String(255), nullable=False, primary_key=True)
    species = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '{} is the display_label. {} is the specie.'.format(self.display_label, self.species)

"""models for database"""
# pylint: disable=too-few-public-methods,invalid-name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Star(db.Model):

    """model for stars"""
    __tablename__ = 'stars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mass = db.Column(db.Float)
    luminosity = db.Column(db.Float)
    temperature = db.Column(db.Float)
    radius = db.Column(db.Float)
    exoplanets = db.relationship("Exoplanet", backref="star")
    constellation_id = db.Column(
        db.Integer, db.ForeignKey("constellations.id"))
    publication_id = db.Column(db.Integer, db.ForeignKey("publications.id"))

    def __repr__(self):
        return "<Star(name='%s', mass=%s, luminosity=%s, temperature=%s, radius=%s)>" % (
            self.name, self.mass, self.luminosity, self.temperature, self.radius)

    def search_result(self):
        """ Returns result format for the star """
        return {"model": "stars", "id": self.id}


class Exoplanet(db.Model):

    """model for exoplanets"""
    __tablename__ = 'exoplanets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    mass = db.Column(db.Float)
    radius = db.Column(db.Float)
    orbital_period = db.Column(db.Integer)
    year_discovered = db.Column(db.Integer)
    star_id = db.Column(db.Integer, db.ForeignKey("stars.id"))
    publication_id = db.Column(db.Integer, db.ForeignKey("publications.id"))

    def __repr__(self):
        return "<Exoplanet(name='%s', mass=%s, radius=%s, orbital_period=%d, "  \
            "year_discovered=%d)>" % (self.name, self.mass, self.radius,
                                      self.orbital_period, self.year_discovered)

    def search_result(self):
        """ Returns result format for the exoplanet """
        return {"model": "exoplanets", "id": self.id}


class Constellation(db.Model):

    """model for constellations"""
    __tablename__ = 'constellations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    abbrev = db.Column(db.String)
    family = db.Column(db.String)
    meaning = db.Column(db.String)
    area = db.Column(db.Float)
    stars = db.relationship("Star", backref="constellation")
    # bordering constellations

    def __repr__(self):
        return "<Constellation(name='%s', abbrev='%s', family='%s', "  \
            "meaning='%s', area='%s')>" % (self.name, self.abbrev,
                                           self.family, self.meaning, self.area)

    def search_result(self):
        """ Returns result format for the constellation """
        return {"model": "constellations", "id": self.id}


class Publication(db.Model):

    """model for publication"""
    __tablename__ = 'publications'

    id = db.Column(db.Integer, primary_key=True)
    ref = db.Column(db.String)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    authors = db.Column(db.String)
    journal = db.Column(db.String)
    abstract = db.Column(db.String)
    stars = db.relationship("Star", backref="discovered_by")
    exoplanets = db.relationship("Exoplanet", backref="discovered_by")

    def __repr__(self):
        return "<Publication(title='%s', year=%s, authors='%s', journal='%s', abstract='%s')>" % (
            self.title, self.year, self.authors, self.journal, self.abstract)

    def search_result(self):
        """ Returns result format for the publication """
        return {"model": "publications", "id": self.id}

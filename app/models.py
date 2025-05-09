from app import db

class HondaType(db.Model):
    __tablename__ = 'honda_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    alternatives = db.relationship('Alternatives', backref='honda_type')
    alternative_comparisons = db.relationship('AlternativeComparison', backref='honda_type')

    def __init__(self, name):
        self.name = name

class Criteria(db.Model):
    __tablename__ = 'criteria'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    alternative_comparisons_criteria = db.relationship('AlternativeComparison', backref='criteria')

    def __init__(self, name):
        self.name = name

class Alternatives(db.Model):
    __tablename__ = 'alternatives'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    honda_type_id = db.Column(db.Integer, db.ForeignKey('honda_types.id'), nullable=False)
    alternative_comparisons_alternative1 = db.relationship('AlternativeComparison', foreign_keys='AlternativeComparison.alternative1_id', backref='alternative1')
    alternative_comparisons_alternative2 = db.relationship('AlternativeComparison', foreign_keys='AlternativeComparison.alternative2_id', backref='alternative2')

    def __init__(self, name, honda_type_id):
        self.name = name
        self.honda_type_id = honda_type_id

class AlternativeComparison(db.Model):
    __tablename__ = 'alternative_comparisons'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    alternative1_id = db.Column(db.Integer, db.ForeignKey('alternatives.id'), nullable=False)
    alternative2_id = db.Column(db.Integer, db.ForeignKey('alternatives.id'), nullable=False)
    criteria_id = db.Column(db.Integer, db.ForeignKey('criteria.id'), nullable=False)
    preference_value = db.Column(db.Float, nullable=False)
    honda_type_id = db.Column(db.Integer, db.ForeignKey('honda_types.id'), nullable=False)

    def __init__(self, alternative1_id, alternative2_id, criteria_id, preference_value, honda_type_id):
        self.alternative1_id = alternative1_id
        self.alternative2_id = alternative2_id
        self.criteria_id = criteria_id
        self.preference_value = preference_value
        self.honda_type_id = honda_type_id
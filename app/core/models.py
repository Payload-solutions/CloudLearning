from app import db

class YogurtData(db.Model):

    __tablename__ = "YogurtData"
    features_id = db.Column(db.Integer, primary_key=True)
    streptococcus_initial = db.Column(db.Float, index=True, nullable=False)
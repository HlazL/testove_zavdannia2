import db

class Users(db.Model):
    __tablename__ = "users"
    # table column id
    id = db.Column(db.Integer, primary_key=True)
    # table column name with data type of String
    name = db.Column(db.String(100), unique=True, nullable=False)
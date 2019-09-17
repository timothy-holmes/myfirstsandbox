from datetime import datetime
from app import db, login
        
class Sand(db.Model):
    __tablename__ = 'sand'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    message = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime, index=True)
    #sand_id = db.Column(db.Integer, db.ForeignKey('sand.id'))
    #replies = db.relationship('Sand', backref='ohpee', lazy='dynamic')
    
    def __init__(self,title,message,sand_id=None):
        # id is automatic, sand_id is optional
        self.timestamp = datetime.utcnow()
        self.title = title
        self.message = message
        # self.sand_id = sand_id

    def __repr__(self):
        return '<Sand {}-{}>'.format(self.title,self.message)
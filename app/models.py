from datetime import datetime
from app import db, login
        
class Sand(db.Model):
    __tablename__ = 'sand'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    message = db.Column(db.String(1024))
    timestamp = db.Column(db.DateTime, index=True)
    og_sand = db.Column(db.Integer, db.ForeignKey('sand.id'))
    replies = db.relationship('Sand', backref=db.backref('sand', remote_side=[id]))
    
    def __init__(self,title,message,sand_id=None):
        # id is automatic
        self.timestamp = datetime.utcnow()
        self.title = title
        self.message = message
        
    def __repr__(self):
        return '<Sand {}-"{}">'.format(self.id,self.title)
    
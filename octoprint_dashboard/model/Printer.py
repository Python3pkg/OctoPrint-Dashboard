from octoprint_dashboard import db
from octoprint_dashboard.model import Group

printer_group = db.Table('printer_group',
                         db.Column('printer_id', db.Integer, db.ForeignKey('printer.id')),
                         db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
                         )


class Printer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    apikey = db.Column(db.String(80))
    ip = db.Column(db.String(80))
    group = db.relationship(Group, secondary=printer_group,
                             backref=db.backref('printer', lazy='dynamic'), lazy="dynamic")

    def __init__(self, name, apikey, ip):
        self.name = name
        self.apikey = apikey
        self.ip = ip

    def __repr__(self):
        return '<Printer %r>' % self.name

    def __hash__(self):
        return hash(self.id)
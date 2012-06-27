from google.appengine.ext import db


class Offender(db.Model):
  number = db.IntegerProperty()
  statement = db.TextProperty()
  name_last = db.StringProperty()
  name_first = db.StringProperty()
  offender_id = db.IntegerProperty()
  age = db.IntegerProperty()
  date = db.DateProperty()
  race = db.StringProperty()
  county = db.StringProperty()

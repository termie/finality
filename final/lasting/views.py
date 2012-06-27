from django import template
from django import shortcuts
from django.template import loader

from google.appengine.ext import db

from final import models

def index(request):
  #t = loader.get_template('templates/index.html')
  #c = template.RequestContext(request, locals())
  offenders = db.GqlQuery('SELECT * '
                          'FROM Offender '
                          'ORDER BY number')
  return shortcuts.render_to_response('templates/index.html', locals())

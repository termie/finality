from django import template
from django import shortcuts
from django.template import loader

from google.appengine.ext import db

from final import models

DECLINED = 'This offender declined to make a last statement.'

def index(request):
  #t = loader.get_template('templates/index.html')
  #c = template.RequestContext(request, locals())
  offenders = db.GqlQuery('SELECT * '
                          'FROM Offender '
                          'ORDER BY number '
                          'LIMIT 20')
  offenders = [x for x in offenders
               if x.photo or x.statement != DECLINED]
  return shortcuts.render_to_response('templates/index.html', locals())
import random

from django import template
from django import shortcuts
from django.template import loader

from google.appengine.api import memcache
from google.appengine.ext import db

from final import models

DECLINED = 'This offender declined to make a last statement.'

def _get_data():
  data = memcache.get("shown_offenders")
  if data is not None:
    return data
  else:
    #offenders = db.GqlQuery('SELECT photo, statement, name_first, name_last, '
    #                        '       age, county '
    #                        'FROM Offender '
    #                        'WHERE show = True '
    #                        'ORDER BY number ')
    offenders = db.GqlQuery('SELECT * '
                            'FROM Offender '
                            'WHERE show = True '
                            'ORDER BY number ')
    offenders = list(offenders)
    memcache.add("shown_offenders", offenders)
    return offenders

def _get_single(number):
  number = int(number)
  data = memcache.get("offender_%s" % number)
  if data is not None:
    return data
  else:
    offender = models.Offender.get_by_key_name(str(number))
    memcache.add("offender_%s" % number, offender)
    return offender

def index(request):
  #t = loader.get_template('templates/index.html')
  #c = template.RequestContext(request, locals())
  offenders = _get_data()
  random.shuffle(offenders)
  # Don't show photos for those without statements.
  #offenders = [x for x in offenders
  #             if x.photo and x.statement != DECLINED]
  # Or do
  #offenders = [x for x in offenders
  #             if x.photo or x.statement != DECLINED]
  return shortcuts.render_to_response('templates/index.html', locals())

def individual(request, number):
  offenders = [_get_single(number)]
  return shortcuts.render_to_response('templates/individual.html', locals())

import json
import os
import sys

from final import models

data = json.load(open('parsed.json'))

DECLINED = 'This offender declined to make a last statement.'

for x in data:
  if not x['statement_full']:
    x['statement_full'] = DECLINED
  m = models.Offender(key_name=x['order'],
                      number=int(x['order']),
                      statement=x['statement_full'],
                      name_last=x['last'],
                      name_first=x['first'],
                      offender_id=int(x['tdcj']),
                      age=int(x['age']),
                      race=x['race'],
                      county=x['country'])
  photo_path = 'texas/%s%s.jpg' % (x['last'], x['first'])
  photo_path = photo_path.replace(' ', '').replace(',', '').lower()
  if os.path.exists(photo_path):
    m.photo = photo_path
  m.save()

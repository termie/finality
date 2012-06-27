import json

from final import models

data = json.load(open('parsed.json'))

for x in data:
  m = models.Offender(key_name=x['order'],
                      number=int(x['order']),
                      statement=x['statement_full'],
                      name_last=x['last'],
                      name_first=x['first'],
                      offender_id=int(x['tdcj']),
                      age=int(x['age']),
                      race=x['race'],
                      county=x['country'])
  m.save()

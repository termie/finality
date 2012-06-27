import json
import pprint

from bs4 import BeautifulSoup as bs


def parse_offenders(s):
  soup = bs(s)
  trs = soup.find_all('tr')
  o = []
  fields = ['order', 'info', 'statement', 'last', 'first', 'tdcj', 'age', 'date', 'race', 'country']
  for x in trs:
    fieldnames = fields[:]
    tds = x.find_all('td')
    l = []
    for td in tds:
      al = td.find_all('a')
      if al:
        l.append(al[0]['href'])
      else:
        l.append(td.string)

    out = dict(zip(fieldnames, l))
    o.append(out)

  o = [x for x in o if x]

  for offender in o:
    g = open(offender['statement']).read()
    offender['statement_full'] = parse_statement(g)

  return o


def parse_statement(s):
  soup2 = bs(s)
  states = soup2.find_all('p')
  if not states:
    return ''

  state = states.pop(0)
  while states:
    if state.string == 'Last Statement:':
      break
    state = states.pop(0)

  string_states = [list(x.stripped_strings) for x in states]
  string_states = [item for sublist in string_states for item in sublist]
  statement = '\n'.join(string_states)
  statement = statement.replace(u'\u2019', "'")
  return statement


def main():
  f = open('dr_executed_offenders.html').read()
  p = parse_offenders(f)
  print json.dumps(p)


if __name__ == '__main__':
  main()

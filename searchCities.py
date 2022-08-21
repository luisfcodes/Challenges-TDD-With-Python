cityList = ['Paris', 'Budapeste', 'Skopje', 'Rotterdam', 'Valencia', 'Vancouver', 'Amsterdam', 
'Vienna', 'Sydney', 'New York City', 'London', 'Bangkok', 'Hong Kong', 'Dubai', 'Rome', 'Istanbul']

citySearch = []

def searchCities(search):
  if len(search) < 2:
    return False
  
  for x in cityList:
    if x.startswith(search):
      citySearch.append(x)
  
  return citySearch
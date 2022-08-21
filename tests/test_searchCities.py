from searchCities import searchCities

def test_should_return_empty_for_searches_with_less_than_two_characters():
  assert searchCities('a') == False

def test_should_return_search_results():
  assert searchCities('Va') == ['Valencia', 'Vancouver']
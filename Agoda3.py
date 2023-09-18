def derive_billboard_price(your_company_name, other_company_names, other_company_prices):
  """Derives the price of a billboard featuring the name of a company.

  Args:
    your_company_name: A string representing the name of your company.
    other_company_names: A list of strings where each element is the name of
      another company.
    other_company_prices: A list of real numbers where other_company_prices[i]
      is the price of other_company_names[i].

  Returns:
    The price of your company name if it can be derived, otherwise -1.
  """

  letter_prices = {}
  for i in range(len(other_company_names)):
    company_name = other_company_names[i]
    company_price = other_company_prices[i]

    for letter in company_name:
      if letter not in letter_prices or letter_prices[letter] > company_price:
        letter_prices[letter] = company_price

  billboard_price = 0
  for letter in your_company_name:
    if letter not in letter_prices:
      return -1

    billboard_price += letter_prices[letter]

  return billboard_price
print(derive_billboard_price("aabc", ["ab", "ac", "bd"], [99.5, 1000.2, 2000.8]))


derive_billboard_price("d", ["aab", "acc"], [500, 6000])


derive_billboard_price("bc", ["aa", "ab", "bb", "ac", "cc"], [2, 3, 4, 4, 6])

derive_billboard_price("aabc", ["ab", "ac", "ad"], [10, 100, 1000])

derive_billboard_price("a", ["abcdefgh"], [10])

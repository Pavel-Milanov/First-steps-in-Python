import re

regex = r"(USD|\$) *(([\d]+)([\.,][\d]{2}))?"

test_str = (" $ 14899.00\n"
            " $ 23.76\n"
            " USD 12.00\n\n\n")
currency_coeff = {"BGN": 2, "EUR": 1.3}
chosen_currency = "BGN"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    # print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
    #
    #                                                                    end=match.end(), match=match.group()))
    try:
        dollarPrice = float(match.group(2))
        newPrice = dollarPrice * currency_coeff[chosen_currency]
        print("USD {dollars} is {currency} {newPrice} ".format(dollars=dollarPrice, currency=chosen_currency,
                                                               newPrice=newPrice))
    except KeyError as e:
        print("Currency {cur} not found. ".format(cur=chosen_currency))
        exit(0)
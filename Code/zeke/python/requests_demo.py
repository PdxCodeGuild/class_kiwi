import requests


response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/kiwi")

print(response.text)
word = response.json
print(type(word))


     # self.deposit = deposit
        # self.check_withdrawl = check_balance
        # self.withdraw = withdraw
        # self.calc_intrest =calc_intrest
    

    # def interest():
    #     interest += 0.01
    #     return interest()

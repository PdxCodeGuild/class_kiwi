'''         +-+#^#+--+#^#+--+#^#+-+             
             Project: Quotes API                  ░░╚══╗░╔═╔════╝
                 Version: 1.00                    ╚═╦═╗╠═╩═╩╗╔═╦═╗
             Author: Colton Tatum                 ░░║▒╠╣▒▒▒▒╠╣▒║▒║
          Email: TatumC4561@gmail.com             ╔═╩═╝╠═╦═╦╝╚═╩═╝
                 Date: 3/1/22                    ░░╔══╝░╚═╚════╗
            +-+#^#+--+#^#+--+#^#+-+
'''

import requests



# Access API and create user to get access to user token needed for each session

# user_token = requests.post("https://favqs.com/api/users", headers={"user":{"login": "woof", "email": "dogsock@gmail.com", "password": "woof"}})

# The URL to get a random quote is https://favqs.com/api/qotd, send a request here, 

def random_quote():
    """Pulls random quote from https://favqs/com/api/qotd"""
    response = requests.get("https://favqs.com/api/qotd", headers = {"Accept" : "application/json"})

    # get json file from website
    quote_json = response.json()

    # parse the JSON in the response into a python dictionary
    author_quote = {"Author":quote_json['quote']['author'], "Quote" : quote_json['quote']['body']}


    quote = "Author: " + author_quote["Author"] + "\nQuote: " + author_quote["Quote"]

    # show the quote and the author.
    return quote



def find_quote():
    """Pulls quotes by subject from https://favqs/com/api/qotd"""
    # parse the JSON in the response into a python dictionary
   
    while True:

        user_keyword = input("Enter an author to recieve a quote, or 'exit' to leave program\n")
        
        if user_keyword == "exit":
            exit()
        
        else:     
            try:    
                keyword_form = user_keyword.replace(" ", "+")
                response = requests.get(f'https://favqs.com/api/quotes/?filter={keyword_form}&type=author', 
                headers = {'Accept' : 'application/json', 
                            'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'
                    })

                # get json file from website
                quote_json = response.json()
                i = 0 # index of quote
                
                while True:
                    try:
                        author = quote_json['quotes'][i]['author']
                        quote = quote_json['quotes'][i]['body']
                        i += 1
                   
                    
                        q_a = "Author: " + author + "\nQuote: " + quote
                        # show the quote and the author.
                        print(q_a)
                    
                        answer = input(f"Would you like to here another quote from {user_keyword}? Yes or No.\n").lower().strip()
                        if answer == 'no':
                            break
                        else:
                            continue
                    
                    except IndexError: 
                        print("That was all of the quotes.")
                        break

            except KeyError:
                print(f"{user_keyword} does not exist.")









def main():
    
    
    print(random_quote())
    print(find_quote())


if __name__ == "__main__":
    main()
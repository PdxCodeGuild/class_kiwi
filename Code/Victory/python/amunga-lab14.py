import requests

lab_req = requests.get("https://icanhazdadjoke.com", headers={
    'Accept': 'application/json'
})

print(lab_req)
lab_14 = lab_req.json()
# print(lab_14)
print(lab_14['joke'])


while True:
    search_term = input("Please enter a search term, you may type 'exit' at anytime to exit: ")
   
    
    
    if search_term == 'exit':
        break
    else:
        lab_version_two = requests.get(f"https://icanhazdadjoke.com/search?term={search_term}", headers={ 'Accept': 'application/json'})
        ver_two = lab_version_two.json()

        print(ver_two['results'][0]['joke'])

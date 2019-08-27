import requests
import pyfiglet
import termcolor
from random import choice

header = pyfiglet.figlet_format("Dad Joke 3000")
header = termcolor.colored(header, color="magenta")
print(header)
user_input=input("let me tell u a joke!give me a topic:")
response_json=requests.get("https://icanhazdadjoke.com/search",
                           headers={"Accept":"application/json"},
                           params={"term":user_input}).json()
nums_jokes=response_json['total_jokes']
result=response_json["results"]
if nums_jokes>1:
    print("There are many jokes and one that is:)")
    print(choice(result)['joke'])
elif nums_jokes==1:
    print("There is one joke for you:)")
    print(result[0]["joke"])
else:
    print("Sorry there is no joke on this topic:(")


from auction_function import logo

print(logo)
diction = {}
winner = ''
get_name = input("What is your name?: ")
get_bid = int(input("What's your bid?: $"))
get_next = input("Are there any other bidders? Type 'Yes' or 'No' \n")
diction[get_name] = get_bid
while get_next == 'Yes':
    get_name = input("What is your name?: ")
    get_bid = int(input("What's your bid?: $"))
    get_next = input("Are there any other bidders? Type 'Yes' or 'No' \n")
    def get_all(name, bid):
        diction[get_name] = get_bid
get_all(name=get_name, bid=get_bid)
if get_next == "No":
      winner = max(diction, key=diction.get)
      new_value = diction.values()
      max_value = max(new_value)     

print(f"The Winner is {winner} with a bid of ${max_value}")
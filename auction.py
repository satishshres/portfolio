def find_highest_bidder(bidding_dictionary):
    """
    Function to find the highest bidder and print the result.
    """
    winner = ""
    highest_bid = 0
    for bidder, bid_amount in bidding_dictionary.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\n🎉 The winner is {winner} with a bid of ${highest_bid}!")

def start_auction():
    """
    Function to manage the auction process.
    """
    print("Welcome to the Auction Program! 🏆")
    bids = {}
    continue_bidding = True
    min_bid_increment = 10  # Minimum bid increment

    while continue_bidding:
        name = input("\nWhat is your name? ").strip()
        
        # Validate bid input
        while True:
            try:
                price = int(input(f"Hello {name}, what is your bid? $"))
                if price > 0:
                    if not bids or price >= max(bids.values()) + min_bid_increment:
                        break
                    else:
                        print(f"Your bid must be at least ${max(bids.values()) + min_bid_increment}. Please try again.")
                else:
                    print("Bid must be greater than 0. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number for your bid.")
        
        # Add bid to the dictionary
        bids[name] = price
        
        # Check if there are more bidders
        while True:
            should_continue = input("Is there another bidder? Type 'yes' or 'no': ").strip().lower()
            if should_continue in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please type 'yes' or 'no'.")
        
        if should_continue == "no":
            continue_bidding = False
            find_highest_bidder(bids)
        elif should_continue == "yes":
            # Clear the console for the next bidder (simulated)
            print("\n" * 50)

# Start the auction
start_auction()

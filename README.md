# parkingTickets

Allows for easier interaction with the Evanston, IL parking ticket payment site. This script will pay your tickets for you (since the Evanston site doesn't allow for account creation or info saving) if you just replace the DELETED lines in parkingTickets.py with your personal info as specified in the comments next to each DELETED line. 

It now keeps track of all tickets that it sees, and is able to graph the total amount of money you spent on parking tickets in one month in a plotly graph. The graphing itself is all handled offline, so no need for an API key or anything.

# Dependencies
* selenium
* chromedriver
* numpy (Graphing only)
* plotly (Graphing only)

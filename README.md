# Trade Crypto on Twitch!

## Current tasks:
chatbot
smartcontracts
tradeserver
visualizer
donations

## General Design:

## Here's a rough outline of how it would work, subject to change.

### The chatbot interfaces with twitch IRC. It is responsible for:
* Tallying votes
* Submitting trades to tradeserver (*many options*)
* Chatting when a new voting round begins / ends
* Provide an interface to publish vote counts in real time to database? probably last thing required

### The tradeserver is responsible for:
* Exposing a REST post url to execute trades
* Keeping track of current positions in the database
* Possibly some verification logic to make sure no stupid trades are made

### Smart contracts will fundraise the initial investment.

### The visualizer will provide the viewport for the stream
* Show current positions
* Show current voting results
* Show an advertisement from donations?

I recommend a real time binding framework for this such as meteorjs + react (react is preference but default is good too)

### Donation collector will make income a thing (todo)

# let's do this

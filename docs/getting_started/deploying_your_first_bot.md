# Deploying your first Hiven-Bot

---

!!! Warning

    **This documentation page is not finished yet! Information can be outdated or entirely not available!**


Deploying a Bot is very easy and quick in OpenHiven.py while also very customisable.
With the ability to pass your own EventHandler and also customise handling and connection attributes you have
control on how exactly your Bot should run. Currently, due to the early Development Stage of some features
some might fail when using, if such a thing happens please report these on the Github Page.

## Authentication and Tokens

As already shown in examples on the page [Intro to OpenHiven.py](./intro.html) to use a bot, you need to pass
a Token to authorise and connect to Hiven. This token is a key to the account that the Client will be
using to interact with the Hiven Platform. Therefore, OpenHiven.py cannot run without it, since its
features depend on such token! Because of that and the risk of other users taking over your account, it is
crucial to keep such a token save and not share it on any platform! Doing that could risk that your entire
account getting compromised! So try to keep it save!

![OpenHiven.py Authentication](../assets/images/openhivenpy_auth-dark.png){: width=900px align=center }

### Getting a User-token
Step 1: Open your browsers development options.
Step 2: Navigate to "Applications" "Storage" "Local Storage" "(canary.)hiven.io"
Step 3: Copy the "hiven-auth" string. It has to be 128 characters long.
Step 4: Don't show your token to anyone. With a token you can get full access to your account even without a password.

### Getting a Bot-token



## Setting up a simple Bot

Setting up a simple Bot is relatively easy and quick. Choose the right Client-Type, pass a token, customise events and 
let the bot run. Still, for each Client-Type there are multiple things to know before running:

* **UserClient:**

    A UserClient is a Client specifically made for User-Interaction using a User-Account on Hiven! That means it accesses 
    the entire account and has full access to the Users data. A UserClient is useful for testing and experimenting with 
    OpenHiven.py, but not recommended for longer run-times! Since using a user-account can be not very secure, we advise 
    you to create a Bot on Hiven if possible!

* **BotClient:**
    
    A BotClient is a Client targeted at Bots! That means it has special functionality directed
    to Bot-Usage and long time execution! That also means user interaction functionality is missing and classic
    relationships with Users are not supported! 

### Creating a Bot-Account

### Setting up a simple EventListener

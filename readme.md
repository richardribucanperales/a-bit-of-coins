##Python Bitcoin Checker

This is a web tool that checks the amount of how much USD equals to 1 bitcoin. As you know, cryptocurrency is like all other currency in the world. It is changing everyday and this tool is designed to grab that information and display it to you without having to get it from a website.

##How it is constructed

What my tool does is it opens the target webpage, which is: https://coinmarketcap.com/currencies/bitcoin/ and uses the module "Beautiful Soup" to grab the attributes containing the information. It then gets the date from your local machine and prints it through the CLI. Not only does it do that, it also prints the output to a log file named "logs.txt." If you want to keep track of how much bitcoin rises or falls, then the log file is what you should look at.

##How to use it

First, you need to install python 2.7. This script is built under python 2.7. Once you install, follow the steps illustrated on this website: https://www.pythoncentral.io/execute-python-script-file-shell/
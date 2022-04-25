# Password-Locker
##### By James Musembi
### This is an application for securing account passwords
## Table of Content

+ [Description](#description)
+ [Installation Requirements](#installation)
+ [Technology Used](#technology-used)
+ [Behaviour Driven Development](#behaviour-driven-development)
+ [Reference](#reference)
+ [License](#license-Copyright)
+ [Authors Info](#author-Info/contacts)

## Description
This is an application written in python in which a user can create an account and store account passwords in it and retrieve them when needed.
## Set-up/Installation 

### Requirements
* Either a computer,phone,tablet or an Ipad
* An access to the Internet
### Installation
* Clone the github repo
* Open the terminal
* On the terminal run the command ./run.py to open the application
* Follow prompts
## Technology Used
* Python3.9- to impliment the functionality of the application.


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ python3.9 run.py```|Hello welcome, Enter your name to create an account <br>* CA ---  Create New Account * L |
|Select  GP| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select LI  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```DEL```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```EX```| exits appliation|

[Go Back to the top](#password-locker)

## License -Copyright 

MIT License

Copyright © license 2022 ,James Musembi, student Moringa school.


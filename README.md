# Author
Written by Guille Gregoire and Hoummadi Selim,
currently students at the IUT of Amiens.


# How to use this project ?

## Git

### Install git
Follow instruction on the following website, depending of your OS

[Download git](https://git-scm.com/downloads)
### Clone project
When you have git installed, you simply have to enter the following command :

```
git clone https://github.com/Aszriel/FlowReaderWebSite.git
```


## How to run the project
### __Create the tables__
Simply run the command :
```
Flask initdb
```
### __Drop the tables__
```
Flask dropdb
```
### __Create sample user__
```
Flask createuser
```
__This command create an user toto with the password tutu and an user thor with password flash__

Note that you have to create the tables with the command ```Flask initdb``` in order to create an account.




# Analyzing Instagram Pages
## Version 1.0

The purpose of this project is to pull relevant data from 1 or more instagram pages, data such as follower, following, number of posts and varous metrics of likes for posts made on each page. 

### Python Dependencies
	* Python 3.7
	* Pipenv
	* Selenium
	* CSV(Comma Separated Values)

## Enivronment Setup

```bash

$ pipenv shell
$ pipenv install 
$ ./pullData.py <instagram-account(s)-textfile>

```

## Descripton of Output

It shall output a csv file which can be accessed or edited through a normal text editor or a spreadsheet application such as Microsoft Excel or Google Docs. Where each account's name will be given an ID and paired with their relevant account data. 

## Limitations 
	* Currently base code only retrieves the first 24 posts
	* Numbers scrapped from the web pages are not the accurate counts
	* Mix of video views and likes in the case of a media post with video

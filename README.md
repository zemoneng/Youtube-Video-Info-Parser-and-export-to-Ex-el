# Youtube Video Info Parser and export to Excel file

This is a code for collecting statistics number of views (also other information) of videos from any channels on Youtube. You give a list of Youtube pages with videos, and the output is an Excel spreadsheet with data.

____

I'm using python 3.8 interpreter.
____

## Installing modules first

I'm using Pycharm. So to start working code you need to install a few python libraries. If you're using Anaconda or something you also can install that libraries if you don't have it: 
- Create your Pycharm project
- go to Pycharm/Preferences... 
- and choose Pycharm interpreter: Pythom 3.8.

go to Terminal in your project:

1. install requests library, to do that enter this line in the terminal:
```
pip install requests
```

2. You need BeautifulSoup library to parse http-pages, but first you need lxml, so enter:
```
pip install lxml
```
and then
```
pip install bs4
```
(BeautifulSoup not working without lxml library)

3. For reading and writing Excel files you need openpyxl:
```
pip install openpyxl
```
and pandas
```
pip install pandas
```

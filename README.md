# Youtube Video Info Parser and export to Excel file

This is a code for collecting number of views (also other information) of videos from any channels on Youtube. You give a list of Youtube pages with videos and the output is an Excel spreadsheet file with data.

____


## Installing modules first

To start working code you need to install a few python libraries (if you're using Anaconda or something you need to check is this libraries already install). I'm using Pycharm, if you do so:
- Create your Pycharm project
- go to Pycharm/Preferences... 
- and choose Pycharm interpreter: Pythom 3.8.

go to the Terminal in your project:

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

_____

Now open py file, add URL's inside the list_of_urls. Run the code. 

Done. Check your result file.

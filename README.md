# x-spider

x-spider is a fully comprehensive data gathering suite of tools
designed to collect all data from a 'target ur' .

Primary use : cybersecurity. 

After running the spider/crawler on any given domain or url you 
will have a folder containing a complete data set of the 'attack surface'
mapped.
********************************************************************************************************
method : Add the target url to the ```example.env``` file and rename the file
         ```.env```

then run ```python data.py```
an output folder is created containing ```data.json``` file.

the data in ```data.json``` can be visualized by running 
```python data-viz.py```  creating a .png file for visual interpretation.

```whois-lookup.py``` provides the dns registration data as a .json file in 
the output folder.

The vizualizations include a 'tree map' , 'word cloud' , 'website structure',
url length 'bar chart' .

comments can be extracted from comments sections (.json)
text is extracted from the url (.txt)
an 'output.json' is created from 'output.json' which then 
creates a 'output.html' of all external and internal links
as clickable links .

Data is gathered for analysis to the output folder.

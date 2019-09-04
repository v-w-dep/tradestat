# tradestat
tradestat is a Python module to generate meaningful reports of HK's external merchandise trade statistics from numerical raw data issued by authorized department.

- 4 types of reports are provided
- HK's external merchandise trade by currency (HKD, USD) and dollar units (thousand, million) with: 
1) World   (total number:   1) 
2) Region  (total number:  16)
3) Area    (total number:   9)
4) Country (total number: 214)

### Developing or suggested working environment: 
- Python version 3.6 or above
- Window 10

### Dependencies: 
1) [pandas](https://github.com/pandas-dev/pandas) 
2) [NumPy](https://www.numpy.org)
3) [xlrd](https://github.com/python-excel/xlrd)
4) [openpyxl](https://openpyxl.readthedocs.io/en/stable/index.html)
5) [pyprind](https://github.com/rasbt/pyprind)
6) [pypiwin32](https://github.com/mhammond/pywin32); try pip install pywin32 or pip install pypiwin32

### Instruction to use:
1) Run one of the world.py, region.py, area.py, country.py each time
2) Enter start year, end period, number of products to display 
3) Process can be tracked by the pyprind percentage indicator 
4) Reports in Excel format will be generated in a new folder "Output"

#### Instruction video:
- world   
[![link not valid](http://img.youtube.com/vi/xAyWChMQHxM/0.jpg)](http://www.youtube.com/watch?v=xAyWChMQHxM "tradestat instruction: world")
- region  
[![link not valid](http://img.youtube.com/vi/18e0Umq5fPo/0.jpg)](http://www.youtube.com/watch?v=18e0Umq5fPo "tradestat instruction: region")

### Trade statistics raw data definition:
A few of periods of raw data in DAT format to demonstrate, and description file can be found [here](https://github.com/oda-developer/tradestat/tree/master/C%26SD_raw_data) in this repository

### Examples:
Full completed reports in Excel format as examples can be downloaded in [Output_completed_as_example](https://github.com/oda-developer/tradestat/tree/master/Output_completed_as_example) in this repository

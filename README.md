This code pull data from the following API 'https://covid-api.com/api/reports. 
Swagger doc of the api: https://covid-api.com/api/


config.ini in the root foolder of the project serves as input which has path to input.xls and response.xlsx files. 

input.xls is read as date,iso and an api call is made to the URL above. 

Response is Covid-19 data for all provinces/states in a country. 

The solution merges confirmed, deaths, recovered from all provinces together and collates them at the country level. 


****TO EXECUTE PROGRAM*****


1. Install dependencies:
       pip install -r requirements.txt1. Install all the needed dependencies as given in requirements.txt

**2**
 
Goto the root dir of the project in a terminal window and run

python covid_data_merger.py 
or
python3 covid_data_merger.py 

based on what python is installed on the machine. 



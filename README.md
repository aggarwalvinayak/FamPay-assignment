# FamPay-assignment

## TO RUN
  After cloning the Repositery
1. `cd YoutubeSearch` #move into the project directory
2. `pip3 install -r requirements.txt` #install the requirments (Requires python3 pre installed)
3. `python3 manage.py runserver`

## Using the App
In the Browser open the URL mentioned on the terminal (usually `127.0.0.1:8000` )
1. `127.0.0.1:8000/videos` contains the required GET API. REST Framework will directly let you test from the browser.
PARAMETERS(optional):

   a. `page` (default=1) : Page Number wanted

   b. `page_size` (default=10) : Results per page required
   
   Example : `127.0.0.1:8000/videos/?page=2&page_size=8`

2. `127.0.0.1:8000/admin` contains the admin panel. Username: *admin* Password: *pass1234*

   Go to YoutubeSearch->Videos for the Dashboard (Also contains filters for sorting/slicing etc.)

Also Supports multi API Key use. Check CONSTANTS in views.py



  

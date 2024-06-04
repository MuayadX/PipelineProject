this how it has to be but it is not gonna work : 
pip install psycopg2-binary -t .
that's why we need to get the (folder) library from this link : 
https://github.com/jkehler/awslambda-psycopg2/tree/master 
download the folder psycopg2-3.9 and change the name to psycopg2 and add to the folder 
of the function file here  is "savelambda_crypto_data" and zip it and upload it to awslambda

make sure under the runtime setting in lamda function console to choose python 3.9
and for the handler modify it as filename.functionname ex: 
save_crypto_data.save_crypto_data
name of the python file . name of the function inside it 

for the terminal : 
go to the folder of the files and open in intgreated terminal 
zip -r savelambda_crypto_data.zip .

other approach is to build an envirment for linux2 on AWS and download python and psycopg2
to it and get "dependancies.zip" download it and upload to aws as a layer to the lambda function 
here is a video : 
https://www.youtube.com/watch?v=80h9lXE07z0&ab_channel=ZyroTech

make sure under the runtime setting in lamda function console to choose python 3.8


make sure to modify the time out from: configuration - general configuration. to 30 seconds 
instread of 3 seconds for both functions 

for the environment variables make sure not to add any quotes to variables ex : 
host	 monorail.proxy.rlwy.net (with no quotes)

dont forget to add ['responsePayload'] to get the data from the event of the 1st function to the code ex; 
data = json.loads(event['responsePayload']['body'])

to be impored 
import json
import psycopg2
import os



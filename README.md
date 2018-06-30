# XIOT_TASK
XIOT fullstak internship filtration task

- cd to the project folder
- Make sure to install requirements found in (requirements.txt) using: 

				pip3 install -r requirements.txt
				
- Activate virtual enviroment : 

				source venv/bin/activate
				
- set FLASK_APP attribute by typying: 

				FLASK_APP=app.py
				
- on the commandline while venv activated type:

				flask run
				
- it should say: running on 127.0.0.1:5000 open that url
- now that should work fine and you see the design of the website
- Enter your data and hit connect
EXAMPLE : 

	HOST:"localhost"
	
	Port:1883
	
	username:"demo"	
	
	password:"123"
	
	topic:"test"
	
	message:"tst"
	
Now it should connect well in mqtt protocol flashs : "host" "connected successfully"

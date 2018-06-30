from flask import Flask,render_template,request,flash,redirect,url_for
import time
import os
import paho.mqtt.client as mqtt
import urllib.parse as urlparse

clients=[]

app = Flask(__name__)
app.secret_key = 'some_secret'
# app.config.from_object(Config)

@app.route('/',methods = ['POST', 'GET'])



# class ContactForm(Form):
#    name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
#    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
#    Address = TextAreaField("Address")
   
#    email = TextField("Email",[validators.Required("Please enter your email address."),
#       validators.Email("Please enter your email address.")])
   
#    Age = IntegerField("age")
#    language = SelectField('Languages', choices = [('cpp', 'C++'), 
#       ('py', 'Python')])
#    submit = SubmitField("Send")



# def contact():
#    form = ContactForm()
   
#    if request.method == 'POST':
#       if form.validate() == False:
#          flash('All fields are required.')
#          return render_template('contact.html', form = form)
#       else:
#          return render_template('success.html')
#       elif request.method == 'GET':
#          return render_template('contact.html', form = form)

def index():
	return render_template('index.html')


@app.route('/connect',methods = ['POST'])
def conn():
	if request.method=="POST":
		host = request.form.get("host")
		port = request.form.get("port")
		ID = request.form.get("ID")
		user = request.form.get("username")
		pswrd = request.form.get("pswrd")
		KA = request.form.get("KA")
		topic = request.form.get("topic")
		msg= request.form.get("msg")
		KA=int(KA)
		port=int(port)
		flash(host)

		mqttc = mqtt.Client(user)
		clients.append(mqttc)
		print("List of clients:")
		for i in clients:
			print ("CLient" + str(i))
		mqttc.on_connect = on_connect
		mqttc.username_pw_set(user, pswrd)	
		mqttc.connect(host,port,KA)
		# mqttc.loop_forever()
		mqttc.loop(10)
		# time.sleep(5)
		# mqttc.diconnect()
		# time.sleep(10)
		mqttc.loop_stop()
		print("haaa")
		# mqttc.loop_stop()
		return redirect(url_for('index'))



# def hi():
# 	if request.method== 'POST':
# 		return ("yeaaaah")
# This is the Publisher

# client = mqtt.Client("Marwa")					#Initialize a client
# client.connect("localhost",5000,60)				#establish a connection
# client.publish("topic/test", "Hello world!");	#publish the message
# client.disconnect();
		
if __name__ == '__main__':
	app.run(debug=True)





# Define event callbacks


def on_connect(client, userdata, flags, rc):
	print("conn")
	flash('You have successfully logged in')
	if rc==0:
		flash('You have successfully logged in')
		print("plzzz")
		return redirect(url_for('index'))
	else:
		flash('Problem connecting')
def on_message(client, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

# mqttc = mqtt.Client()
# # Bind call back fns
# mqttc.on_message = on_message
# mqttc.on_connect = on_connect
# mqttc.on_publish = on_publish
# mqttc.on_subscribe = on_subscribe

# # Uncomment to enable debug messages
# #mqttc.on_log = on_log

# # Parse CLOUDMQTT_URL (or fallback to localhost)
# url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://localhost:1883')
# url = urlparse.urlparse(url_str)
# topic = url.path[1:] or 'test'
# # url.username="Marwa"
# # url.password="123"
# # Connect
# mqttc.username_pw_set("Marwa", "123")
# mqttc.connect(url.hostname, url.port)

# # Start subscribe, with QoS level 0
# mqttc.subscribe(topic, 0)

# # Publish a message
# mqttc.publish(topic, "my message")

# # Continue the network loop, exit when an error occurs
# rc = 0
# if rc == 0:
#     rc = mqttc.loop()
# print("rc: " + str(rc))
# mqttc.publish(topic, "my message")
# mqttc.loop_stop()
# mqttc.publish(topic, "after stop")
# print("rc after: " + str(rc))
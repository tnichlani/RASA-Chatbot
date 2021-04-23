from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
#restaurants = None

def sendmail(MailID,restraunts):
    sender_address = 'shashanklalupgrad@gmail.com'
    sender_pass = 'upgrad123'
    receiver_address = MailID
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Restraunt Details'   #The subject line
    #The body and the attachments for the mail
    html = """\
    <html>
      <head>Please find below the restraunt details</head>
      <body>
        {0}
      </body>
    </html>
    """.format(restraunts.to_html())
    part1 = MIMEText(html, 'html')
    message.attach(part1)
    #message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

def budget_group(row):
    if row['Average Cost for two'] <300 :
        return 'lesser than 300'
    elif 300 <= row['Average Cost for two'] <700 :
        return 'between 300 to 700'
    else:
        return 'more than 700'
        
def RestaurantSearch(City,Cuisine,Budget):
    ZomatoData['Budget'] = ZomatoData.apply(lambda row: budget_group (row),axis=1)      
    #TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
    restaurants = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower())) & (ZomatoData['Budget'].apply(lambda x: Budget.lower() in x.lower()))]
    return restaurants[['Restaurant Name','Address','Average Cost for two','Aggregate rating']].sort_values(by=['Aggregate rating'], ascending=False)
    
class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		#print(F'hello {price}')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget = price)
		response=""
        #print(F'hello {price}')
		if results.shape[0] == 0:
			response= "no results"
		else:
			for restaurant in RestaurantSearch(loc,cuisine,price).iloc[:5].iterrows():
				restaurant = restaurant[1]
				response=response + F"Found {restaurant['Restaurant Name']} in {restaurant['Address']} rated {restaurant['Address']} with avg cost {restaurant['Average Cost for two']} \n\n"
				
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('email')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		restaurants = RestaurantSearch(City=loc,Cuisine=cuisine,Budget = price).head(10) #Top 10 restraunts      
		sendmail(MailID,restaurants)
		dispatcher.utter_message("Email Sent to : "+MailID)        
		return [SlotSet('email',MailID)]
        
class Check_location(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city_list = [each_city.lower() for each_city in WeOperate]
		res = loc.lower() in city_list
		if (res):
			return [SlotSet('location',loc), SlotSet('location_found','found')]         
		else:
			return [SlotSet('location','None'), SlotSet('location_found','notfound')]
## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price        
	
* restaurant_search{"price": "more than 700"}
	- slot{"price": "more than 700"}
	- action_search_restaurants
	- slot{"location": "delhi"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye


## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price    
* affirm
	- action_search_restaurants
	- utter_query_mail
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - utter_goodbye


## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_query_mail
* goodbye
    - utter_goodbye

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_check_location
	- slot{"location": null}
	- slot{"location_found": "notfound"}
	- utter_location_notfound
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
	- utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "lesser than 300"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
	- slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "delhi"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai", "price": "between 300 to 700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
	- action_check_location
	- slot{"location": "mumbai"}
	- slot{"location_found": "found"}
	- slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi", "price": "more than 700"}
    - slot{"location": "delhi"}
	- action_check_location
	- slot{"location": "delhi"}
	- slot{"location_found": "found"}
	- slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
	- action_check_location
	- slot{"location": "Delhi"}
	- slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye

## interactive_story_RepeatedLocation
* greet
    - utter_greet
* restaurant_search{"location": "faizabaaaad"}
    - slot{"location": "faizabaaaad"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
	- utter_goodbye
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_location
    - slot{"location": "agra"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "agra"}
	- utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye

* restaurant_search{"location": "basti"}
    - slot{"location": "basti"}
    - action_check_location
    - slot{"location": "None"}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* goodbye
    - utter_goodbye	

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"location": "Mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - action_check_location
    - slot{"location": "Lucknow"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - utter_query_mail
* goodbye
    - utter_goodbye
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - slot{"location": "Agra"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_query_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - slot{"email": "shashank.lal@gmail.com"}
    - utter_goodbye

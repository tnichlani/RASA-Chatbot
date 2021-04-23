
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

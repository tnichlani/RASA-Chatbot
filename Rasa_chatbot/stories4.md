
## interactive_story_1
* greet
    - utter_greet
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
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_query_mail
* affirm
    - utter_ask_mail
* affirm{"email": "shashank.lal@gmail.com"}
    - slot{"email": "shashank.lal@gmail.com"}
    - action_send_mail
    - utter_goodbye

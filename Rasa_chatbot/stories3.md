
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"location": "None"}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "faizabad"}
    - slot{"location": "faizabad"}
    - action_check_location
    - slot{"location": "None"}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
    - utter_goodbye

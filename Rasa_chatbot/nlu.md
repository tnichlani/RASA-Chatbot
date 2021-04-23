## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi
- hi
- hello

## intent:restaurant_search
- i'm looking for a place to eat
- restraunts in [Rishikesh](location)
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [bambai](location:mumbai)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- [dilli](location:delhi)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [noida](location)
- [allahabad](location)
- [bhubaneshwar](location)
- [mangalore](location)
- [Mysore](location)
- [Mysuru](location:Mysore)
- restaurants in [noida](location)
- restaurants in [Prayagraj](location:Allahabad)
- [Bambai](location:mumbai)
- please find me a restaurant in [allahabad](location)
- restaurants in [Mangalore](location)
- [Mangaluru](location:mangalore)
- please find me a restaurant in [Bhubaneshwar](location)
- [Puducherry](location)
- [Pondicherry](location:Puducherry)
- [Varanasi](location)
- [Banaras](location:Varanasi)
- [Benaras](location:Varanasi)
- [Vadodara](location)
- [Baroda](location:Vadodara)
- [Vizag](location)
- [Visakhapatnam](location:Vizag)
- [Vizagapatam](location:Vizag)
- [Kanpur](location)
- [Cawnpore](location:Kanpur)
- [Lucknow](location)
- [Lakhnau](location:Lucknow)
- [Kochi](location)
- [Cochin](location:Kochi)
- [Coimbatore](location)
- [Kovai](location:Coimbatore)
- [Covai](location:Coimbatore)
- [Chennai](location)
- [Madras](location:Chennai)
- [Guwahati](location)
- [Gauhati](location:Guwahati)
- [Pune](location)
- [Poona](location:Pune)
- [Kolkata](location)
- [calcutta](location:Kolkata)
- [Ooty](location)
- [Udhagamandalam](location:Ooty)
- [Gangtok](location)
- [gantok](location:Gangtok)
- [Shimla](location)
- [Simla](location:Shimla)
- show me restaurants in price range [lesser than 300](price)
- [lesser than 300](price)
- [< 300](price:lesser than 300)
- [< than 300](price:lesser than 300)
- [less than 300](price:lesser than 300)
- [between 300 to 700](price)
- [300 to 700](price:between 300 to 700)
- [between 300 and 700](price:between 300 to 700)
- [more than 700](price)
- [> 700](price:more than 700)
- [> than 700](price:more than 700)
- [greater than 700](price:more than 700)
- yes. please send it to [shashank.lal@gmail.com](email)
- please mail to [shashank.lal@gmail.com](email)
- [upgrad@gmail.com](email)
- cool. send all the restaurant details to [abc.xyz@yahoo.co.in](email)

## synonym:more than 700
- > 700
- > than 700
- greater than 700

## synonym:lesser than 300
- < 300
- < than 300
- less than 300

## synonym:between 300 to 700
- 300 to 700
- between 300 and 700

## synonym:4
- four

## synonym:New Delhi
- Delhi
- Dilli

## synonym:bangalore
- Bengaluru

## synonym:Shimla
- Simla

## synonym:Gangtok
- gantok

## synonym:Ooty
- Udhagamandalam


## synonym:Kolkata
- calcutta

## synonym:Pune
- Poona

## synonym:Guwahati
- Gauhati

## synonym:Chennai
- Madras

## synonym:Coimbatore
- Kovai
- Covai

## synonym:Kochi
- Cochin

## synonym:Lucknow
- Lakhnau

## synonym:Kanpur
- Cawnpore

## synonym:Vizag
- Visakhapatnam
- Vizagapatam


## synonym:Vadodara
- Baroda

## synonym:Varanasi
- Banaras
- Benaras


## synonym:Puducherry
- Pondicherry

## synonym:mangalore
- Mangaluru


## synonym:Bhubaneshwar
- Kalinga

## synonym:Mysore
- Mysuru

## synonym:Allahabad
- Prayagraj

## synonym:mumbai
- Bombay
- Bambai

## synonym:noida
- gautambudh nagar
- gautambudhnagar
- gautam budh nagar
- greater noida
- greaternoida

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:email
- [a-zA-Z0-9_.+]+@[a-zA-Z]+[.][a-zA-Z0-9-.]+$
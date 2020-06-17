## book room
* greet
  - utter_greet
* book_room
  - utter_how_many
* num_of_room
  - utter_what_kind
* kind_of_room{"num_room":"one", "kind":"simple"}
  - utter_confirm
* affirm
  - utter_anything_else
* deny
  - utter_goodbye

## clean room path 1
* greet
  - utter_greet
* clean_room
  - utter_when
* clean_when{"time":"now"}
  - utter_will_send
  - utter_did_that_help
* affirm
  - utter_anything_else
  
## FAQ1 checkin
* checkin
  - utter_checkin
  
## FAQ2 checkout
* checkout
  - utter_checkout
  
## FAQ3 cancel reservation
* cancel_booking
  -utter_cancel_booking

## FAQ4 cancel policy
* cancellation_policy
  -utter_cancel_policy
  
## FAQ5 restaurant
* restaurant
  -utter_restaurant_details
  
## FAQ6 breakfast
* breakfast
  -utter_breakfast_details
  
## FAQ7 breakfast timings
* breakfast_timings
  -utter_breakfast_timings
  
## FAQ8 restaurant timings
* restaurant_timings
  -utter_restaurant_timings

## book room path2
* book_room
  - utter_how_many
* num_of_room
  - utter_what_kind
* kind_of_room{"num_room":"one", "kind":"simple"}
  - utter_confirm
  
## boring path
* boring
  - utter_anything_else
* affirm
  - utter_repeat

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_anything_else
  
## say goodbye2
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  


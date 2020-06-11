## happy path

* greet
  - utter_greet
* mood_great
  - utter_newdress

## new dress path

* greet
  - utter_greet
* new_dress
  - utter_newdress
* affirm
  - utter_gender
* choose_gender
  - utter_know
  - size_form
  - form{"name": "size_form"}
  - form{"name": null}  
  - utter_slots_values
  - utter_ask_feedback
* affirm
  - utter_done
  - utter_askplans
* occasion
  - utter_askclothtype
* choose_clothtype
  - utter_askpatterns
* choose_patterns
  - utter_askfittings
* choose_fittings
  - utter_askcolour
* choose_colour
  - utter_done
  - utter_clothimages
  - utter_image2
  - utter_image3
  - utter_image4
  - utter_image5
  - utter_image6
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 1

* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

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
  - utter_goodbye

## bot challenge

* bot_challenge
  - utter_iamabot

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/
#
# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List, Union
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
#import requests
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
#
class Actiongetsizes(FormAction):
     def name(self) -> Text:
         return "size_form"

     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "chest": self.from_text(intent=None),
            "height": self.from_text(intent=None),
            "waist": self.from_text(intent=None),
        }
     @staticmethod


     def required_slots(tracker: Tracker)->List[Text]:
        # type:()->List[Text]
         print("required_slots(tracker: Tracker)")
    
         return ["chest","height","waist"]


         
    # def run(self,dispatcher: CollectingDispatcher,tracker:Tracker,
     #domain: Dict[Text,Any])->List(Dict[Text,Any]):
     #chest= tracker.get_slot("name")
     #height= tracker.get_slot("height")
      #    waist= tracker.get_slot("waist")
       # dispatcher.utter_message(template="utter_done")
        #return[]

        # return[SlotSet("name","name")]   

     def submit(self,dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

         dispatcher.utter_message(template="utter_done")
         return []

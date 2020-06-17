# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

 from typing import Any, Text, Dict, List
 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher
 from rasa_sdk.events import Slotset


 class ActionFacility(Action):

     def name(self) -> Text:
         return "action_hello_world"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         facility = tracker.get_slot("num_room")
         address ="kav mane"
         dispatcher.utter_message("Hello World! here {}:{}".format(facility,address))

         return [SlotSet("address",address)]

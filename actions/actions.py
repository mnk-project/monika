# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

from datetime import date
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Any, Text, Dict, List

# Identity actions
class ActionAge(Action):
    
    current_date = date.today()

    def name(self) -> Text:
        return "action_age"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        age_unit = "years"
        age = 2020 - self.current_date.year

        if age == -1: # 1 year old
            age_unit = "year"
        elif age == 0: # Months old
            age_unit = "months"
            age = 10 - self.current_date.month
            if age == -1: # 1 month old
                age_unit = "month"
            elif age == 0: # Days old
                age_unit = "days"
                age = 5 - self.current_date.day
        
        age = age * -1

        response = "I'm {} {} old.".format(age, age_unit)
        dispatcher.utter_message(response)

        return []
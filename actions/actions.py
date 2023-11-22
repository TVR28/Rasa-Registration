from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGreet(Action):
    def name(self) -> Text:
        return "utter_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_greet")
        return []

class ActionRegisterOptions(Action):
    def name(self) -> Text:
        return "utter_register_options"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_register_options")
        return []

class ActionChooseInter(Action):
    def name(self) -> Text:
        return "utter_choose_inter"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_choose_inter")
        return []

class ActionChooseBtech(Action):
    def name(self) -> Text:
        return "utter_choose_btech"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_choose_btech")
        return []

class ActionProvideName(Action):
    def name(self) -> Text:
        return "utter_provide_name"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_provide_name")
        return []

class ActionProvideAge(Action):
    def name(self) -> Text:
        return "utter_provide_age"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_provide_age")
        return []

class ActionProvideGender(Action):
    def name(self) -> Text:
        return "utter_provide_gender"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_provide_gender")
        return []

class ActionProvideEmail(Action):
    def name(self) -> Text:
        return "utter_provide_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_provide_email")
        return []

class ActionThankYou(Action):
    def name(self) -> Text:
        return "utter_thank_you"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_thank_you")
        return []



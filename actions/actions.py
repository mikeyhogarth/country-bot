from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import json

with open('actions/countries.json') as json_file:
    country_data = json.load(json_file)


def get_country_record(tracker, key):
    location = list(
        filter(lambda e: e['entity'] == 'location', tracker.latest_message['entities']))[0]['value']
    record = list(
        filter(lambda c: c[key].lower() == location.lower(), country_data))[0]

    return record


class ActionGetCountryDetails(Action):
    def name(self) -> Text:
        return "action_get_country_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        intent = tracker.latest_message['intent']["name"]

        try:
            if "from_country" in intent:
                record = get_country_record(tracker, 'name')
            else:
                record = get_country_record(tracker, 'capital')

        except:
            dispatcher.utter_message(
                text="I think you tried to ask about a country but I couldn't understand which country you meant. Did you spell it correctly?")
            return

        if(intent == "learn_capital_from_country"):
            message = 'The capital of {0} is {1}'.format(
                record['name'], record['capital'])
        elif(intent == "learn_country_from_capital"):
            message = '{0} is the capital of {1}'.format(
                record['capital'], record['name'])
        elif(intent == "learn_population_from_country"):
            message = 'The population of {0} is {1}'.format(
                record['name'], record['population'])
        else:
            message = "Sorry, I didn't understand what you were asking"

        dispatcher.utter_message(text=message)
        return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

affairs ={
  "周一": "",
  "周二": "",
  "周三": "",
  "周四": "",
  "周五": "",
  "周六": "",
  "周日": "",
}
class ActionSetAffair(Action):

    def name(self) -> Text:
        return "action_set_affair"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_weekday = tracker.get_slot("weekday")
        dispatcher.utter_message(text=f"您已设置了{user_weekday}的时间计划：")
        user_affair = tracker.get_slot("affair")
        dispatcher.utter_message(text=f"{user_affair}")
        affairs[""+user_weekday] = user_affair

        return []

class ActionQueryAffair(Action):

    def name(self) -> Text:
        return "action_query_affair"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if len(affairs)==0:
            dispatcher.utter_message(text=f"计划表为空。")
        else:
            for x, y in affairs.items():
                dispatcher.utter_message(text=f"{x}:{y}")

        return []
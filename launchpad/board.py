import logging

from launchpad.invokers.groups import *


class LaunchPad:
    groups: dict[int, LaunchPadItemGroup] = dict()

    def register_groups(self, config: dict):
        # Register the groups
        self.groups.update({
            PadGroup.group_code: PadGroup(config.get("pads")),
            PotentiometerGroup.group_code: PotentiometerGroup(config.get("potentiometers")),
            PlayRecGroup.group_code: PlayRecGroup(config.get("play_rec")),
            KeysGroup.group_code: KeysGroup(config.get("keys"))
        })

    def process_event(self, event: dict) -> None:
        group_code = event.get("group_code")
        if group_code in self.groups:
            self.groups[group_code].consume_event(**event)
        else:
            logging.debug(f"Group code {group_code} not found")

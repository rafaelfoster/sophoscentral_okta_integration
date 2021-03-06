# flake8: noqa
"""
Copyright 2020 - Present Okta, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# AUTO-GENERATED! DO NOT EDIT FILE DIRECTLY
# SEE CONTRIBUTOR DOCUMENTATION

from okta.okta_object import OktaObject
from okta.models import event_hook_channel_config_auth_scheme_type\
    as event_hook_channel_config_auth_scheme_type


class EventHookChannelConfigAuthScheme(
    OktaObject
):
    """
    A class for EventHookChannelConfigAuthScheme objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.key = config["key"]\
                if "key" in config else None
            if "type" in config:
                if isinstance(config["type"],
                              event_hook_channel_config_auth_scheme_type.EventHookChannelConfigAuthSchemeType):
                    self.type = config["type"]
                elif config["type"] is not None:
                    self.type = event_hook_channel_config_auth_scheme_type.EventHookChannelConfigAuthSchemeType(
                        config["type"].upper()
                    )
                else:
                    self.type = None
            else:
                self.type = None
            self.value = config["value"]\
                if "value" in config else None
        else:
            self.key = None
            self.type = None
            self.value = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "key": self.key,
            "type": self.type,
            "value": self.value
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format

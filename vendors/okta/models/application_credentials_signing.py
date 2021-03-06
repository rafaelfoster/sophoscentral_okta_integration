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
from okta.models import application_credentials_signing_use\
    as application_credentials_signing_use


class ApplicationCredentialsSigning(
    OktaObject
):
    """
    A class for ApplicationCredentialsSigning objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.kid = config["kid"]\
                if "kid" in config else None
            self.last_rotated = config["lastRotated"]\
                if "lastRotated" in config else None
            self.next_rotation = config["nextRotation"]\
                if "nextRotation" in config else None
            self.rotation_mode = config["rotationMode"]\
                if "rotationMode" in config else None
            if "use" in config:
                if isinstance(config["use"],
                              application_credentials_signing_use.ApplicationCredentialsSigningUse):
                    self.use = config["use"]
                elif config["use"] is not None:
                    self.use = application_credentials_signing_use.ApplicationCredentialsSigningUse(
                        config["use"].upper()
                    )
                else:
                    self.use = None
            else:
                self.use = None
        else:
            self.kid = None
            self.last_rotated = None
            self.next_rotation = None
            self.rotation_mode = None
            self.use = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "kid": self.kid,
            "lastRotated": self.last_rotated,
            "nextRotation": self.next_rotation,
            "rotationMode": self.rotation_mode,
            "use": self.use
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format

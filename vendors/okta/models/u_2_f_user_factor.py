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

from okta.models.user_factor\
    import UserFactor
from okta.models import u_2_f_user_factor_profile\
    as u_2_f_user_factor_profile


class U2FUserFactor(
    UserFactor
):
    """
    A class for U2FUserFactor objects.
    """

    def __init__(self, config=None):
        super().__init__(config)
        if config:
            self.factor_type = "u2f"
            if "profile" in config:
                if isinstance(config["profile"],
                              u_2_f_user_factor_profile.U2FUserFactorProfile):
                    self.profile = config["profile"]
                elif config["profile"] is not None:
                    self.profile = u_2_f_user_factor_profile.U2FUserFactorProfile(
                        config["profile"]
                    )
                else:
                    self.profile = None
            else:
                self.profile = None
        else:
            self.profile = None

    def request_format(self):
        parent_req_format = super().request_format()
        current_obj_format = {
            "profile": self.profile
        }
        parent_req_format.update(current_obj_format)
        return parent_req_format

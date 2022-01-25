# -*- coding: utf-8 -*-
# Copyright: (c) 2022, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):
    DOCUMENTATION = r"""
options:
  mapping:
    version_added: "1.3.0"
    description:
      - Optional parameters where user can override Choice Lists values for objects.
      - Currently, only values inside incident object mapping can be overridden.
    type: dict
    suboptions:
      incident:
        description:
          - User mappings for Incident object.
          - Where mapping is not set, the default will be used.
        type: dict
        suboptions:
          hold_reason:
            description:
              - Reason why incident is on hold.
              - Required if I(state) value is C(on_hold).
            type: dict
          impact:
            description:
              - The measure of the business criticality of the affected service.
            type: dict
          state:
            description:
              - State of the incident.
              - If I(state) value is C(on_hold), I(on_hold_reason) parameter must be filled in.
              - Special value that can not be overridden is C(absent), which would remove an incident from ServiceNow.
            type: dict
          urgency:
            description:
              - The extent to which resolution of an incident can bear delay.
            type: dict
      configuration_item:
        description:
          - User mappings for Configuration item object
          - Where mapping is not set, the default will be used.
        type: dict
        suboptions:
          environment:
            description:
              - The environment to which this configuration item belongs.
            type: dict
          install_status:
            description:
              - The functional status of the configuration item.
              - Special value that can not be overridden is C(absent), which would remove a configuration item from ServiceNow.
            type: dict
          operational_status:
            description:
              - The operational status of the configuration item.
            type: dict
"""

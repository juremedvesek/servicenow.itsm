# -*- coding: utf-8 -*-
# Copyright: (c) 2021, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from . import choices


empty = ("", "")


def get_new_payload_mapping(table_client):
    choices_client = choices.ChoicesClient(table_client)
    incident_choices = choices_client.get_grouped_choices("incident")

    correct = dict(
        impact=incident_choices["severity"],
        urgency=incident_choices["severity"],
        state=incident_choices["state"],
        hold_reason=incident_choices["hold_reason"] + [empty],
        close_code=incident_choices["close_code"] + [empty]
    )
    return correct

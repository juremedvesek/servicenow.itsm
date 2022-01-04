# -*- coding: utf-8 -*-
# Copyright: (c) 2021, XLAB Steampunk <steampunk@xlab.si>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

INCIDENT_QUERY = "incident"


empty = ("", "")


def incident_mapping(choices):
    correct = dict(
        impact=choices["severity"],
        urgency=choices["severity"],
        state=choices["state"],
        hold_reason=choices["hold_reason"] + [empty],
        close_code=choices["close_code"] + [empty]
    )
    return correct

# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]
# (c) modified by AmirulAndalib [amirulandalib@github]

import logging
import traceback

from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
)

from ..core.getVars import get_val

torlog = logging.getLogger(__name__)

# todo add alpha admin if needed


async def is_admin(client, user_id, chat_id, force_owner=False):
    if force_owner:
        if user_id == get_val("OWNER_ID"):
            return True
        else:
            return False
    else:
        return True

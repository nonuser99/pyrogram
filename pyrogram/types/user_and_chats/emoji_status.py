#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from datetime import datetime
from typing import Optional

import pyrogram
from pyrogram import raw, utils

from ..object import Object


class EmojiStatus(Object):
    """A user emoji status.

    Parameters:
        custom_emoji_id (``int``):
            Custom emoji id.

        until_date (:py:obj:`~datetime.datetime`, *optional*):
            Valid until date.

        title (``str``, *optional*):
            Title of the collectible.

        collectible_id (``int``, *optional*):
            Collectible id.

        name (``str``, *optional*):
            Name of the collectible.

        pattern_custom_emoji_id (``int``, *optional*):
            Pattern emoji id.

        center_color (``int``, *optional*):
            Center color of the collectible emoji in decimal format.

        edge_color (``int``, *optional*):
            Edge color of the collectible emoji in decimal format.

        pattern_color (``int``, *optional*):
            Pattern color of the collectible emoji in decimal format.

        text_color (``int``, *optional*):
            Text color of the collectible emoji in decimal format.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        custom_emoji_id: int,
        until_date: Optional[datetime] = None,
        title: Optional[str] = None,
        collectible_id: Optional[int] = None,
        name: Optional[str] = None,
        pattern_custom_emoji_id: Optional[int] = None,
        center_color: Optional[int] = None,
        edge_color: Optional[int] = None,
        pattern_color: Optional[int] = None,
        text_color: Optional[int] = None
    ):
        super().__init__(client)

        self.custom_emoji_id = custom_emoji_id
        self.until_date = until_date
        self.title = title
        self.collectible_id = collectible_id
        self.name = name
        self.pattern_custom_emoji_id = pattern_custom_emoji_id
        self.center_color = center_color
        self.edge_color = edge_color
        self.pattern_color = pattern_color
        self.text_color = text_color

    @staticmethod
    def _parse(client, emoji_status: "raw.base.EmojiStatus") -> Optional["EmojiStatus"]:
        if isinstance(emoji_status, raw.types.EmojiStatus):
            return EmojiStatus(
                client=client,
                custom_emoji_id=emoji_status.document_id,
                until_date=utils.timestamp_to_datetime(getattr(emoji_status, "until", None))
            )

        if isinstance(emoji_status, raw.types.EmojiStatusCollectible):
            return EmojiStatus(
                client=client,
                custom_emoji_id=emoji_status.document_id,
                until_date=utils.timestamp_to_datetime(getattr(emoji_status, "until", None)),
                title=emoji_status.title,
                collectible_id=emoji_status.collectible_id,
                name=emoji_status.slug,
                pattern_custom_emoji_id=emoji_status.pattern_document_id,
                center_color=emoji_status.center_color,
                edge_color=emoji_status.edge_color,
                pattern_color=emoji_status.pattern_color,
                text_color=emoji_status.text_color
            )

        return None

    def write(self):
        if self.collectible_id:
            return raw.types.EmojiStatusCollectible(
                collectible_id=self.collectible_id,
                document_id=self.custom_emoji_id,
                title=self.title,
                slug=self.name,
                pattern_document_id=self.pattern_custom_emoji_id,
                center_color=self.center_color,
                edge_color=self.edge_color,
                pattern_color=self.pattern_color,
                text_color=self.text_color,
                until=utils.datetime_to_timestamp(self.until_date)
            )

        return raw.types.EmojiStatus(
            document_id=self.custom_emoji_id,
            until=utils.datetime_to_timestamp(self.until_date)
        )

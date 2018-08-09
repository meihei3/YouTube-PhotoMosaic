#!/usr/bin/python
#
# Copyright 2018 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from apiclient.discovery import build
from apiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "%s"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def YouTube(API_KEY=""):
    if DEVELOPER_KEY != "%s":
        API_KEY = DEVELOPER_KEY
    else:
        assert API_KEY != ""
    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                 developerKey=API_KEY)


class Channel(object):
    def __init__(self, youtube, channel_id):
        self._youtube = youtube
        self._channel_id = channel_id
        self.__update()
        if self.__channel_response["pageInfo"]["totalResults"] != 1:
            raise ValueError("This channel id is not found.")

    def get_channel_thumbnail_url(self, size="default"):
        assert size in ("default", "medium", "high")
        return self.__channel_response["items"][0]["snippet"]["thumbnails"][size]["url"]

    def get_video_thumbnail_urls(self, n=10):
        cnt, token = 0, None

        url_list = []
        while cnt <= n:
            if n - cnt < 50:
                search_response = self.__search(part="snippet", max_result=n-cnt, token=token)
            else:
                search_response = self.__search(part="snippet", max_result=50, token=token)
            url_list += [item["snippet"]["thumbnails"]["medium"]["url"] for item in search_response["items"]]
            if "nextPageToken" not in search_response:
                break
            token = search_response["nextPageToken"]
            cnt += 50
        return url_list

    def __update(self):
        self.__channel_response = self._youtube.channels().list(
            part="id, snippet, brandingSettings, contentDetails, invideoPromotion, statistics, topicDetails",
            id=self._channel_id
        ).execute()

    def __search(self, part="id", max_result=25, token=None, order="date"):
        return self._youtube.search().list(
            channelId=self._channel_id,
            part=part,
            maxResults=max_result,
            pageToken=token,
            order=order,
            type="video"
        ).execute()


if __name__ == "__main__":
    yt = YouTube()
    ch = Channel(yt, "UCLhUvJ_wO9hOvv_yYENu4fQ")
    print(ch.get_channel_thumbnail_url())

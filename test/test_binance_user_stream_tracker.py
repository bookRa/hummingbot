#!/usr/bin/env python

from os.path import join, realpath
import sys

sys.path.insert(0, realpath(join(__file__, "../../")))


from wings.tracker.binance_user_stream_tracker import BinanceUserStreamTracker
from wings.user_stream_tracker import UserStreamTrackerDataSourceType


from wings.tracker.binance_order_book_tracker import BinanceOrderBookTracker
import asyncio
import logging
from typing import Dict, Optional
import unittest
logging.basicConfig(level=logging.DEBUG)


class BinanceOrderBookTrackerUnitTest(unittest.TestCase):
    order_book_tracker: Optional[BinanceOrderBookTracker] = None
    @classmethod
    def setUpClass(cls):
        cls.ev_loop: asyncio.BaseEventLoop = asyncio.get_event_loop()
        cls.user_stream_tracker: BinanceUserStreamTracker = BinanceUserStreamTracker(
            UserStreamTrackerDataSourceType.EXCHANGE_API)
        cls.user_stream_tracker_task: asyncio.Task = asyncio.ensure_future(cls.user_stream_tracker.start())

    def test_user_stream(self):
        # Wait process some msgs.
        self.ev_loop.run_until_complete(asyncio.sleep(120.0))
        print(self.user_stream_tracker.user_stream)

def main():

    unittest.main()


if __name__ == "__main__":
    main()
from gevent.event import Event
from gevent.queue import Queue

from raiden.utils import typing, pex


class NotifyingQueue(Event):
    def __init__(self, maxsize=None, items=()):
        super().__init__()
        self._queue = Queue(maxsize, items)

        if items:
            self.set()

    def put(self, item):
        """ Add new item to the queue. """
        self._queue.put(item)
        self.set()

    def get(self, block=True, timeout=None):
        """ Removes and returns an item from the queue. """
        value = self._queue.get(block, timeout)
        if self._queue.empty():
            self.clear()
        return value

    def peek(self, block=True, timeout=None):
        return self._queue.peek(block, timeout)

    def __len__(self):
        return len(self._queue)

    def copy(self):
        """ Copies the current queue items. """
        copy = self._queue.copy()

        result = list()
        while not copy.empty():
            result.append(copy.get_nowait())
        return result


class QueueIdentifier(typing.NamedTuple):
    recipient: typing.Address
    channel_identifier: typing.ChannelID

    def __repr__(self):
        return (
            f'<'
            f'QueueIdentifier recipient:{pex(self.recipient)} channelid:{self.channel_identifier}'
            f'>'
        )

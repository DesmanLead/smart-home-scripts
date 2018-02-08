#!/usr/bin/python
# -*- coding: utf-8 -*-


class MovingAverage(object):
    def __init__(self, initial, size=2):
        self._buffer = [initial]
        self._size = size

    def put(self, value):
        self._buffer.append(value)
        if len(self._buffer) > self._size:
            self._buffer = self._buffer[1:]

    def filtered_value(self):
        return sum(self._buffer) / len(self._buffer)

    def __repr__(self):
        return '< size: %d, value: %d >' % (self._size, self.filtered_value())

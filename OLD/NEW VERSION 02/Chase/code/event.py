"""
Copyright (C) 2014  Jason Gosen

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


class TimedEventSystem(object):
    def __init__(self):
        self. events = []

    def add(self, delay, func):
        """ delay - milliseconds to wait until calling func
        func - callback function for when the delay finishes """
        self.events.append(TimedEvent(self, delay, func))

    def remove(self, event):
        self.events.remove(event)

    def update(self, delta):
        for event in self.events:
            event.update(delta)


class TimedEvent(object):
    def __init__(self, parent, delay, func):
        self.parent = parent
        self.delay = delay
        self.func = func
        self.elapsed = 0

    def update(self, delta):
        self.elapsed += delta
        if self.elapsed >= self.delay:
            self.func()
            self.kill()

    def kill(self):
        self.parent.remove(self)

from utility import receiver
from utility.eventmaster import EventMaster, Event


class Control:
    def __init__(self):
        self._ip = None
        self._port = None
        self._receiver = None
        self._eventDict = {
            "turnForward": Event("turnForward"),
            "move": Event("move"),
            "rotate": Event("rotate"),
            "turnAll": Event("turnAll"),
            "setAuto": Event("setAuto"),
            "setCamera": Event("setCamera")
        }
        self._oldPackage = [None, None, None, None, None]
        self._eventMaster = EventMaster()
        self._eventMaster.append(self._eventDict.get("turnForward"))
        self._eventMaster.append(self._eventDict.get("move"))
        self._eventMaster.append(self._eventDict.get("rotate"))
        self._eventMaster.append(self._eventDict.get("turnAll"))
        self._eventMaster.append(self._eventDict.get("setCamera"))
        self._eventMaster.start()

    def connect(self, ip, port):
        self._receiver = receiver.Receiver(ip, port)
        self._receiver.packageFormat = "fiiff"

        def onReceive(data):
            if data[0] != self._oldPackage[0]:
                self._eventDict["turnForward"].push(data[0])

            if data[1] != self._oldPackage[1]:
                self._eventDict["move"].push(data[1])

            if data[2] != self._oldPackage[2]:
                self._eventDict["rotate"].push(data[2])

            if data[3] != self._oldPackage[3]:
                self._eventDict["turnAll"].push(data[3])

            if data[4] != self._oldPackage[4]:
                self._eventDict["setCamera"].push(data[4])

            self._oldPackage = data[:]

        self._receiver.connectToEvent(onReceive, "onReceive")
        self._receiver.connect()

    def disconnect(self):
        self._receiver.disconnect()

    def connectToEvent(self, foo, toEvent):
        event = self._eventDict[toEvent]
        event.connect(foo)

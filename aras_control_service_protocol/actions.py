from enum import Enum


class TakeOffAction(Enum):
    START_TAKE_OFF = "START_TAKE_OFF"


class GoUpAction(Enum):
    START_GO_UP = "START_GO_UP"


class ArasAction(Enum):
    START_CONTROL_SERVICE = "START_CONTROL_SERVICE"
    STOP_CONTROL_SERVICE = "STOP_CONTROL_SERVICE"

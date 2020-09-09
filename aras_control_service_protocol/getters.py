import grpc

from aras_control_service_protocol.messages import (
    Empty, Bool
)
from aras_control_service_protocol._stubs import (
    ControlServiceStub
)


# ------------------------ ARAS getters -----------------------------#

def getControlServiceStatus(control_service_ip):
    try:
        channel = grpc.insecure_channel(control_service_ip)
        stub = ControlServiceStub(channel)
        return stub.GetControlServiceStatus(Empty())
    except Exception as e:
        info = str(e)
        return Bool(value=False, info=info)

from aras_control_service_protocol.emitters import TakeOffEventEmitter
from aras_control_service_protocol.events import TakeOffEvent
from aras_control_service_protocol.messages import Device

CONTROL_SERVICE_IP = "localhost:50052"
ACCESS_DATA = {"ip": "192.168.50.158"}


drone = Device(
    type=Device.DeviceType.DRON,
    id=DRONE_ID,
    access_data=str(ACCESS_DATA))

take_off_emiter = TakeOffEventEmitter(CONTROL_SERVICE_IP)
take_off_emiter.emit(
    TakeOffEvent.TAKE_OFF_CONNECTED_BUT_FAILED, drone)
take_off_emiter.emit(TakeOffEvent.TAKE_OFF_CONNECTION_FAILED, drone)
take_off_emiter.emit(TakeOffEvent.TAKE_OFF_DONE, drone)

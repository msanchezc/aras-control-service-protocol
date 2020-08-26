from aras_control_service_protocol.events import ArasEvent
from aras_control_service_protocol.emitters import ArasEventEmitter
from aras_control_service_protocol.messages import StartInfo, Device


CONTROL_SERVICE_IP = "localhost:50052"
DRONE_ACCESS_DATA = {"ip": "192.168.50.158"}
DBEST_ACCESS_DATA = {"ip": "TODO"}
OWNER_ID = "lab"
BASE_ID = "base_lab"
DRONE_ID = "apolo"
DBEST_ID = "TODO"
ARAS_UPDATE_INFO_API_URL = "localhost:8000/monitor/api/update_info_drone"

drone = Device(
    type=Device.DeviceType.DRONE,
    id=DRONE_ID,
    access_data=str(DBEST_ACCESS_DATA))

battery_charging_system = Device(
    type=Device.DeviceType.BATTERY_CHARGING_SYSTEM,
    id=DRONE_ID,
    access_data=str(DBEST_ACCESS_DATA))

start_info = StartInfo(
    aras_update_info_api_url=ARAS_UPDATE_INFO_API_URL,
    owner_id=OWNER_ID,
    base_id=BASE_ID,
    drones=[drone],
    battery_charging_system=battery_charging_system,
    weather_station=battery_charging_system)

aras_event_emitter = ArasEventEmitter(CONTROL_SERVICE_IP)
aras_event_emitter.emit(ArasEvent.START_CONTROL_SERVICE_REQUESTED, start_info)

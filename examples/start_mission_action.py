from aras_control_service_protocol.emitters import MissionActionEmitter
from aras_control_service_protocol.actions import MissionAction
from aras_control_service_protocol.messages import Device, MissionData, Waypoint

CONTROL_SERVICE_IP = "localhost:50052"
ACCESS_DATA = {"ip": "192.168.50.158"}
DRONE_ID = "apolo"

drone = Device(
    type=Device.DeviceType.DRONE,
    id=DRONE_ID,
    access_data=str(ACCESS_DATA))

wp1 = Waypoint(latitude=3.3311495, longitude=-76.5392257, altitude=30)
wp2 = Waypoint(latitude=3.3313156, longitude=-76.5390251, altitude=30)
wp3 = Waypoint(latitude=3.3324065, longitude=-76.5402373, altitude=30)

waypoints = [wp1, wp2, wp3]

mission_data = MissionData(drone=drone, waypoints=waypoints)

mission_action_emmiter = MissionActionEmitter(CONTROL_SERVICE_IP)
mission_action_emmiter.emit(MissionAction.START_MISSION, mission_data)

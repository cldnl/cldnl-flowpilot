# hard-forked from https://github.com/commaai/openpilot/tree/05b37552f3a38f914af41f44ccc7c633ad152a15/selfdrive/car/gm/values.py
from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CarControllerParams():
  STEER_MAX = 600  # Safety limit, not LKA max. Trucks use 600.
  STEER_STEP = 2  # control frames per command
  STEER_DELTA_UP = 7
  STEER_DELTA_DOWN = 17
  MIN_STEER_SPEED = 3.  # m/s
  STEER_DRIVER_ALLOWANCE = 50
  STEER_DRIVER_MULTIPLIER = 4
  STEER_DRIVER_FACTOR = 100
  NEAR_STOP_BRAKE_PHASE = 0.5  # m/s

  # Heartbeat for dash "Service Adaptive Cruise" and "Service Front Camera"
  ADAS_KEEPALIVE_STEP = 100
  CAMERA_KEEPALIVE_STEP = 100

  # Volt gasbrake lookups
  MAX_GAS = 3072 # Safety limit, not ACC max. Stock ACC >4096 from standstill.
  ZERO_GAS = 2048 # Coasting
  MAX_BRAKE = 350 # ~ -3.5 m/s^2 with regen

  # Allow small margin below -3.5 m/s^2 from ISO 15622:2018 since we
  # perform the closed loop control, and might need some
  # to apply some more braking if we're on a downhill slope.
  # Our controller should still keep the 2 second average above
  # -3.5 m/s^2 as per planner limits
  ACCEL_MAX = 2. # m/s^2
  ACCEL_MIN = -4. # m/s^2

  MAX_ACC_REGEN = 1404  # Max ACC regen is slightly less than max paddle regen
  GAS_LOOKUP_BP = [-1., 0., ACCEL_MAX]
  GAS_LOOKUP_V = [MAX_ACC_REGEN, ZERO_GAS, MAX_GAS]
  BRAKE_LOOKUP_BP = [ACCEL_MIN, -1.]
  BRAKE_LOOKUP_V = [MAX_BRAKE, 0.]

STEER_THRESHOLD = 1.0

class CAR:
  SILVERADO_NR = "CHEVROLET SILVERADO NO RADAR"

class CruiseButtons:
  INIT = 0
  UNPRESS = 1
  RES_ACCEL = 2
  DECEL_SET = 3
  MAIN = 5
  CANCEL = 6

class AccState:
  OFF = 0
  ACTIVE = 1
  FAULTED = 3
  STANDSTILL = 4

class CanBus:
  POWERTRAIN = 0
  OBSTACLE = 1
  CHASSIS = 2
  SW_GMLAN = 3
  LOOPBACK = 128

FINGERPRINTS = {
  CAR.SILVERADO_NR: [
  {
    190: 6, 193: 8, 197: 8, 201: 8, 208: 8, 209: 7, 211: 2, 241: 6, 249: 8, 257: 8, 288: 5, 289: 8, 298: 8, 304: 3, 309: 8, 311: 8, 313: 8, 320: 4, 322: 7, 328: 1, 352: 5, 381: 8, 384: 4, 386: 8, 388: 8, 413: 8, 451: 8, 452: 8, 453: 6, 455: 7, 460: 5, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 497: 8, 500: 6, 501: 8, 528: 5, 532: 6, 560: 8, 562: 8, 563: 5, 565: 5, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 707: 8, 715: 8, 717: 5, 761: 7, 789: 5, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 869: 4, 880: 6, 977: 8, 1001: 8, 1011: 6, 1017: 8, 1020: 8, 1033: 7, 1034: 7, 1217: 8, 1221: 5, 1233: 8, 1249: 8, 1259: 8, 1261: 7, 1263: 4, 1265: 8, 1267: 1, 1271: 8, 1280: 4, 1296: 4, 1300: 8, 1930: 7
  }],
}

NO_ASCM = set([CAR.SILVERADO_NR])
HIGH_TORQUE = set([CAR.SILVERADO_NR])

DBC = {
  # No Radar varieties (Non ASCM)
  CAR.SILVERADO_NR: dbc_dict('gm_global_a_powertrain_generated', 'gm_global_a_object', chassis_dbc='gm_global_a_chassis'),
}

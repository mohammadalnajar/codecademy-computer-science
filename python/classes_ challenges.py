# 1. Setting Up Our Robot
print("Setting Up Our Robot ========================================================")


class DriveBot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        DriveBot.robot_count += 1
        self.id = DriveBot.robot_count

        return None

    def __repr__(self):
        pass

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robots = []
robot_1 = DriveBot()
robots.append(robot_1)
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

robot_2 = DriveBot(35, 75, 25)
robots.append(robot_2)
robot_3 = DriveBot(20, 60, 10)
robots.append(robot_3)

# for robot in robots:
#     robot.latitude = -50.0
#     robot.longitude = 50.0
#     robot.all_disabled = True
DriveBot.all_disabled = True
DriveBot.latitude = -50.0
DriveBot.longitude = 50.0


print(robot_1.latitude)
print(robot_2.longitude)
print(robot_3.all_disabled)

print(robot_1.id)
print(robot_2.id)
print(robot_3.id)

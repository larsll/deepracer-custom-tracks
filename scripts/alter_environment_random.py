## This script is a domain randomizer for the 2024_reinvent_champ_custom track
import rospy
from deepracer_msgs.srv import SetVisualVisible
import random

def set_visual_visible(link_name, visual_name, visible):
    rospy.wait_for_service('/gazebo/set_visual_visible')
    try:
        set_visual_visible_service = rospy.ServiceProxy('/gazebo/set_visual_visible', SetVisualVisible, persistent=True)
        response = set_visual_visible_service(link_name=link_name, visual_name=visual_name, visible=visible)
        return response.success
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return False

def main():
    rospy.init_node('alter_environment_random', anonymous=True)

    visuals_wall = [
        "racetrack::background::visual",
        "racetrack::background_color::visual",
        "racetrack::background_small::visual"
    ]

    visuals_bool = [
        "racetrack::cl::visual",
        "racetrack::vegas_building_01::visual",
        "racetrack::vegas_building_02::visual",
        "racetrack::vegas_building_03::visual",
        "racetrack::landmark01::visual",
        "racetrack::landmark02::visual",
        "racetrack::landmark03::visual",
        "racetrack::landmark04::visual",
        "racetrack::landmark05::visual",
        "racetrack::landmark06::visual",
        "racetrack::landmark07::visual",
        "racetrack::signs::visual"
    ]

    selected_index = random.randint(0, len(visuals_wall))
    for i, visual in enumerate(visuals_wall):
        link_name = visual.split("::")[1]
        visible = 1 if i == selected_index else 0
        success = set_visual_visible(link_name, visual, visible)
        visibility_status = "On" if visible else "Off"
        success_status = "Success" if success else "Failed"
        rospy.loginfo(f"{link_name:<20} {visibility_status:<5} {success_status}")

    for visual in visuals_bool:
        link_name = visual.split("::")[1]
        visible = random.randint(0, 1)
        success = set_visual_visible(link_name, visual, visible)
        visibility_status = "On" if visible else "Off"
        success_status = "Success" if success else "Failed"
        rospy.loginfo(f"{link_name:<20} {visibility_status:<5} {success_status}")


if __name__ == "__main__":
    main()
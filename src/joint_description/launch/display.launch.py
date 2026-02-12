from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('joint_description')

    view_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'view_model.launch.py')
        )
    )

    joint_gui = TimerAction(
        period=1.0,  # vent 1 sekund for robot_state_publisher
        actions=[
            Node(
                package='joint_state_publisher_gui',
                executable='joint_state_publisher_gui',
                name='joint_state_publisher_gui'
            )
        ]
    )

    return LaunchDescription([
        view_launch,
        joint_gui
    ])

from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('joint_description')
    urdf_path = os.path.join(pkg_share, 'urdf', 'joint_model.urdf')

    with open(urdf_path, 'r') as infp:
        robot_description_content = infp.read()

    #robot_description_content = '<robot xmlns:xacro="http://www.ros.org/wiki/xacro"  name="robot"><link name="world"/></robot>'

    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description_content}]
    )

    node_rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen'
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
        node_robot_state_publisher,
        node_rviz,
        joint_gui
    ])
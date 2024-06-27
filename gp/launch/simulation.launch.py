import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
from launch_ros.actions import Node
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription

def generate_launch_description():
    gazebo_pkg = "gazebo_ros"
    spawn_node = "spawn_entity.py"
    spawn_entity = Node(
        package=gazebo_pkg,
        executable=spawn_node,
        name="spawn_entity_node",
        arguments=["-topic", "robot_description", "-entity", "my_bot"],
        output="screen"
    )

    pkg_name = "gp"
    rsp_file = "rsp.launch.py"
    rsp_path = os.path.join(get_package_share_directory(pkg_name), "launch", rsp_file)
    rsp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([rsp_path])
    )

    gazebo_file = "gazebo.launch.py"
    gazebo_path = os.path.join(get_package_share_directory(gazebo_pkg), "launch", gazebo_file)
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_path])
    )

    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity
    ])

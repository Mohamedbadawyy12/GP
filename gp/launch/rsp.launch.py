import os
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command
from launch_ros.actions import Node
from launch import LaunchDescription
import xacro

# this is the function launch system will look for
def generate_launch_description():

    ####### DATA INPUT ########
    urdf_file_name = 'robot.urdf.xacro'
    package_name = 'gp'
    ####### DATA INPUT END ########

    print("Fetching URDF ==>")
    # path to our package/urdf/urdf_file
    robot_desc_path = os.path.join(get_package_share_directory(package_name), "urdf", urdf_file_name)
    xacro_file =xacro.process_file(robot_desc_path)
    # Robot State Publisher
    urdf_content = open(robot_desc_path).read()
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher_node',
        parameters=[{'use_sim_time': True, 'robot_description': xacro_file.toxml()}],
        output='screen'
    )
    
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher_node',
        output='screen'
    )

    # create and return launch description object
    return LaunchDescription(
        [
            robot_state_publisher_node,
            joint_state_publisher_node
        ]
    )

cmake_minimum_required(VERSION 2.8.3)
project(commander)

find_package(catkin REQUIRED
    COMPONENTS
        rospy
        std_msgs
        message_generation
)

add_service_files(
        DIRECTORY srv
        FILES commander.srv
)


catkin_python_setup()
generate_messages(DEPENDENCIES std_msgs)

catkin_package(
        CATKIN_DEPENDS
            message_runtime
            std_msgs
)

#############
## Install ##
#############

install(
        FILES launch/commander.launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

catkin_install_python(
        PROGRAMS scripts/commander
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
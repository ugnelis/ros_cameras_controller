cmake_minimum_required(VERSION 2.8.3)
project(web_console)

add_definitions(-std=c++11)

find_package(catkin REQUIRED
    COMPONENTS
        rospy
)

catkin_python_setup()
catkin_package()

#############
## Install ##
#############

install(
        FILES scripts/web_console
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
        PERMISSIONS
            OWNER_READ OWNER_WRITE OWNER_EXECUTE
            GROUP_READ GROUP_EXECUTE
            WORLD_READ WORLD_EXECUTE
)

install(
        DIRECTORY src/static
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/src
)

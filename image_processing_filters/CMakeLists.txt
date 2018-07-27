cmake_minimum_required(VERSION 2.8.3)
project(image_processing_filters)

add_definitions(-std=c++11)

find_package(catkin REQUIRED
    COMPONENTS
        roscpp
        nodelet
        image_transport
        cv_bridge
)

find_package(OpenCV REQUIRED)

catkin_package(
        INCLUDE_DIRS include
        LIBRARIES ${PROJECT_NAME}
        CATKIN_DEPENDS
            roscpp
            nodelet
            image_transport
            cv_bridge
)

###########
## Build ##
###########

include_directories(
        include
        ${catkin_INCLUDE_DIRS}
        ${OpenCV_INCLUDE_DIRS}
)

add_library(
        ${PROJECT_NAME}
        src/ThresholdFilterNodelet.cpp
)

#add_dependencies(
#        ${PROJECT_NAME}
#        ${catkin_EXPORTED_TARGETS}
#)

target_link_libraries(
        ${PROJECT_NAME}
        ${catkin_LIBRARIES}
        ${OpenCV_LIBRARIES}
)

#############
## Install ##
#############

install(
        TARGETS ${PROJECT_NAME}
        ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
        RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
        DIRECTORY include/${PROJECT_NAME}/
        DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
        FILES_MATCHING PATTERN "*.h"
)

install(
        FILES nodelet_plugins.xml
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
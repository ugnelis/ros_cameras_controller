# image_processing_filters

## Overview

This is package lets to apply image processing filter to ROS image topics.

**Keywords:** image processing, image topic, computer vision.

### License

The source code is released under a [BSD 3-Clause license](LICENSE).

**Author(s): Ugnius Malūkas  
Maintainer: Ugnius Malūkas, ugnius@malukas.lt**

The image_processing_filters package has been tested under [ROS] Kinetic and Ubuntu 16.04.

## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)] (Middleware for Robotics),
- [OpenCV] (Computer Vision)


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/ugnelis/ros_cameras_controller.git
	cd ../
	catkin_make


## Usage

Run the main node with

	roslaunch image_processing_filters image_processing_filters.launch


## Launch files

* **image_processing_filters.launch:** applies image processing filters to running image topic. 
    
    Arguments

    - **`image_raw`** Image topic. Default: `/video_stream_to_topic/stream/image`.
    - **`threshold_value`** Threshold value. Default: `100`.


## Nodelets

### ThresholdFilterNodelet

Applies threshold filter to video stream and makes it as a ROS image topic.


#### Subscribed Topics

* **`/image_raw`** ([sensor_msgs/Image])

	Video stream.


#### Published Topics

* **`/threshold`** ([sensor_msgs/Image])

	Applied threshold filter.


#### Parameters

* **`threshold_value`** (int, default: 100)

	Threshold value.


## Bugs & Feature Requests

Please report bugs and request features using the [Issue Tracker](https://github.com/ugnelis/ros-cameras-controller/issues).


[Robot Operating System (ROS)]: http://www.ros.org
[OpenCV]: https://opencv.org
[sensor_msgs/Image]: http://docs.ros.org/api/sensor_msgs/html/msg/Image.html

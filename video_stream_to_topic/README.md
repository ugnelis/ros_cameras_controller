# video_stream_to_topic

## Overview

This is package which converts video stream (e.g. from IP camera) and makes it as a ROS image topic.

**Keywords:** stream, ip camera, topic.

### License

The source code is released under a [BSD 3-Clause license](LICENSE).

**Author(s): Ugnius Malūkas  
Maintainer: Ugnius Malūkas, ugnius@malukas.lt**

The video_stream_to_topic package has been tested under [ROS] Kinetic and Ubuntu 16.04.

## Installation

### Building from Source

#### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (Middleware for Robotics),
- [OpenCV] (Computer Vision)


#### Building

To build from source, clone the latest version from this repository into your catkin workspace and compile the package using

	cd catkin_workspace/src
	git clone https://github.com/ugnelis/ros-cameras-controller.git
	cd ../
	catkin_make


## Usage

Run the main node with

	roslaunch video_stream_to_topic video_stream_to_topic.launch


## Launch files

* **video_stream_to_topic.launch:** video streamer to image topic node is launched. 
    
    Arguments

    - **`stream_url`** Stream URL of the video. Default: `http://192.178.1.13/mjpg/video.mjpg`.
    - **`loop_rate`** Loop rate of the image publisher. Default: `5.0`.


## Nodes

### video_stream_to_topic

Converts video stream and makes it as a ROS image topic.


#### Published Topics

* **`/stream/image`** ([sensor_msgs/Image])

	Stream video as a topic.


#### Parameters

* **`stream_url`** (string, default: "http://192.178.1.13/mjpg/video.mjpg")

	Stream URL of the video.

* **`loop_rate`** (double, default: 5.0, min: 0.0)

	Loop rate of the image publisher


## Bugs & Feature Requests

Please report bugs and request features using the [Issue Tracker](https://github.com/ugnelis/ros-cameras-controller/issues).


[ROS]: http://www.ros.org
[OpenCV]: https://opencv.org
[sensor_msgs/Image]: http://docs.ros.org/api/sensor_msgs/html/msg/Image.html

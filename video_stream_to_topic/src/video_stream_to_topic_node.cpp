#include <ros/ros.h>
#include "video_stream_to_topic/VideoStreamToTopic.h"

int main(int argc, char **argv) {
    ros::init(argc, argv, "video_stream_to_topic");
    ros::NodeHandle nodeHandle("~");

    video_stream_to_topic::VideoStreamToTopic videoStreamToTopic(nodeHandle);

    ros::spin();
    return 0;
}

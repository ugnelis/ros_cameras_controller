#ifndef VIDEO_STREAM_TO_TOPIC_VIDEOSTREAMTOTOPIC_H
#define VIDEO_STREAM_TO_TOPIC_VIDEOSTREAMTOTOPIC_H

#include <ros/ros.h>

namespace video_stream_to_topic {

/**
 * Main class to handle video stream to topic.
 */
class VideoStreamToTopic {
public:
    /**
     * Constructor.
     * @param nodeHandle The ROS node handle.
     */
    explicit VideoStreamToTopic(ros::NodeHandle &nodeHandle);

    /**
     * Destructor.
     */
    virtual ~VideoStreamToTopic();

private:
    ros::NodeHandle nodeHandle_; // ROS node handle;
};

} // namespace video_stream_to_topic

#endif // VIDEO_STREAM_TO_TOPIC_VIDEOSTREAMTOTOPIC_H

#ifndef VIDEO_STREAM_TO_TOPIC_VIDEOSTREAMTOTOPIC_H
#define VIDEO_STREAM_TO_TOPIC_VIDEOSTREAMTOTOPIC_H

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>

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
    ros::NodeHandle nodeHandle_;                        // ROS node handle.
    image_transport::Publisher imagePublisher_;         // Streamed video's publisher.
    image_transport::ImageTransport imageTransport_;    // Image transport.
    std::string streamUrl_;                             // Stream URL.
    double loopRate_;                                   // Loop rate.
};

} // namespace video_stream_to_topic

#endif // VIDEO_STREAM_TO_TOPIC_VIDEOSTREAMTOTOPIC_H

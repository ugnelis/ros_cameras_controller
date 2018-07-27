#ifndef VIDEO_STREAM_TO_TOPIC_THRESHOLDFILTERNODELET_H
#define VIDEO_STREAM_TO_TOPIC_THRESHOLDFILTERNODELET_H

#include <memory>
#include <ros/ros.h>
#include <nodelet/nodelet.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <opencv2/core.hpp>

namespace image_processing_filters {

/**
 * Class to handle Threshold filter.
 */
class ThresholdFilterNodelet : public nodelet::Nodelet {
public:
    /**
     * Constructor.
     */
    explicit ThresholdFilterNodelet();

    /**
     * Destructor.
     */
    virtual ~ThresholdFilterNodelet();

    /**
     * Method is called when this nodelet is initialized.
     */
    virtual void onInit();

    /**
     * Called each time when camera image is received.
     * @param message Image message.
     */
    void imageCallback(const sensor_msgs::ImageConstPtr& message);

private:
    std::shared_ptr<image_transport::ImageTransport> imageTransport_;   // Image receiver.
    image_transport::Publisher imagePublisher_;                         // Image publisher.
    image_transport::Subscriber imageSubscriber_;                       // Image subscriber.
    int thresholdValue_; // Threshold value;
};

} // namespace image_processing_filters

#endif //VIDEO_STREAM_TO_TOPIC_THRESHOLDFILTERNODELET_H

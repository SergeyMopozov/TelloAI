'''
Created on Oct 7, 2020

@author: mrmopoz
'''
import cv2
from brain.process_video import object_detection_api_video


# get video stream
def video(logger, error_log, mode='video'):
    # get capture video
    
    cap = cv2.VideoCapture('udp://@0.0.0.0:11111', cv2.CAP_FFMPEG)
    
    # open if not open
    if not cap.isOpened():
        cap.open('udp://@0.0.0.0:11111')
    
    print('Start video')
    logger.info('Start video')
    
    while True:
        try:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret:
                # Display the resulting frame
                # process each frame in detector
                if mode =='video':
                    cv2.imshow('frame', frame)
                if mode == 'obj-detect':
                    cv2.imshow('frame', object_detection_api_video(frame))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                # command_logger.info('Stop video stream')
                # When everything done, release the capture
                cap.release()
                cv2.destroyAllWindows()
                logger.info('Stop video')
                break
        except Exception:
            error_log.exception(Exception)
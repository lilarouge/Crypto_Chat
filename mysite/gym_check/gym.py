import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose= mp.solutions.pose
#counts how many time
counter=0
#defines if my arm is up or down
stage=None
def calculate_angle(a,b,c):
    a= np.array(a)
    b= np.array(b)
    c= np.array(c)

    radians= np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle= np.abs(radians*180.0/np.pi)

    if angle > 180.0:
        angle= 360-angle

    return angle

#Video feed

cap= cv2.VideoCapture(0)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:

    while cap.isOpened():
        ret, frame = cap.read()

        #Recolor image to RGB
        image= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable =False

        #make detection
        results= pose.process(image)

        #Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #Extract body parts- landmarks
        try:
            landmarks= results.pose_landmarks.landmark

            #Get coordinates
            shoulder= [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow= [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist= [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            #Calculate angle
            angle= calculate_angle(shoulder, elbow, wrist)

            #Visualize
            cv2.putText(image,str(angle),
            tuple(np.multiply(elbow, [640,480]).astype(int)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2, cv2.LINE_AA
            )
            
            #Curl counter logic
            if angle > 160:
                stage ="down"
            if angle < 30 and stage == "down":
                stage="up"
                counter +=1

                print(counter)
            if counter >= 6:
                url = "https://www.google.com"
                webbrowser.open_new_tab(url)
                #htmlfile.open('<a href = "gym.html" target="_blank"> </a>\n')
        except:
            pass

        #Render curl counter
        #Set up status box
        cv2.rectangle(image, (0,0), (515,40), (245,117,16),-1)

        #Rep data
        cv2.putText(image, "We are just checking you're not a robot. Press q to continue", (15,12),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)

        
        #Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(245,117,66),thickness=2, circle_radius=2),
        mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2)
        )
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()




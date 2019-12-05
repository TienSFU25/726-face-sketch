import cv2
import re
from os import listdir
from os.path import isfile, join

save_to_folder = "./frames"
reg = re.compile('cam(\d).jpg')
indices = [int(reg.match(f).group(1)) for f in listdir(save_to_folder)]
i = max(indices)

cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    processed_frame = cv2.putText(frame, "Press C to capture", (100, 100),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    cv2.imshow('frame', processed_frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    if key == ord('c'):
        cv2.imwrite(save_to_folder + "/cam" + str(i) + ".jpg", frame)
        i += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

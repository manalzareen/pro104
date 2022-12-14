import cv2
img = cv2.imread("solarImg.jpg")

cv2.putText(img,
           "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
           )

cv2.putText(img,
           "Mercury",
           (120,270),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )

cv2.putText(img,
           "Venus",
           (185,270),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.putText(img,
           "Earth",
           (240,270),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.putText(img,
           "Mars",
           (287,270),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.putText(img,
           "Jupiter",
           (380,230),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.putText(img,
           "Saturn",
           (560,230),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.putText(img,
           "Uranus",
           (690,250),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.putText(img,
           "Neptune",
           (760,250),
           cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (255,255,255)    
           )
cv2.imwrite("planets_with_name.jpg",img)
cv2.imshow("output", img)
cv2.waitKey(0)
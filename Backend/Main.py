import cv2
import numpy as np
import os

import DetectPlates
import PossiblePlate


SCALAR_BLACK = (0.0, 0.0, 0.0)
SCALAR_WHITE = (255.0, 255.0, 255.0)
SCALAR_YELLOW = (0.0, 255.0, 255.0)
SCALAR_GREEN = (0.0, 255.0, 0.0)
SCALAR_RED = (0.0, 0.0, 255.0)

showSteps = False


def main():
   
    imgOriginalScene  = cv2.imread("LicPlateImages/WhatsApp Image 2019-07-27 at 1.37.30 PM.jpeg")               # open image

    if imgOriginalScene is None:                         
        print("\nerror: image not read from file \n\n")  
        os.system("pause")                                  
        return                                              
    

    listOfPossiblePlates = DetectPlates.detectPlatesInScene(imgOriginalScene)           
    
    cv2.imshow("imgOriginalScene", imgOriginalScene)  

    if len(listOfPossiblePlates) == 0:                          
        print("\nno license plates were detected\n")  
    else:                                                       
        licPlate = listOfPossiblePlates[0]

        cv2.imshow("imgPlate", licPlate.imgPlate)           
        drawRedRectangleAroundPlate(imgOriginalScene, licPlate)             

        cv2.imshow("imgOriginalScene", imgOriginalScene)                

        cv2.imwrite("imgOriginalScene.png", imgOriginalScene)           
    cv2.waitKey(0)					

    return

def drawRedRectangleAroundPlate(imgOriginalScene, licPlate):

    p2fRectPoints = cv2.boxPoints(licPlate.rrLocationOfPlateInScene)            

    cv2.line(imgOriginalScene, tuple(p2fRectPoints[0]), tuple(p2fRectPoints[1]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[1]), tuple(p2fRectPoints[2]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[2]), tuple(p2fRectPoints[3]), SCALAR_RED, 2)
    cv2.line(imgOriginalScene, tuple(p2fRectPoints[3]), tuple(p2fRectPoints[0]), SCALAR_RED, 2)


if __name__ == "__main__":
    main()



















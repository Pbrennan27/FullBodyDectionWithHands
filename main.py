import cv2
import mediapipe as mp
import time
import pygame
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()#Is set to False
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime=0
pygame.init()
y = 100

p11=10
p12=20
y11=10
y12=10
y13=20

white = (255, 255, 255)

# assigning values to X and Y variable
X = 1920
Y = 1080
point=[0,0]

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Image')
def cvimage_to_pygame(image):
    """Convert cvimage into a pygame image"""
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return pygame.image.frombuffer(image.tostring(), image.shape[1::-1],
                                   "RGB")
def load(image):
    imagename = image
    imagetitle = str(imagename)+".png"
    image = pygame.image.load(imagetitle)
while True:

    success, img = cap.read()
    img = cv2.resize(img, (1920, 1080))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    results1 = hands.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            #print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            #if(id>10 & id<16):
            if (id == 11):
                point = [cx, cy]
                p11=cx
                y11=cy
                cv2.circle(img, (cx, cy), 15, (0, 255, 0), cv2.FILLED)
            if(id==12):
                p12=cx
                y12=cy
            if(id==24):
                y13=cy
            else:
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
    if results1.multi_hand_landmarks:
        for handLms in results1.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm) #gets index node and position on img (in scale value not pixel)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    img=cv2.flip(img,1)
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    #cv2.imshow("Image", img)
    cv2.waitKey(1)
    img=cvimage_to_pygame(img)


    #y=img2.shape[1]

    #img2 = pygame.image.load('middle.png')
    #rarm = pygame.image.load('rarm.png')
    #larm= pygame.image.load('larm.png')
    #larm =pygame.transform.flip(larm,1,0)

    #img2 = cv2.resize(img2,((p11-p12),y))
    p= p12-p11
    yh= y13-y11
    if yh<0:
        yh=(yh*-1)
    if p<0:
        p=(p*-1)
    #larmSize = larm.get_size()
    #rarmSize = rarm.get_size()
    #img2=pygame.transform.scale(img2,(p,yh+100))
    #larm = pygame.transform.scale(larm,(larmSize[0]/2,yh+100))
    #rarm = pygame.transform.scale(rarm, (rarmSize[0]/2, yh + 100))




    display_surface.fill(white)
    display_surface.blit(img,(0,0))

    #display_surface.blit(rarm,((1920-p12),(y12-100)))
    #display_surface.blit(larm, ((1920-(p11+(larmSize[0]/2))), (y12 - 100)))
    #display_surface.blit(img2, (1920 - point[0], point[1] - 100))
    #load('d16d8a96d54a4c56b60fb0934815c5d2-removebg-preview')
    pygame.display.update()
    #for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
     #   if event.type == pygame.QUIT:
            # deactivates the pygame library
       #     pygame.quit()
            # quit the program.
      #      quit()

        # Draws the surface object to the screen.
        #pygame.display.update()


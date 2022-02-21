"""21/02/2022"""
"""Added Face depth detection - this can be used to accurately calculate a persons height by using a fixed scale based on
their distance from the camera
Currently this is about 10% inaccurate on what the actualy distance from the camera is . Need to adjust W and/or w
values in code"""
"""Pytorch seems to be the best library for converting 2d images to 3d models, need to research on how to use this 
properly"""
"""Once Pytorch part of project is complete I can use the OBJLoader.py to load the model into the program, the object's
 center will be at the depth of the FaceDepthMeasurement + a constant (average distance from front of face to center of head).
 This should center the clothing on the persons body and have it exactly to scale"""
"""Need to find way to overlay the clothing via OpenGL or other methods, currently unable to display the .obj file in
a pygame window with the camera showing as well"""

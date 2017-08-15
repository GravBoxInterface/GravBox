# GravBox
## PROJECT SYNOPSIS

GravBox is the interface application for the Augmented Reality (AR) Sandbox for gravitational dynamics simulations designed and built at the University of Iowa by Dr. Hai Fu\'s 2016-2017 Introduction to Astrophysics class. The GravBox application was developed by Zachary Luppen, Erin Maier, and Mason Reed. The sandbox was designed and built by Wyatt Bettis, Ross McCurdy, and Sadie Moore. The gravitational algorithm was written by Sophie Deam, Jacob Isbell, and Jianbo Lu. Graphic design was contributed by Jeremy Swanston. The original AR Sandbox is the result of an NSF-funded project on informal science education for freshwater lake and watershed science developed by the UC Davis' W.M. Keck Center for Active Visualization in the Earth Sciences, together with the UC Davis Tahoe Environmental Research Center, Lawrence Hall of Science, and ECHO Lake Aquarium and Science Center. To learn more about the GravBox project, contact Hai Fu at hai-fu@uiowa.edu, or visit our Github at https://github.com/GravBoxInterface/GravBox.

## RESOURCES FOR USING GRAVBOX

A tablet is used for interaction and input on the AR Sandbox device. The tablet is a Samsung Galaxy Tab A, with a 1920x1200 pixel ratio. After the password to the tablet is entered, the kivy launcher app is located on the home screen. When pressed, it opens up all of the kivy apps currently saved on the tablet. Tapping on the Gravbox app opens it. The app works by having the user input the speed and direction of a particle from the starting location of their choice, and then having it interact with the topography created by the sand and read in by the Kinect. A user simply drags their finger across the screen to decide the particle's location, speed and direction. Location is determined by where the user initially places their finger. Speed is indicated by how long the vector is, which has a maximum length built into the app. Direction is indicated by where the user moves their finger, and is updated in real-time as the user moves their finger across the screen, allowing them to pick what direction they want. Once the user lifts their finger from the screen, this data is automatically written into a .txt file, which the gravity algorithm detects and reads in.



### KIVY



### BUILDOZER



### PYTHON



### GRAVITY ALGORITHM
https://github.com/jwisbell/gravity_sandbox

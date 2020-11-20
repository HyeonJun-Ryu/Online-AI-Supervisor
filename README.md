# Online-AI-Supervisor (OAS)

## Team Member
1. HyeonJun Ryu(Team Leader, Main Developer) - Kyungpook National University, Computer And Science / hjryu1816@gmail.com
2. MinJe Seok(Secondary Developer, Document manager) - Kyungpook National University, Department of Agricultural Civil and Biological Engineering / mjseok8@naver.com

## DEMO
1. Test start with OAS(Online-AI-Supervisor).

2. The program will detect your face like below picture.
<img width="1392" alt="1" src="https://user-images.githubusercontent.com/74097144/99790982-43dbbf00-2b68-11eb-889e-d42aecc6b354.png">

3. Next, OAS will capture your eyes like below picture.
<img width="579" alt="1-2" src="https://user-images.githubusercontent.com/74097144/99791722-5a364a80-2b69-11eb-929d-0f353638a9c1.png">

4. Now, OAS will track your eyes.
<img width="991" alt="2-1" src="https://user-images.githubusercontent.com/74097144/99791015-4f2eea80-2b68-11eb-9f63-e3301364eebf.png">
<img width="991" alt="2" src="https://user-images.githubusercontent.com/74097144/99791007-4dfdbd80-2b68-11eb-9f32-1b175e7a3bef.png">

5. And OAS predict your gaze on the screen like this.
<img width="437" alt="4" src="https://user-images.githubusercontent.com/74097144/99792169-0c6e1200-2b6a-11eb-819e-48d2663c004d.png">
(The red dot is where you look as OAS predicted.)

 
6. If the eyes are out of the test screen(like below picture) for more than a certain period of time, a warning and disqualification will be processed.
<img width="651" alt="5" src="https://user-images.githubusercontent.com/74097144/99792663-c1a0ca00-2b6a-11eb-8b37-2acafb8c0916.png">
(The red dot is where you look as OAS predicted.)

## 0. Development Environment
* MacBook Pro 13" TouchBar 2020
* macOS Catalina 10.15.7
* Python 3.8.2
* IDE: PyCharm CE 2020.2.3
* opencv-python-3.4.8.29

## 1. Installation
(This guide is based on python and pycharm installed.)

In PyCharm terminal, enter this command. " pip install opencv-python==3.4.8.29 " (The new version may not work properly.)

## 2. How to use

2020/11/20 - Progress about 70 %

OAS/eyetracker.py - Open file on IDE like Pycharm and Run. *"eye_recording.flv" This video must be in the same folder.*

OAS/facedetect.py - Open file on IDE like Pycharm and Run. * Need a cam *

If you want stop the program, press esc.

If an Opencv related error occurs, run the following command.
< pip uninstall opencv >
< pip install opencv-python=3.4.8.29 >

Errors can occur in the latest version of opencv.


## 3. Contribute

Progressing...

## Log
NTF - Need To Fix
About Develop - (D)

* 2020/11/03 - 1st Planning Meeting, 
* 2020/11/10(D) - Project OAS Started, Built a based source code(main,py), Applied Webcam(NTF - Can't recognize eyes), Built a code that detect face & eye(eye.py)
* 2020/11/11 - 2nd Planning Meeting, Decided a team name(Practical Code (PC)), Planned OAS project.
* 2020/11/11(D) - Enabled always eye tracking, Started work on eyes' area detecting. (NFT: It can't recognize  face and eyes well when I wearing a mask. And also, it can't find eyes when I wear glasses.)
* 2020/11/20 - 

## Reference

* Pysource, "Eye motion tracking - Opencv with Python", Youtube [https://youtu.be/kbdbZFT9NQI]
* https://pysource.com/2019/01/04/eye-motion-tracking-opencv-with-python/
* haarcascade_eye.xml, haarcascade_frontalface_default.xml used in eye.py - https://github.com/opencv/opencv/tree/master/data/haarcascades

## Contact

* hjryu1816@gmail.com
* xptmffk816@knu.ac.kr



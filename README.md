# urbanAI 2022

# Usage

## Server Setup
Note: 
- Make sure you have Python3 installed on your machine. 
- The following instructions are for MacOS and Linux users. I'm not sure how it works on Windows.

1. Make sure that you have all necessary requirements for Python3. To install any missing requirements, open a terminal and run `pip3 install -r requirements.txt`

2. Run `python3 application.py`

3. Go to `http://127.0.0.1:3000/index.html`

4. When you are finished, press `Ctrl+C` on the terminal to stop the server.


# Notes

---

05/10/2022 -
Merged with 'load-geometry' branch.

---

W2 21/09/2022:
**The WebGL frame**

Scrum Sprints

Build the framework:
1.	**Joey –**
      HTML/CSS styling of webpage
-	Building frame for ThreeJS app.

ThreeJS: <br>

2.	**Russell –**
      Scene setup - framework for basic structure of scene
- Camera setup
3.	**Owen –**
      Existing geometry conversion to GLTF (existing urban geometry)
- Simple building envelopes.
- Extends to API in later stages for selecting map areas - Convert JSON to GLTF
4.	**Chris –**
      Load geometry option - load for different geometry as an option (GLTF)
- Backend storage solutions.
5.	**Nila –**
      Sun/lighting configuration options
- Moving the sun based on number slider

Notes:<br>
⁃	Camera should focus on centred origin of geometry<br>
⁃	Camera should be able to rotate and pan<br>
⁃	For this sprint no materials or textures are required<br>
⁃	GLTF overview - https://www.khronos.org/files/gltf20-reference-guide.pdf <br>
⁃   THREEJS scene overview - https://threejs.org/docs/index.html#manual/en/introduction/Creating-a-scene




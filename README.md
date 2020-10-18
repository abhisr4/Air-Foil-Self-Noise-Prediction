# Air Foil Self Noise Prediction

A simple Flash Web application to predict the air foil self noise.

# Dataset
The dataset can be found UCI Machine Learning Repository.
  Link: https://bit.ly/3j89KVt
The dataset comprises different size NACA 0012 airfoils at various wind tunnel speeds and angles of attack.

The problem has following inputs:
  1. Frequency in Hz
  2. Angle of attack
  3. Chord Length
  4. Free-stream velocity in m/s
  5. Suction side displacement thickness, in meters

The only output is -> scaled sound pressure level, in decibles

# Tools Used
 1. HTML, CSS
 2. Flask framework
 3. Python tensorflow library
 4. Jupyter Notebook for training the model
 5. Machine Learning libraries

# Additional Notes
 1. I have used Aritifical Neural Network to build the regression model.
 2. Any regression will do the following task but conventional regression model is not that suitable. Recurrent Neural Network, Convolutional Neural Network Models might do the job as well.

# Pipe Loss App

This is a Python App built with Kivy Library which computes the head loss of a fluid moving along a pipe system taking into account Major and minor losses. 



## 🔰 How does it work?

This app is built using Kivy builder settings. It has several windows where an user could input the data to compute the head losses of a fluid into a pipe system with accesories.

## Main Window

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/1.png" width = "500">

There are 3 windows where an user could input the data:
* Fluid Properties
* Pipe Characteristics
* Accesories

And there is a button to compute the head loss.


## Fluid Properties

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/2.png" width = "500">

In this window an user must input the flow rate in $\frac{m^3}{s}$, and select the fluid in order to load its density $(\frac{kg}{m^3})$ and dynamic viscosity $(Pa-s)$. By default, an user could select any of the following fluids:
* Water
* Air
* Glycerine
* Oil
* Gasoline

But there is an *Other* option which open another window where the user could input data such as:
* Name of the fluid
* Density
* Dynamic Viscosity

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/3.png" width = "500">


## Pipe Characteristics
<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/4.png" width = "500">

In this window an user must input the length of the pipe $(m)$. After that, it's necessary to set the *Material Roughness* and the *Geometry Section*

### Material Roughness

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/5.png" width = "500">

There is a list of default materials with its roughness $(m)$. But the user could select *Other Material* option in order to input the data for a specific pipe material.

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/6.png" width = "500">

### Geometry Section

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/7.png" width = "500">

In this window there are 4 option of cross section for the pipe:
* Circular
<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/G1.JPG" width = "100">

* Annular Circular
<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/G2.JPG" width = "100">

* Rectangular
<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/G3.JPG" width = "100">

* Annular Rectangular
<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/G4.JPG" width = "100">

If the user selects any of the geometries a new window appears where is possible input the geometry data.

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/8.png" width = "500">


## Accessories

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/9.png" width = "500">


In this window the user must select the type of inlet (connection with a tank)
* No inlet
* Inward-projecting
* Sqaure-edged
* Chamfered

Also it's necessary to define whether there is an outlet or not using the switch

Finally, the *Accessories Button* shows a window with a list a common accessories in pipeline systems such as valves, elbows etc. An user just need to enter the number of each accesory in the pipeline system. By default, all accessories have a value of 0.

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/10.png" width = "500">

## Example
This is the solution of the problem 11.7 from the book *Applied Fluid Mechanics, 7th by Mott R. and Untener J.*

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/11.png" width = "500">

<img src = "https://raw.githubusercontent.com/alejo1630/pipe_loss/main/Images/App/12.png" width = "500">

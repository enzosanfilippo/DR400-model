# DR400 Aircraft Modeling in OpenVSP

![Status](https://img.shields.io/badge/status-in%20progress-yellow)

## Overview
This project focuses on the **geometric modeling of the Robin DR400** aircraft using **OpenVSP**.  
The DR400 is a legendary training aircraft in French flying clubs, and I personally logged over **40 flight hours** on this plane.  
This project is developed by an aeronautics enthusiast and engineering student, passionate about flight mechanics and aircraft modeling.
I am always open to discussions and collaborations around flight simulation, aerodynamics, and aircraft design.

The motivation behind this project was to:
- Take on the challenge of self-learning an aircraft modeling tool  
- Strengthen my aeronautical engineering skills with a hands-on project  
- Contribute the **first DR400 model publicly available for OpenVSP**  

The learning process was mostly based on YouTube tutorials and self-experimentation.

---

##  Project Content
The OpenVSP geometry file includes:
- Fuselage  
- Wings  
- Elevator 
- Fairings and landing gear wheels  
- Propeller  

---

##  Future Improvements
Several aspects can be refined to improve the accuracy of the model:
- Implement the **exact propeller** model used on DR400 aircraft  
- Refine the **fairings and wheel dimensions** to match reality  
- Define and include the **center of mass**  
- Generate a **coherent mesh** that can be processed by the **VSPAero module**  
  (currently, VSPAero fails due to mesh inconsistencies)  

---

##  Next Steps
The next major development will focus on **automating aerodynamic coefficient calculations** using the Python API for OpenVSP.  

Current limitation: version conflicts between **Spyder** (Python environment) and **OpenVSP** prevent smooth API integration.  

---

##  Contributions
I am open to external contributions and collaboration with fellow aviation enthusiasts!  
Ways to contribute:
- Improving the current geometry and mesh and skinning quality  
- Helping set up the Python API for aerodynamic automation  
- Sharing insights on best practices for OpenVSP and VSPAero  

If you have experience with OpenVSP, VSPAero, or aerodynamics simulation in general, your help will be highly appreciated !

---

##  Repository Structure  
- /geometry/ → dr_400.vsp3 # Main OpenVSP geometry file
- /plan_dr400/ → handwrited sketch of the DR400-120 found on opensource
- /lift_coefficent.py/ → personal python program still need to be worked on as noticed before

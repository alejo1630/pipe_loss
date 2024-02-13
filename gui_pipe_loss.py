from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import math
import numpy as np


# Set size of the app
Config.set("graphics", "width", "600")
Config.set("graphics", "height", "600")
Config.set('graphics', 'resizable', False)


class IntroWindow(Screen):
    
    def calculation(self):
        global fluid_name, density, viscosity, geo, material_name, roughness, inlet_value, outlet_check

        calculation_screen = self.manager.get_screen("calculation")

        # FLuid Properties
        density = float(density)
        viscosity = float(viscosity)
        calculation_screen.ids.fluid_r.text = f"{fluid_name}"
        calculation_screen.ids.density_r.text = f"{density}"
        calculation_screen.ids.viscosity_r.text = f"{viscosity}"

        # Pipe Geometry
        if geo == "Circular": # Circular
            g1_screen = self.manager.get_screen("g1")

            d_h =  float(g1_screen.ids.g1_D.text)# Diameter (m)
            area = math.pi * d_h**2 / 4 # Area (m2)

        elif geo == "Annular Circular": # Annular circular
            g2_screen = self.manager.get_screen("g2")

            D = float(g2_screen.ids.g2_D.text) # (m)
            d = float(g2_screen.ids.g2_d.text) # (m)
            area = math.pi * (D**2 - d**2) / 4 # Area (m2)
            wp = math.pi * (D + d) # wetted perimeter (m)
            r_h = area/wp # hydraulic radius (m)
            d_h = 4*r_h # hydraulic diameter (m)

        elif geo == "Rectangular": # Rectangular
            g3_screen = self.manager.get_screen("g3")

            b = float(g3_screen.ids.g3_B.text) # Base (m)
            h = float(g3_screen.ids.g3_H.text) # Height (m)
            area = b * h # Area (m2)
            wp = 2*b + 2*h # wetted perimeter (m)
            r_h = area/wp # hydraulic radius (m)
            d_h = 4*r_h # hydraulic diameter (m)

        elif geo == "Annular Rectangular": # Annular Rectangular
            g4_screen = self.manager.get_screen("g4")

            b = float(g4_screen.ids.g4_B.text) # Base (m)
            h = float(g4_screen.ids.g4_H.text) # Height (m)
            d = float(g4_screen.ids.g4_d.text) # (m) 
            area = (b * h) - (math.pi * d**2 /4) # Area (m2)
            wp = (2*b + 2*h) + (math.pi * d) # wetted perimeter (m)
            r_h = area/wp # hydraulic radius (m)
            d_h = 4*r_h # hydraulic diameter (m)
        
        calculation_screen.ids.pipe_geometry_r.text = f"{geo}"
        calculation_screen.ids.pipe_dh_r.text = f"{d_h:.3f}"
        calculation_screen.ids.pipe_area_r.text = f"{area:.3f}"

        # Flow rate
        fluid_screen = self.manager.get_screen("fluid")
        Q = float(fluid_screen.ids.fluid_rate.text)
        calculation_screen.ids.flow_rate_r.text = f"{Q}"

        # Velocity
        vel = Q/area
        calculation_screen.ids.velocity_r.text = f"{vel:.3f}"

        # Reynolds
        Re = (density * vel * d_h) / viscosity
        calculation_screen.ids.reynolds_r.text = f"{Re:.2e}"

        # Pipe Length
        pipe_screen = self.manager.get_screen("pipe")
        L = float(pipe_screen.ids.pipe_length.text)
        calculation_screen.ids.length_r.text = f"{L}"

        # Pipe material
        calculation_screen.ids.pipe_material_r.text = f"{material_name}"

        # Roughness
        roughness = float(roughness)
        calculation_screen.ids.roughness_r.text = f"{roughness}"

        # Relative Roughness
        rel_rough = d_h/roughness
        calculation_screen.ids.relative_roughness_r.text = f"{rel_rough:.3f}"
        
        # Friction Factor
        f = 0.25/(math.log10(1/(3.7*rel_rough) + 5.74/(Re**0.9)))**2
        calculation_screen.ids.friction_factor_r.text = f"{f:.5f}"

        # Complete turbulence friction factor
        ft = 0.25/(math.log10(1/(3.7*rel_rough)))**2
        calculation_screen.ids.friction_factor_turbulence_r.text = f"{ft:.5f}"

        # Inlet
        if inlet_value == "Inward-projecting":
            k_inlet = 0.78

        elif inlet_value == "Square-edged":
            k_inlet = 0.5

        elif inlet_value == "Chamfered":
            k_inlet = 0.25         

        else:
            k_inlet = 0      

        # Outlet
            
        if outlet_check == True:
            k_outlet = 1
        else:
            k_outlet = 0
            
        # Accessories
        
        acc_values = np.array([340, 150, 8, 35, 160, 800, 100, 150, 45, 3, 420, 75, 30, 16, 50, 20, 60])

        k_acc = np.dot(acc_values, list_acc)

        # K Major Loss

        K_M = f * (L/d_h)

        # K _total
        K_total = k_inlet + k_outlet + k_acc * ft + K_M
        calculation_screen.ids.resistance_coefficient_r.text = f"{K_total:.2f}"

        # Head Loss
        H_L = K_total * (vel**2 / (2*9.81))
        calculation_screen.ids.head_loss_r.text = f"{H_L:.2f}"


class FluidWindow(Screen):
    checks = []

    def checkbox_click(self, instance, value, fluid):

        global density, viscosity, fluid_name

        fluids = {
                "Water" : [1000 , 1e-3],
                "Air" : [1.2, 1.8e-5],
                "Glycerine" : [1260, 1.5],
                "Oil" : [900, 3e-2],
                "Gasoline" : [680, 2.9e-4]
                }
        if value == True:
            FluidWindow.checks.append(fluid)

            if FluidWindow.checks[0] != "Other":
                fluid_name = FluidWindow.checks[0]
                density = fluids[FluidWindow.checks[0]][0]
                viscosity = fluids[FluidWindow.checks[0]][1]
            
            else:
                other_screen = self.manager.get_screen("other_fluid")
                fluid_name = other_screen.ids.fluid_name.text
                density = other_screen.ids.density_text.text
                viscosity = other_screen.ids.viscosity_text.text

            self.ids.density_label.text = f"Density: {density} kg/m3"
            self.ids.viscosity_label.text = f"Viscosity: {viscosity} Pa-s"
            
        else:
            FluidWindow.checks.remove(fluid)


class PipeWindow(Screen):
    pass


class AccessoriesWindow(Screen):

    global outlet_check

    inlet_check = []
    outlet_check = False

    def checkbox_click(self, instance, value, inlet):
        
        global inlet_value

        if value == True:
            AccessoriesWindow.inlet_check.append(inlet)

        else:
            AccessoriesWindow.inlet_check.remove(inlet)

        inlet_value = AccessoriesWindow.inlet_check[0]

    def switch_click(self, switchObject, switchValue):
        global outlet_check

        outlet_check = switchValue
        

class OtherFluidWindow(Screen):

    def change_properties(self):
        global density, viscosity, fluid_name

        fluid_name = self.ids.fluid_name.text
        density = self.ids.density_text.text
        viscosity = self.ids.viscosity_text.text

        other_screen = self.manager.get_screen("fluid")

        other_screen.ids.density_label.text = f"Density: {density} kg/m3"
        other_screen.ids.viscosity_label.text = f"Viscosity: {viscosity} Pa-s"


class RoughnessWindow(Screen):
    checks_material = []

    def checkbox_click(self, instance, value, material):
        global material_name, roughness

        roughness_material = {
                            "Glass" : 0,
                            "Plastic" : 3e-7,
                            "Copper" : 1.5e-6,
                            "Brass" : 1.5e-6,
                            "Steel" : 1.5e-6,
                            "Commercial Steel" : 4.6e-5,
                            "Welded Steel" : 4.6e-5,
                            "Galvanized Iron" : 1.5e-4,
                            "Ductile Iron-Coated" : 1.2e-4,
                            "Ductile Iron-Uncoated" : 2.4e-4,
                            "Concrete": 1.2e-4,
                            "Riveted Steel": 1.8e-3
                            }
        
        if value == True:
            RoughnessWindow.checks_material.append(material)

            if RoughnessWindow.checks_material[0] != "Other Material":
                material_name = RoughnessWindow.checks_material[0]
                roughness = roughness_material[RoughnessWindow.checks_material[0]]

            else:
                other__screen = self.manager.get_screen("other_material")
                roughness = other__screen.ids.roughness_text.text

            self.ids.roughness_label.text = f"{roughness}"

        else:
            RoughnessWindow.checks_material.remove(material)


class OtherMaterialWindow(Screen):
    
    def other_material_info(self):

        global material_name, roughness

        material_name = self.ids.material_pipe.text
        roughness = self.ids.roughness_text.text

        other_screen = self.manager.get_screen("roughness")

        other_screen.ids.roughness_label.text = f"{roughness}"


class GeometryWindow(Screen):
    
    global geo

    geo = ""

    def g1(self):
        global geo 

        geo = "Circular"
    
    def g2(self):
        global geo 
        
        geo = "Annular Circular"

    def g3(self):
        global geo 
        
        geo = "Rectangular"

    def g4(self):
        global geo 
        
        geo = "Annular Rectangular"


class G1Window(Screen):
    pass


class G2Window(Screen):
    pass


class G3Window(Screen):
    pass


class G4Window(Screen):
    pass


class ListAccWindow(Screen):
    
    def accessories_values(self):
        global list_acc

        list_acc = np.zeros(17)

        list_acc[0] = self.ids.globe_valve.text
        list_acc[1] = self.ids.angle_valve.text
        list_acc[2] = self.ids.gate_valve_FO.text
        list_acc[3] = self.ids.gate_valve_3_4.text
        list_acc[4] = self.ids.gate_valve_1_2.text
        list_acc[5] = self.ids.gate_valve_1_4.text
        list_acc[6] = self.ids.check_valve_swing.text
        list_acc[7] = self.ids.check_valve_ball.text
        list_acc[8] = self.ids.butterfly_valve.text
        list_acc[9] = self.ids.ball_valve.text
        list_acc[10] = self.ids.foot_valve_poppet.text
        list_acc[11] = self.ids.foot_valve_hinged.text
        list_acc[12] = self.ids.elbow_90.text
        list_acc[13] = self.ids.elbow_45.text
        list_acc[14] = self.ids.return_bend.text
        list_acc[15] = self.ids.t_flow_run.text
        list_acc[16] = self.ids.t_flow_branch.text
    

class CalculationWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


# Builder based on the .kv file
kv = Builder.load_file('PipeLoss.kv')

# App
class PipeLoss(App):

    def build(self):
        return kv


if __name__ == "__main__":

    PipeLoss().run()


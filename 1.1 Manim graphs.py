#import necessary libs
from manimlib.imports import *
import numpy as np 

# Develop the graphs 

class graphx(GraphScene):
    CONFIG={
        "x_min": -4,
        "x_max": 4,
        "y_min": -2,
        "y_max": 2,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "graph_origin": 0.5 * DOWN + 0 * LEFT,
    }

    # Defining graph functions 
    def show_function_graph(self): 
        self.setup_axes(animate=True)
        # Math function
        def func(x):
            return np.sin(x)
        def func2(x):
            return np.cos(x)
        #sin graph
        graph_sin=self.get_graph(func,x_min=-np.pi, x_max=np.pi)
        graph_sin.set_color(RED)
        # Cos graph
        graph_cos=self.get_graph(func2,x_min=-np.pi, x_max=np.pi)
        graph_cos.set_color(YELLOW)
        
        # Play grapgs
        self.play(ShowCreation(graph_sin), run_time=3)
        self.wait(1)
        # self.play(ShowCreation(graph_cos), run_time=3)
        self.wait(1)
        # Adding text 
        text1=TextMobject('y=f(x)').set_height(1.1)
        text1.set_color(BLUE)
        text1.next_to(graph_cos, UP)
        text1.shift(1.5*UP)
        self.play(Write(text1))
        self.wait(3)
        #creat a picture 
        picture= Group(*self.mobjects)
        picture.scale(0.6).to_edge(LEFT, buff=SMALL_BUFF)
        manim=TextMobject('1.1 Manim').set_height(1.1).next_to(picture, RIGHT)
        manim.shift(UP)
        Tutorial=TextMobject('Graphs', tex_to_color_map={'Graphs': YELLOW}).set_height(1.1).next_to(manim, DOWN,buff=1.5)
        # Tutorial.set_color(YELLOW)

        self.play(ShowCreation(manim))
        self.play(ShowCreation(Tutorial))
        self.wait(3)


    # Defining construction
    def construct(self):
        self.show_function_graph()


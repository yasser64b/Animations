class int():
	CONFIG = {
	"y_max": 2,
	"x_max": 2,
	"y_axis_height": 5,
	"y_axis_label": "$f(x)$",
	}
	def construct(self):

	# Drawings 

		self.show_function_graph()
	def show_function_graph(self):
		self.setup_axes(animate=False)
		def func1(x):
			return (x**0.5)

		def func2(x):
			return (x**2)


		def rect(x):
			return 2.775*(x-1.5)+3.862
		recta = self.get_graph(rect,x_min=0,x_max=1)
		graph1 = self.get_graph(func1,x_min=0,x_max=1.5)
		graph2 = self.get_graph(func2,x_min=-1.3,x_max=1.3)

		graph1.set_color(YELLOW)
		graph2.set_color(BLUE)

		input_tracker_p1 = ValueTracker(.001)
		input_tracker_p2 = ValueTracker(1)		
		
		def get_x_value(input_tracker):
			return input_tracker.get_value()

		def get_y_value(input_tracker):
			return graph1.underlying_function(get_x_value(input_tracker))

		def get_x_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), 0)

		def get_y_point(input_tracker):
			return self.coords_to_point(0, get_y_value(input_tracker))

		def get_graph_point(input_tracker):
			return self.coords_to_point(get_x_value(input_tracker), get_y_value(input_tracker))

		def get_v_line(input_tracker):
			return DashedLine(get_x_point(input_tracker), get_graph_point(input_tracker), stroke_width=2)

		def get_h_line(input_tracker):
			return DashedLine(get_graph_point(input_tracker), get_y_point(input_tracker), stroke_width=2)
		#
		input_triangle_p1 = RegularPolygon(n=3, start_angle=TAU / 4)
		output_triangle_p1 = RegularPolygon(n=3, start_angle=0)
		for triangle in input_triangle_p1, output_triangle_p1:
			triangle.set_fill(WHITE, 1)
			triangle.set_stroke(width=0)
			triangle.scale(0.1)
		# 
		input_triangle_p2 = RegularPolygon(n=3, start_angle=TAU / 4)
		output_triangle_p2 = RegularPolygon(n=3, start_angle=0)
		for triangle in input_triangle_p2, output_triangle_p2:
			triangle.set_fill(WHITE, 1)
			triangle.set_stroke(width=0)
			triangle.scale(0.1)

		# 
		x_label_p1 = TexMobject("a")
		output_label_p1 = TexMobject("f(a)")
		x_label_p2 = TexMobject("b")
		output_label_p2 = TexMobject("f(b)")
		v_line_p1 = get_v_line(input_tracker_p1)
		v_line_p2 = get_v_line(input_tracker_p2)
		h_line_p1 = get_h_line(input_tracker_p1)
		h_line_p2 = get_h_line(input_tracker_p2)
		graph_dot_p1 = Dot(color=WHITE)
		graph_dot_p2 = Dot(color=WHITE)

		#functions on graphs
		function1=TexMobject('\\sqrt x').set_color(YELLOW)
		function1.next_to(graph1, RIGHT+UP, buff=0)

		function2=TexMobject('x^2').set_color(BLUE)
		function2.next_to(graph1, UP+RIGHT, buff=0)
		function2.shift(LEFT+UP)

	
		# reposition mobjects
		x_label_p1.next_to(v_line_p1, DOWN)
		x_label_p2.next_to(v_line_p2, DOWN)
		output_label_p1.next_to(h_line_p1, LEFT)
		output_label_p2.next_to(h_line_p2, LEFT)
		input_triangle_p1.next_to(v_line_p1, DOWN, buff=0)
		input_triangle_p2.next_to(v_line_p2, DOWN, buff=0)
		output_triangle_p1.next_to(h_line_p1, LEFT, buff=0)
		output_triangle_p2.next_to(h_line_p2, LEFT, buff=0)
		graph_dot_p1.move_to(get_graph_point(input_tracker_p1))
		graph_dot_p2.move_to(get_graph_point(input_tracker_p2))
		
		#play functions
		self.play(ShowCreation(graph1), run_time=4)
		self.play(ShowCreation(function1))
		self.play(ShowCreation(graph2), run_time=4)
		self.play(ShowCreation(function2))

		# Explanations 
		text1 = TextMobject("A=Region bounded by two curves?").set_color(YELLOW)
		text2 = TextMobject("Find points of intersection")
		text1.to_edge(UP)
		self.play(Write(text1))
		self.wait(4)
		text2.next_to(text1, DOWN, buff=0.2)
		self.play(Write(text2))
		self.wait(1)


		# Animacion del punto a
		self.add_foreground_mobject(graph_dot_p1)
		self.add_foreground_mobject(graph_dot_p2)
		self.play(
		    DrawBorderThenFill(input_triangle_p1),
		    Write(x_label_p1),
		    ShowCreation(v_line_p1),
		    GrowFromCenter(graph_dot_p1),
		    ShowCreation(h_line_p1),
		    Write(output_label_p1),
		    DrawBorderThenFill(output_triangle_p1),
		    DrawBorderThenFill(input_triangle_p2),
		    Write(x_label_p2),
		    ShowCreation(v_line_p2),
		    GrowFromCenter(graph_dot_p2),
		    ShowCreation(h_line_p2),
		    Write(output_label_p2),
		    DrawBorderThenFill(output_triangle_p2),
		    run_time=3
		)


	# 	##################		
		pendiente_recta = self.get_secant_slope_group(
			1.9, recta, dx = 1.4,
		    df_label = None,
		    dx_label = None,
		    dx_line_color = RED,
		    df_line_color= ORANGE,
		    )
		grupo_secante = self.get_secant_slope_group(
		    1.5, graph1, dx = 2,
		    df_label = None,
		    dx_label = None,
		    dx_line_color = "#942357",
		    df_line_color= "#3f7d5c",
		    secant_line_color = BLUE,
		)

	# 	self.play(FadeIn(grupo_secante), run_time=3)		


		kwargs = {
		    "x_min" : 0.01,
		    "x_max" : 1,
		    "fill_opacity" : 0.75,
		    "stroke_width" : 0.25,
		}
		self.graph1=graph1
		self.graph2=graph2
		iteraciones=6

		self.rect_list1 = self.get_riemann_rectangles_list(
		    graph1, iteraciones,start_color=PURPLE,end_color=ORANGE, **kwargs
		)
	#graph 2
		self.rect_list2 = self.get_riemann_rectangles_list(
		    graph2, iteraciones,start_color=BLACK,end_color=BLACK, **kwargs
		)

		flat_rects = self.get_riemann_rectangles(
		    self.get_graph(lambda x : 0), dx = 0.05,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs)

		rects1 = self.rect_list1[4]
		rects2 = self.rect_list2[4]


		self.transform_between_riemann_rects(
		    flat_rects, rects1, 
		    replace_mobject_with_target_in_scene = True,
		    run_time=6
		)

		text4 = TexMobject("A_1").set_color(YELLOW)
		text4.next_to(graph1,LEFT, buff=0.2)
		text4.shift(1.7*RIGHT+0.8*DOWN)
		self.play(Write(text4))
		self.wait(2)


		self.transform_between_riemann_rects(
		    flat_rects, rects2, 
		    replace_mobject_with_target_in_scene = True,
		    run_time=6
		)
		self.wait (1)
		
		text5 = TexMobject("A_2").set_color(BLUE)
		text5.next_to(graph2,RIGHT, buff=0.2)
		text5.shift(1.9*LEFT+0.8*DOWN)
		self.play(Write(text5))
	

		text6 = TexMobject("A")
		text6.next_to(graph2,RIGHT, buff=0.2)
		text6.shift(3*LEFT+0.4*DOWN)
		self.play(Write(text6))
		#over write



		# self.wait (3)
		
		self.play(FadeOut(text2))	
		self.wait()

		self.add(graph2)

		text3 = TexMobject("A=","A_1", "-", "A_2")
		text3[1].set_color(YELLOW)
		text3[3].set_color(BLUE)
		text3.next_to(text1, DOWN, buff=0.2)
		self.play(Write(text3))
		self.wait(3)

		self.play(FadeOut(text3), FadeOut(text1))	
		self.wait()
		# self.play(FadeOut(sqrt))
		# adding mani		
		picture = Group(*self.mobjects)
		picture.scale(0.8).to_corner(UP+LEFT, buff=SMALL_BUFF)
		self.play(FadeInFrom(picture,DOWN, runtime=3))
		self.wait(3)

		# Import furmulas
		self.import_formulas()
		self.write_formulas()
		self.set_changes()

		# Int_title=TextMobject("Power Substitution:}")
		# # Int_title.shift(2*RIGHT)
		# Int_title.set_color(YELLOW)
		# Int_parts=TexMobject('\\begin{cases} u=\\sqrt{x} \\\\ x=u^2 \\\\ dx=2u du \end{cases}')
		# Int_parts.set_color(YELLOW)


		# [1] \int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	?
		# [2]\int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	? 		
		self.step_formula(n_step=1,
			changes=self.set_of_changes[1-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			write=[],
			)

		# Int_title.next_to(formulas[0], UP, buff=2)
		# Int_parts.next_to(formulas[0], RIGHT, buff=1)
		# self.play(Write(Int_title), Write(Int_parts))
		# self. wait(3)
		# self.play(FadeOut(Int_title),FadeOut(Int_parts))
		# self.wait(2)

		#[2]
		#[3]
		self.step_formula(n_step=2,
			changes=self.set_of_changes[2-1],
			pre_copy=[],
			pos_copy=[],
			fade=[0,6,7,8,9],
			pos_write=[],
			time_pre_changes=1,
			time_pos_changes=1,
			# path_arc=-PI,
			# run_time=4
			)

		# Int_parts.next_to(self.formulas[2], UP, buff=1)
		# Int_parts.shift(3*RIGHT)
		# self.play(Write(Int_parts))
		# self.wait(2)

		# c1=SurroundingRectangle(self.formulas[2][5:8],buff=0.1).set_color(YELLOW)
		# c2=SurroundingRectangle(self.formulas[2][23],buff=0.1).set_color(YELLOW)
	
		# c3=SurroundingRectangle(self.formulas[2][11:14],buff=0.1).set_color(YELLOW)
		# c4=SurroundingRectangle(self.formulas[2][25],buff=0.1).set_color(YELLOW)
	
		# c5=SurroundingRectangle(self.formulas[2][16:18],buff=0.1).set_color(YELLOW)
		# c6=SurroundingRectangle(self.formulas[2][29:34],buff=0.1).set_color(YELLOW)
		
		# # c1.rotate(PI)
		# self.play(ShowCreationThenDestruction(c1, runtime=3),ShowCreationThenDestruction(c2, runtime=3))
		# self.wait()
		# self.play(ShowCreationThenDestruction(c3, runtime=3),ShowCreationThenDestruction(c4, runtime=3))
		# self.wait()
		# self.play(ShowCreationThenDestruction(c5, runtime=3),ShowCreationThenDestruction(c6, runtime=3))
		# self.wait()

		#[3] 
		#[4] 
		self.step_formula(n_step=3,
			changes=self.set_of_changes[3-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			write=[11,5],
			)

		# self.play(
		# 			FadeOut(Int_parts),
		# 			)

		#[4] to
		#[5] 
		self.step_formula(n_step=4,
			changes=self.set_of_changes[4-1],
			pre_copy=[],
			pos_copy=[],
			fade=[3],
			write=[4,8,9,10,13,14],
			time_pre_changes=2,
			time_pos_changes=2,
			# path_arc=-PI,
			run_time=2
			)

		# [5] to [6]
		self.step_formula(n_step=5,
			changes=self.set_of_changes[5-1],
			write=[6, 7, 8],
			pre_copy=[15, 16],
			pos_copy=[4,5],
			)

		
		# #[6] [7]

		self.step_formula(n_step=6,
			changes=self.set_of_changes[6-1],
			pre_copy=[],
			pos_copy=[],
			fade=[0,6,7,8,13,14,15,17,19,9,21],
			pos_write=[3,4],
			)	

		# # [7]
		# # [8]

		self.step_formula(n_step=7,
			changes=self.set_of_changes[7-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			write=[3,4,5,6,7,8,9,15,16,17,18,19,20,21],
			)

		# R1=Brace(self.formulas[7][9:26],DOWN,buff=SMALL_BUFF).set_color(YELLOW)
		# RT1=R1.get_text('13.86').set_color(YELLOW)
		# R2=Brace(self.formulas[7][28:44],DOWN,buff=SMALL_BUFF).set_color(YELLOW)
		# RT2=R2.get_text('0.386').set_color(YELLOW)
		# R3=Brace(self.formulas[7][46:49],DOWN,buff=SMALL_BUFF).set_color(YELLOW)
		# RT3=R3.get_text('0').set_color(YELLOW)
		# self.play(GrowFromCenter(R1), FadeIn(RT1))
		# self.play(GrowFromCenter(R2), FadeIn(RT2))
		# self.play(GrowFromCenter(R3), FadeIn(RT3))
		# self.wait(2)

		# self.play(FadeOut(R1),
		# 			FadeOut(RT1),
		# 			FadeOut(R2),
		# 			FadeOut(RT2),
		# 			FadeOut(R3),
		# 			FadeOut(RT3),
		# 			)


		# # [8] 
		# # [9]

		self.step_formula(n_step=8,
			changes=self.set_of_changes[8-1],
			pre_copy=[],
			pos_copy=[],
			fade=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],
			pos_write=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],
			)
		# [9] to [10]
		self.step_formula(n_step=9,
			changes=self.set_of_changes[9-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			pos_write=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47],
			time_pre_changes=1,
			time_pos_changes=1,
			# path_arc=-PI,
			)

		# [10] to [11]
		self.step_formula(n_step=10,
			changes=self.set_of_changes[10-1],
			pre_copy=[20,21,22,23,24,25,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42],
			pos_copy=[26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48],
			fade=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,43,44,45,46,47],
			write=[25, 32, 45],
			time_pre_changes=2,
			time_pos_changes=2,
			)

		# [11] to [12]
		self.step_formula(n_step=11,
			changes=self.set_of_changes[11-1],
			pre_fade=[2,8,11,12,13,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],
			pos_write=[13,15,16,17],
			)
		# [12] to [13]
		self.step_formula(n_step=12,
			changes=self.set_of_changes[12-1],
			pre_fade=[2,3,4,5,6,7,8,9,10,11,12,13],
			pos_write=[],
			# time_pre_changes=1,
			# time_pos_changes=1,
			)


		c1=SurroundingRectangle(self.formulas[12],buff=0.2).set_color(YELLOW)
		c1.rotate(PI)
		self.play(ShowCreation(c1,runtime=3))
		self.wait(7)


		# clean
		clean= Circle(fill_opacity=5).scale(7)
		clean.set_fill(WHITE)

		# Tcircle.set_color(BLACK)
		self.play(GrowFromEdge(clean, LEFT, run_time=3))
		# self.wait() 

		Tcircle= Circle(fill_opacity=5).scale(2)
		Tcircle.set_fill()
		Tcircle.set_color(RED)
		pg1=TexMobject('Py', 'B','\\\\TV')
		pg1[0].set_color(YELLOW)
		pg1[1].set_color(BLUE)
		pg1[2].set_color(BLUE)

		pg1.next_to(Tcircle,0,buff=0).scale(2.3)

		TNXtext=TextMobject('Thanks For Watching').scale(1.5)
		TNXtext.set_color(BLACK)
		TNXtext1=TextMobject( 'Please Subscribe').scale(1.5)
		TNXtext.to_edge(UP)
		TNXtext1.to_edge(1.3*DOWN)
		TNXtext1.shift(UP)
		# TNXtext[1].to_edge(DOWN)
		TNXtext1.set_color(RED)

		self.play(Write(TNXtext))
		self.play(GrowFromCenter(Tcircle,run_time=4), Write(pg1, run_time=2))
		self.play(Write(TNXtext1))
		self.wait(5)



		# # self.write_formulas_edge()
		# #
		# # c1=SurroundingRectangle(self.formulas[14],buff=0.2)
		# # c2=SurroundingRectangle(self.formulas[14],buff=0.2)
		# # c2.rotate(PI)
		# # self.play(ShowCreationThenDestruction(c1),ShowCreationThenDestruction(c2))
		# # self.wait(2)

	def import_formulas(self):
		self.formulas=formulas


	def write_formulas(self):
		self.play(Write(self.formulas[0]))
		print(self.formulas[0])
	
	def set_changes(self):
		self.set_of_changes=[
		#1
		[[
						(0,1,2,3,4,5,6,7,8,9,10,11,12), 
						(0,1,2,3,4,5,6,7,8,9,10,11,12)
		]],
		#2
		[[
						(2,3,4,5,10,11,12,1), 
						(0,1,2,3, 5, 6, 7,4)
		]],
		#3
		[[
				(5,7,0,2,4),
				(0,3,6,8,10)
		]],
		#4
		[[
				(0,6,8,10,11,5),
				(5,0,2,15,16,12)
		]],
		#5
		[[
				(0,1,2,3,4,5,8,9,10,12,13,14,15,16),
				(0,1,2,3,9,10,13,14,15,17,18,19,20,21)
		]],
		#6
		[[
			(2,4,5,10,18,20),
			(0,1,2,5,7,6)
		]],
		#7
		[[
			(0,1,2,5,6,7,3,4),
			(0,1,2,12,13,14,10,11)
		]],
		#8
		[[
			(),
			()
		]],
		#9
		[[
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18),
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)
		]],
		#10
		[[
			(0,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42),
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)
		]],
		#11
		[[
			(0,1,4,5,6,15,17,18,19),
			(0,1,3,4,5,7,9,10,11)
		]],
		#12
		[[
			(0,1,14,15,16,17,18),
			(0,1,2,3,4,5,6)
		]],

		]

	def step_formula(self,
							pre_write=[],
							pos_write=[],
							pre_fade=[],
							pos_fade=[],
							fade=[],
							write=[],
							changes=[[]],
							path_arc=0,
							n_step=0,
							pre_copy=[],
							pos_copy=[],
							time_pre_changes=0.3,
							time_pos_changes=0.3,
							run_time=2,
							time_end=0.3,
							pre_order=["w","f"],
							pos_order=["w","f"]
							):
		formula_copy=[]
		for c in pre_copy:
			formula_copy.append(self.formulas[n_step-1][c].copy())

		for ani_ in pre_order:
			if len(pre_write)>0 and ani_=="w":
				self.play(*[Write(self.formulas[n_step-1][w])for w in pre_write])
			if len(pre_fade)>0 and ani_=="f":
				self.play(*[FadeOut(self.formulas[n_step-1][w])for w in pre_fade])

		self.wait(time_pre_changes)

		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					self.formulas[n_step-1][i],self.formulas[n_step][j],
					path_arc=path_arc
					)
				for i,j in zip(pre_ind,post_ind)
				],
				*[FadeOut(self.formulas[n_step-1][f])for f in fade if len(fade)>0],
				*[Write(self.formulas[n_step][w])for w in write if len(write)>0],
				*[ReplacementTransform(formula_copy[j],self.formulas[n_step][f])
				for j,f in zip(range(len(pos_copy)),pos_copy) if len(pre_copy)>0
				],
				run_time=run_time
			)

		self.wait(time_pos_changes)

		for ani_ in pos_order:
			if len(pos_write)>0 and ani_=="w":
				self.play(*[Write(self.formulas[n_step][w])for w in pos_write])
			if len(pos_fade)>0 and ani_=="f":
				self.play(*[FadeOut(self.formulas[n_step][w])for w in pos_fade])

		self.wait(time_end)

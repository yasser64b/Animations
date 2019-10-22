class int():
	CONFIG = {
	"y_max": 8,
	"x_max": 8,
	"y_axis_height": 5,
	"y_axis_label": "$f(x)={e^{\sqrt x} \over \sqrt x}$",
	}
	def construct(self):


	# Logo
		Tcircle= Circle(fill_opacity=5).scale(2)
		Tcircle.set_fill()
		Tcircle.set_color(RED)
		pg1=TexMobject('Py', 'B','\\\\TV')
		pg1[0].set_color(YELLOW)
		pg1[1].set_color(BLUE)
		pg1[2].set_color(BLUE)

		pg1.next_to(Tcircle,0,buff=0).scale(2.3)

		self.play(Write(Tcircle,run_time=1), Write(pg1, run_time=1))
		self.wait(0.5)
		self.play(FadeOutAndShiftDown(Tcircle), FadeOutAndShiftDown(pg1))
		self.wait()



		pg1.scale(0.4)
		# pg1.to_corner(DOWN+RIGHT)
		Tcircle2=Tcircle.scale(0.4)
		Tcircle2.to_corner(UP+RIGHT)
		pg2=pg1.next_to(Tcircle,0,buff=0)

		# self.play(Write(Tcircle2),Write(pg2))
		# self.wait()

	# # 	####

		self.show_function_graph()
	def show_function_graph(self):
		self.setup_axes(animate=False)
		def func(x):
			# return 0.1 * (x + 3-5) * (x - 3-5) * (x-5) + 5
			return np.exp(x**0.5)/(x**0.5)

		def rect(x):
			return 2.775*(x-1.5)+3.862
		recta = self.get_graph(rect,x_min=1,x_max=4)
		graph = self.get_graph(func,x_min=0.05,x_max=7)
		graph.set_color(YELLOW)
		input_tracker_p1 = ValueTracker(1)
		input_tracker_p2 = ValueTracker(4)

		def get_x_value(input_tracker):
			return input_tracker.get_value()

		def get_y_value(input_tracker):
			return graph.underlying_function(get_x_value(input_tracker))

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
		x_label_p1 = TexMobject("1")
		output_label_p1 = TexMobject("f(1)")
		x_label_p2 = TexMobject("4")
		output_label_p2 = TexMobject("f(4)")
		v_line_p1 = get_v_line(input_tracker_p1)
		v_line_p2 = get_v_line(input_tracker_p2)
		h_line_p1 = get_h_line(input_tracker_p1)
		h_line_p2 = get_h_line(input_tracker_p2)
		graph_dot_p1 = Dot(color=WHITE)
		graph_dot_p2 = Dot(color=WHITE)
				
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
		
		self.play(ShowCreation(graph), run_time=4)
		
		# Integration 
		sqrt = TexMobject("\\int_1^4 {e^{\\sqrt x} \over \\sqrt x}  dx=?").scale(1.5)
		sqrt.to_corner(UP+RIGHT)
		self.play(Write(sqrt))
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
		    1.5, graph, dx = 2,
		    df_label = None,
		    dx_label = None,
		    dx_line_color = "#942357",
		    df_line_color= "#3f7d5c",
		    secant_line_color = BLUE,
		)

	# 	self.play(FadeIn(grupo_secante), run_time=3)		




		kwargs = {
		    "x_min" : 1,
		    "x_max" : 4,
		    "fill_opacity" : 0.75,
		    "stroke_width" : 0.25,
		}
		self.graph=graph
		iteraciones=6

		self.rect_list = self.get_riemann_rectangles_list(
		    graph, iteraciones,start_color=PURPLE,end_color=ORANGE, **kwargs
		)
		flat_rects = self.get_riemann_rectangles(
		    self.get_graph(lambda x : 0), dx = 0.5,start_color=invert_color(PURPLE),end_color=invert_color(ORANGE),**kwargs)

		rects = self.rect_list[0]
		self.transform_between_riemann_rects(
		    flat_rects, rects, 
		    replace_mobject_with_target_in_scene = True,
		    run_time=6
		)
		self.wait (5)

		self.play(FadeOut(sqrt))
		# adding mani		
		picture = Group(*self.mobjects)
		picture.scale(0.6).to_corner(UP+LEFT, buff=SMALL_BUFF)
		self.play(FadeInFrom(picture,DOWN, runtime=3))
		self.wait(3)

		# Import furmulas
		self.import_formulas()
		self.write_formulas()
		self.set_changes()

		Int_title=TextMobject("Power Substitution:}")
		# Int_title.shift(2*RIGHT)
		Int_title.set_color(YELLOW)
		Int_parts=TexMobject('\\begin{cases} u=\\sqrt{x} \\\\ x=u^2 \\\\ dx=2u du \end{cases}')
		Int_parts.set_color(YELLOW)


		# [1] \int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	?
		# [2]\int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	? 		
		self.step_formula(n_step=1,
			changes=self.set_of_changes[1-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			write=[],
			time_pre_changes=0,
			time_pos_changes=2,
			# path_arc=-PI,
			# run_time=2
			)

		Int_title.next_to(formulas[0], UP, buff=2)
		Int_parts.next_to(formulas[0], RIGHT, buff=1)
		self.play(Write(Int_title), Write(Int_parts))
		self. wait(3)
		self.play(FadeOut(Int_title),FadeOut(Int_parts))
		self.wait(2)

		#[2]\int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	? 		
		#[3] \int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	\int	{	e 	^	u	\over	u	}	\times	{	2	\over	u	}	d	u

		self.step_formula(n_step=2,
			changes=self.set_of_changes[2-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			pos_write=[20,21,22,23,24,25,26,27,28,29,30,31,32,33],
			time_pre_changes=1,
			time_pos_changes=1,
			# path_arc=-PI,
			# run_time=4
			)

		Int_parts.next_to(self.formulas[2], UP, buff=1)
		Int_parts.shift(3*RIGHT)
		self.play(Write(Int_parts))
		self.wait(2)

		c1=SurroundingRectangle(self.formulas[2][5:8],buff=0.1).set_color(YELLOW)
		c2=SurroundingRectangle(self.formulas[2][23],buff=0.1).set_color(YELLOW)
	
		c3=SurroundingRectangle(self.formulas[2][11:14],buff=0.1).set_color(YELLOW)
		c4=SurroundingRectangle(self.formulas[2][25],buff=0.1).set_color(YELLOW)
	
		c5=SurroundingRectangle(self.formulas[2][16:18],buff=0.1).set_color(YELLOW)
		c6=SurroundingRectangle(self.formulas[2][29:34],buff=0.1).set_color(YELLOW)
		
		# c1.rotate(PI)
		self.play(ShowCreationThenDestruction(c1, runtime=3),ShowCreationThenDestruction(c2, runtime=3))
		self.wait()
		self.play(ShowCreationThenDestruction(c3, runtime=3),ShowCreationThenDestruction(c4, runtime=3))
		self.wait()
		self.play(ShowCreationThenDestruction(c5, runtime=3),ShowCreationThenDestruction(c6, runtime=3))
		self.wait()

		#[3] \int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	\int	{	e 	^	u	\over	u	}	\times	{	2	\over	u	}	d	u
		#[4] \int	{	e	^	{	\sqrt{	x	}	}	\over	\sqrt{	x 	}	}	d	x	=	\int	{	e 	^	u	\over	u	}	\times	{	2	\over	u	}	d	u
		self.step_formula(n_step=3,
			changes=self.set_of_changes[3-1],
			pre_copy=[],
			pos_copy=[],
			fade=[20,22,24,25,26,27,28,30,31],
			write=[21,23,25],
			)

		self.play(
					FadeOut(Int_parts),
					)





		#[4] to
		#[5] 
		self.step_formula(n_step=4,
			changes=self.set_of_changes[4-1],
			pre_copy=[],
			pos_copy=[],
			fade=[20,26,27],
			pos_write=[],
			time_pre_changes=2,
			time_pos_changes=2,
			# path_arc=-PI,
			run_time=2
			)

		# [5] to [6]
		self.step_formula(n_step=5,
			changes=self.set_of_changes[5-1],
			write=[25,26,27,28,29,30,31],
			)

		
		# #[6] [7]

		self.step_formula(n_step=6,
			changes=self.set_of_changes[6-1],
			pre_copy=[],
			pos_copy=[],
			fade=[],
			pos_write=[1,2,3,4,36,37,38,39],
			)

		# # [7]
		# # [8]

		self.step_formula(n_step=7,
			changes=self.set_of_changes[7-1],
			pre_copy=[35,39,37,25],
			pos_copy=[49,30,42,37],
			fade=[36,37,38,30,39],
			write=[34,35,36,38,39,40,41,43,44,45,48],
			time_pre_changes=2,
			time_pos_changes=2,
			# path_arc=-PI,
			run_time=2
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
			fade=[28,40,46,47,48,49,42,34],
			write=[27,28,29,30,31,32,33,35,36,37,38,39],
			time_pre_changes=1,
			time_pos_changes=1,
			# path_arc=-PI,
			run_time=2
			)

		self.step_formula(n_step=9,
			changes=self.set_of_changes[9-1],
			pre_copy=[],
			pos_copy=[],
			fade=[32],
			pos_write=[24,40],
			time_pre_changes=1,
			time_pos_changes=1,
			# path_arc=-PI,
			)
		c1=SurroundingRectangle(self.formulas[9],buff=0.2).set_color(YELLOW)
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
						(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), 
						(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)
		]],
		#2
		[[
						(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19), 
						(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)

		]],
		#3
		[[
				(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,23,32,33,29),
				(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,22,24,26,27,19)
		]],
		#4
		[[
				(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,24,22),
				(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,23,21)
		]],
		#5
		[[
				(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23),
				(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24)
		]],
		#6
		[[
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31),
			(0,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35)
		]],
		#7
		[[
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35),
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,46,47)
		]],
		#8
		[[
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,30,35,37),
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,32,34)
		]],
		#9
		[[
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39),
			(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39)
		]],
		#10
		[[
			(0,1,2,3,4,5,6,7,15),
			(0,1,2,3,4,5,6,7,9)
		]],
		#11
		[[
			(0,1,2,3,4,5),
			(0, 1, 2, 3, 4, 5)
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

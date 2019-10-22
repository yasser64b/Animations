
class Opr(Scn):
	def construct(self):
		self.add_sound("math.m4a",time_offset=0, gain=None)
		creature=SVGMobject('OmegaCreature')\
    	    .scale(0.5)
		creature[0].set_color(WHITE)
		creature[1].set_color(WHITE)
		creature[2].set_color(BLACK)
		creature[3].set_color(BLACK)
		creature[4].set_color(YELLOW)
        # self.add(creature)
		creature.to_corner(DOWN+LEFT)
		cre1=creature.copy()
		cre2=creature.copy()
		cre1.next_to(creature,RIGHT)
		cre2.next_to(cre1,RIGHT)

		self.add(creature, cre1, cre2)

		# self.wait(1)
		# # Logo
		Tcircle= Circle(fill_opacity=5).scale(2)
		Tcircle.set_fill()
		Tcircle.set_color(WHITE)
		pg1=TexMobject('Py', 'B','\\\\TV')
		pg1[0].set_color(YELLOW)
		pg1[1].set_color(BLUE)
		pg1[2].set_color(BLUE)

		pg1.next_to(Tcircle,0,buff=0).scale(2.3)

		self.play(GrowFromEdge(Tcircle,UP,run_time=4), Write(pg1, run_time=2))
		self.wait()



		pg1.scale(0.2)
		# pg1.to_corner(DOWN+RIGHT)
		Tcircle2=Tcircle.scale(0.2)
		Tcircle2.to_corner(DOWN+RIGHT)
		pg2=pg1.next_to(Tcircle,0,buff=0)

		self.play(Write(Tcircle2),Write(pg2))
		self.wait()
		
		text1=TextMobject('Do you know the answer?!').scale(1.5)
		text1.set_color(BLUE)
		text1.to_edge(UP)
		# self.play(Write(text1))
		# self.wait(2)

		self.import_formulas()
		self.write_formulas()
		self.set_changes()
		self.step_formula(n_step=1,
			changes=self.set_of_changes[0],
			pos_order=["w"],
			time_pre_changes=3
			)
		self.wait(1)
		self.play(Write(text1))
		self.wait(4)
		self.play(FadeOutAndShiftDown(text1))

		text1=TextMobject('The order of operations:').scale(1.5)
		text1.set_color(BLUE)
		text1.to_edge(UP)

		self.play(Write(text1))
		
		self.step_formula(n_step=1,
			changes=self.set_of_changes[1],
			fade=[0, 2,	4,	6,	8,	9],
			write=[2,3,	4,	5, 6, 8,10],
			)

		c1=Brace(self.formulas[1][:4], DOWN, buff = SMALL_BUFF)
		t1=TextMobject('1st').next_to(c1,0.1*DOWN, buff=0.5)

		c2=Brace(self.formulas[1][4:7], DOWN, buff = 0.4)
		t2=TextMobject('2nd').next_to(c2,0.1*DOWN, buff=0.5)

		c3=Brace(self.formulas[1][7:9],DOWN, buff = 0.4)
		t3=TextMobject('3rd').next_to(c3,0.1*DOWN, buff=0.5)

		c4=Brace(self.formulas[1][9:],DOWN, buff = 0.4)
		t4=TextMobject('4th').next_to(c4,0.1*DOWN, buff=0.5)
		
		self.play(GrowFromEdge(c1, UP), Write(t1))
		self.wait(3)
		self.play(GrowFromEdge(c2,UP), Write(t2))
		self.wait(3)
		self.play(GrowFromEdge(c3,UP), Write(t3))
		self.wait(3)
		self.play(GrowFromEdge(c4,UP), Write(t4))
		self.wait(3)

		text3=TextMobject('Same priority').set_color(YELLOW)
		text3.to_corner(LEFT+DOWN)
		text3.shift(UP)
		text4=TextMobject('Operate from left to right').set_color(YELLOW)
		text4.to_corner(RIGHT+DOWN)
		text4.shift(UP)
		arrow1=Arrow(text3.get_right(),text4.get_left()).set_color(BLUE)
		text5=TexMobject('e.g.,  1+3-2=2').set_color(RED)
		text5.next_to(arrow1,DOWN, buff=0.2)

		self.play(Write(text3), GrowFromEdge(arrow1,LEFT), Write(text4))
		self.wait(3)
		self.play(Write(text5))
		self.wait(5)

		#clean the page 
		clean= Circle(fill_opacity=5).scale(10)	
		clean.set_fill(BLACK)
		self.play(GrowFromCenter(clean, run_time=3))
		self.wait()
		self.add(Tcircle2,pg2)
		# self.wait()
		self.add(creature, cre1, cre2)

		text6=TextMobject("Let's solve it through math order of operations rules").scale(1.1)
		text6.to_edge(UP)
		self.play(Write(text6))
		self.wait(1)

		#10/2(2+3)=??
		self.step_formula(n_step=2,
			changes=self.set_of_changes[0],
			write=[0,1,2,3,4,5,6,7,8,9],
			)
		self.wait(6)

		brace1=Brace(self.formulas[1][7:9],DOWN, buff = SMALL_BUFF)
		thttps://github.com/yasser64b/Animationsex5=TexMobject('5').scale(2)
		tex5.next_to(brace1,DOWN, buff=0.1)
		self.play(GrowFromCenter(brace1), Write(tex5))
		self.wait(2)
		self.play(FadeOut(tex5), FadeOut(brace1))

		#10/2x5=??
		self.step_formula(n_step=3,
			changes=self.set_of_changes[2],
			pos_order=["w"],
			fade=[3,4,5,6,7],
			write=[3,4]
			)
		self.wait(3)

		text7=TextMobject("Same precedence!  ", "left to right").scale(1.1)
		text7[1].set_color(YELLOW)
		text7.to_edge(UP)
		self.play(ReplacementTransform(text6,text7))
		self.wait(2)

		brace2=Brace(self.formulas[2][:3],DOWN, buff = SMALL_BUFF)
		tex5.next_to(brace2,DOWN, buff=0.1)
		self.play(GrowFromCenter(brace2), Write(tex5))
		self.wait(2)
		self.play(FadeOut(tex5), FadeOut(brace2))

		#5x5=??
		self.step_formula(n_step=4,
			changes=self.set_of_changes[3],
			fade=[0,1,2],
			write=[0]
			)
		self.wait(3)
		#5x5=25
		self.step_formula(n_step=5,
			changes=self.set_of_changes[4],
			fade=[4],
			write=[4]
			)
		self.wait(3)
		
		#10/2(2+3)=25
		self.step_formula(n_step=6,
			changes=self.set_of_changes[5],
			fade=[0,1,2],
			write=[0,1,2,3,4,5,6,7]
			)
		self.wait(3)


		text8=TextMobject("Is this answer correct??!!").set_color(YELLOW)
		text8.scale(1.5)
		text8.to_edge(UP)
		self.play(ReplacementTransform(text7, text8))
		# self.wait(4)
		# Surprising sign

		creature1=SVGMobject('OmegaCreature_suprised')\
    	    .scale(1)
		creature1[0].set_color(WHITE)
		creature1[1].set_color(WHITE)
		creature1[2].set_color(BLACK)
		creature1[3].set_color(BLACK)
		creature1[4].set_color(BLUE)
        # self.add(creature)
		creature1.to_edge(DOWN, buff=0.5)
		# creature.shift(UP)
		# self.play(Write(creature1))
		

		creature4=SVGMobject('Bubbles_thought').scale(0.5)   
		creature4.next_to(creature1, UP,buff=0.1)
		creature4.shift(RIGHT)

		quesText=TextMobject('?').scale(1.4)
		quesText.set_color(RED)
		quesText.next_to(creature4,0, buff=0)

		self.play(GrowFromCenter(creature1),GrowFromCenter(creature4), Write(quesText))
		self.wait(1)


		cross = Cross(self.formulas[6])
		cross.set_stroke(YELLOW, 6)
		self.play(ShowCreation(cross))
		self.wait(2)		

		text9=TextMobject("What did go wrong??").set_color(YELLOW)
		text9.scale(1.5)
		text9.to_edge(UP)
		self.play(ReplacementTransform(text8, text9))
		self.wait(4)


		text10=TextMobject("Let's try another procedure:")
		text10.scale(1.5)
		text10.to_edge(UP)
		self.play(ReplacementTransform(text9, text10))
		self.wait(2)
		
		self.play(FadeOut(cross), FadeOut(creature1), FadeOut(creature4), FadeOut(quesText))
		self.wait(3)

		# 10/2(2+3)=??
		self.step_formula(n_step=7,
			changes=self.set_of_changes[6],
			fade=[1],
			write=[1]
			)
		self.wait(3)

		# frac 10/2(2+3)=??

		self.step_formula(n_step=8,
			changes=self.set_of_changes[7],
			fade=[1],
			write=[0,2,9]
			)
		self.wait(3)

		# frac 10/2(5)=??
		self.step_formula(n_step=9,
			changes=self.set_of_changes[8],
			fade=[5,6,7],
			write=[5]
			)
		self.wait(3)

		# frac 10/10=??
		self.step_formula(n_step=10,
			changes=self.set_of_changes[9],
			fade=[3,4,5,6],
			write=[3]
			)
		self.wait(3)

		# frac 10/10=1
		self.step_formula(n_step=11,
			changes=self.set_of_changes[10],
			fade=[6],
			write=[6]
			)
		self.wait(3)

		text11=TextMobject("Correct answer:",)
		text11.scale(1.5)
		text11.set_color(GREEN)
		text11.to_edge(UP)

		creature3=SVGMobject('OmegaCreature_Happy').scale(2)   
		# creature3=SVGMobject('Check').scale(2)   
		creature3.to_edge(RIGHT)
		creature3[4].set_color(GREEN)
		creature3[2].set_color(BLUE)
		creature3[3].set_color(BLUE)
        # self.add(creature3)

		self.play(ReplacementTransform(text10, text11),GrowFromCenter((creature3)))
		self.wait(8)
 
		# Finish

		clean= Circle(fill_opacity=5).scale(10)
		clean.set_fill(BLACK)
		# Tcircle.set_color(BLACK)
		self.play(GrowFromEdge(clean, LEFT, run_time=3))
		self.wait() 
		 		
		Tcircle= Circle(fill_opacity=5).scale(2)
		Tcircle.set_fill()
		Tcircle.set_color(WHITE)
		pg1=TexMobject('Py', 'B','\\\\TV')
		pg1[0].set_color(YELLOW)
		pg1[1].set_color(BLUE)
		pg1[2].set_color(BLUE)

		pg1.next_to(Tcircle,0,buff=0).scale(2.3)

		TNXtext=TextMobject('Thanks For Watching').scale(1.5)
		TNXtext.to_edge(UP)
		self.play(Write(TNXtext))
		self.play(GrowFromEdge(Tcircle,UP,run_time=4), Write(pg1, run_time=2))
		self.wait(5)

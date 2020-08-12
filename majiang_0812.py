import copy
import time
import os
import sys
import random

class player:
	list_t = [];list_w = [];list_b= []; list_hope_pai = [];
	yipeng = 0; yipeng_score = 0; nenpeng = []; hope_score = 0; have_peng = []
	one_xiang_ting = [];xia_jiao = 0; list_ding = []; nengang = []; have_gang = []
	score = 0; ding = 't'; value = 100; mo = 0; da = 0
	dui = 0; name = ""
	def __init__(self):
		self.list_t=[];self.list_w=[];self.list_b=[];self.list_hope_pai=[];self.nenpeng=[]
		self.have_peng=[];self.one_xiang_ting = [];self.list_ding= [];self.nengang = []; self.have_gang = []
	def sort_pai(self):
		self.list_t.sort(); self.list_w.sort(); self.list_b.sort()
	def show(self):
		#return
		print(self.name,self.list_t,"t",self.list_w,"w",self.list_b,"b")
		print("score:",self.score, "mo:", self.mo, "ding:",self.ding,"da:",self.da,"  nengpeng:",self.nenpeng,"  have_peng", self.have_peng,
				"nengang:",self.nengang,"have_gang:",self.have_gang)

	def mopai(self,pai):
		self.mo = pai
		self.da = 0
		if pai < 10:
			self.list_t.append(pai)
		elif pai < 20:
			self.list_w.append(pai-10)
		elif pai < 30:
			self.list_b.append(pai-20)
		self.sort_pai()
		self.score=self.caculate_score()

	def dapai_spec(self,pai):
		if pai < 10:
			self.list_t.remove(pai)
		elif pai < 20:
			self.list_w.remove(pai-10)
		elif pai < 30:
			self.list_b.remove(pai-20)
		self.da=pai
		return pai

	def remove_spec(self,pai):
		if pai < 10:
			self.list_t.remove(pai)
		elif pai < 20:
			self.list_w.remove(pai-10)
		elif pai < 30:
			self.list_b.remove(pai-20)
		return pai

	def guzhang2(self):
		if self.ding == 't':

			if self.list_w.count(1) == 1 and self.list_w.count(2) == 0 and self.list_w.count(3) == 1 and self.list_w.count(4) != 0:
				return 11
			if self.list_w.count(9) == 1 and self.list_w.count(8) == 0 and self.list_w.count(7) == 1 and self.list_w.count(6) != 0:
				return 19
			if self.list_b.count(1) == 1 and self.list_b.count(2) == 0 and self.list_b.count(3) == 1 and self.list_b.count(4) != 0:
				return 21
			if self.list_b.count(9) == 1 and self.list_b.count(8) == 0 and self.list_b.count(7) == 1 and self.list_b.count(6) != 0:
				return 29
		if self.ding == 'w':
			if self.list_t.count(1) == 1 and self.list_t.count(2) == 0 and self.list_t.count(3) == 1 and self.list_t.count(4) != 0:
				return 1
			if self.list_t.count(9) == 1 and self.list_t.count(8) == 0 and self.list_t.count(7) == 1 and self.list_t.count(6) != 0:
				return 9
			if self.list_b.count(1) == 1 and self.list_b.count(2) == 0 and self.list_b.count(3) == 1 and self.list_b.count(4) != 0:
				return 21
			if self.list_b.count(9) == 1 and self.list_b.count(8) == 0 and self.list_b.count(7) == 1 and self.list_b.count(6) != 0:
				return 29
		if self.ding == 'b':
			if self.list_w.count(1) == 1 and self.list_w.count(2) == 0 and self.list_w.count(3) == 1 and self.list_w.count(4) != 0:
				return 11
			if self.list_w.count(9) == 1 and self.list_w.count(8) == 0 and self.list_w.count(7) == 1 and self.list_w.count(6) != 0:
				return 19
			if self.list_t.count(1) == 1 and self.list_t.count(2) == 0 and self.list_t.count(3) == 1 and self.list_t.count(4) != 0:
				return 1
			if self.list_t.count(9) == 1 and self.list_t.count(8) == 0 and self.list_t.count(7) == 1 and self.list_t.count(6) != 0:
				return 9
		return 0

	def t_duoque_b_guzhang(self):
		if self.list_w.count(1) == 1 and self.list_w.count(2) == 0 and self.list_w.count(3) == 0:
			return 11
		if self.list_w.count(9) == 1 and self.list_w.count(8) == 0 and self.list_w.count(7) == 0:
			return 19
		if self.list_w.count(1) == 0 and self.list_w.count(2) == 1 and self.list_w.count(3) == 0 and self.list_w.count(4) == 0:
			return 12
		if self.list_w.count(9) == 0 and self.list_w.count(8) == 1 and self.list_w.count(7) == 0 and self.list_w.count(6) == 0:
			return 18
		return 0
	def t_duoque_w_guzhang(self):
		if self.list_b.count(1) == 1 and self.list_b.count(2) == 0 and self.list_b.count(3) == 0:
			return 21
		if self.list_b.count(9) == 1 and self.list_b.count(8) == 0 and self.list_b.count(7) == 0:
			return 29
		if self.list_b.count(1) == 0 and self.list_b.count(2) == 1 and self.list_b.count(3) == 0 and self.list_b.count(4) == 0:
			return 22
		if self.list_b.count(9) == 0 and self.list_b.count(8) == 1 and self.list_b.count(7) == 0 and self.list_b.count(6) == 0:
			return 28
		return 0

	def w_duoque_t_guzhang(self):
		if self.list_b.count(1) == 1 and self.list_b.count(2) == 0 and self.list_b.count(3) == 0:
			return 21
		if self.list_b.count(9) == 1 and self.list_b.count(8) == 0 and self.list_b.count(7) == 0:
			return 29
		if self.list_b.count(1) == 0 and self.list_b.count(2) == 1 and self.list_b.count(3) == 0 and self.list_b.count(4) == 0:
			return 22
		if self.list_b.count(9) == 0 and self.list_b.count(8) == 1 and self.list_b.count(7) == 0 and self.list_b.count(6) == 0:
			return 28
		return 0
	def w_duoque_b_guzhang(self):
		if self.list_t.count(1) == 1 and self.list_t.count(2) == 0 and self.list_t.count(3) == 0:
			return 1
		if self.list_t.count(9) == 1 and self.list_t.count(8) == 0 and self.list_t.count(7) == 0:
			return 9
		if self.list_t.count(1) == 0 and self.list_t.count(2) == 1 and self.list_t.count(3) == 0 and self.list_t.count(4) == 0:
			return 2
		if self.list_t.count(9) == 0 and self.list_t.count(8) == 1 and self.list_t.count(7) == 0 and self.list_t.count(6) == 0:
			return 8
		return 0

	def b_duoque_t_guzhang(self):
		if self.list_w.count(1) == 1 and self.list_w.count(2) == 0 and self.list_w.count(3) == 0:
			return 11
		if self.list_w.count(9) == 1 and self.list_w.count(8) == 0 and self.list_w.count(7) == 0:
			return 19
		if self.list_w.count(1) == 0 and self.list_w.count(2) == 1 and self.list_w.count(3) == 0 and self.list_w.count(4) == 0:
			return 12
		if self.list_w.count(9) == 0 and self.list_w.count(8) == 1 and self.list_w.count(7) == 0 and self.list_w.count(6) == 0:
			return 18
		return 0

	def b_duoque_w_guzhang(self):
		if self.list_t.count(1) == 1 and self.list_t.count(2) == 0 and self.list_t.count(3) == 0:
				return 1
		if self.list_t.count(9) == 1 and self.list_t.count(8) == 0 and self.list_t.count(7) == 0:
			return 9
		if self.list_t.count(1) == 0 and self.list_t.count(2) == 1 and self.list_t.count(3) == 0 and self.list_t.count(4) == 0:
			return 2
		if self.list_t.count(9) == 0 and self.list_t.count(8) == 1 and self.list_t.count(7) == 0 and self.list_t.count(6) == 0:
			return 8
		return 0

	def guzhang(self):
		if self.ding == 't':
			if self.list_ding.count('b') >= 2:
				pai = self.t_duoque_b_guzhang()
				if pai == 0:
					return self.t_duoque_w_guzhang()
				return pai

			if self.list_ding.count('w') >= 2:
				pai = self.t_duoque_w_guzhang()
				if pai == 0:
					return self.t_duoque_b_guzhang()
				return pai
		if self.ding == 'w':
			if self.list_ding.count('t') >= 2:
				pai = self.w_duoque_t_guzhang()
				if pai == 0:
					return self.w_duoque_b_guzhang()
				return pai

			if self.list_ding.count('b') >= 2:
				pai = self.w_duoque_b_guzhang()
				if pai == 0:
					return self.w_duoque_t_guzhang()
				return pai
			
		if self.ding == 'b':
			if self.list_ding.count('t') >= 2:
				pai = self.b_duoque_t_guzhang()
				if pai == 0:
					return self.b_duoque_w_guzhang()
				return pai

			if self.list_ding.count('w') >= 2:
				pai = self.b_duoque_w_guzhang()
				if pai == 0:
					return self.b_duoque_t_guzhang()
				return pai
		return 0

	def if_nengmo(self,pai):
		if pai < 10:
			if self.list_t.count(pai) == 4:
				return 0
		elif pai < 20:
			if self.list_w.count(pai-10) == 4:
				return 0
		else:
			if self.list_b.count(pai-20) == 4:
				return 0
		return 1

	def dapai(self):
		if self.ding == 't' and len(self.list_t) > 0:
			self.da = self.list_t.pop()
		elif self.ding == 'w' and len(self.list_w) > 0:
			self.da = self.list_w.pop()+10
		elif self.ding == 'b' and len(self.list_b) > 0:
			self.da = self.list_b.pop()+20
		else:
			gupai = self.guzhang()
			if gupai > 0:
				self.da = self.dapai_spec(gupai)
			elif self.score >= 8 and self.score < 11 and len(self.nenpeng) < 4:
				best_pai,max_score,max_score_pai_num = self.think(2)
				if best_pai == 0:
#					gupai = self.guzhang2()
#					if gupai > 0:
#						best_pai = gupai
#					else:
					best_pai,max_score,max_score_pai_num = self.think(1)
				self.da = self.dapai_spec(best_pai)
			else:
				best_pai,max_score,max_score_pai_num = self.think(1)
				if max_score >=14:
					self.xia_jiao = 1
				self.da = self.dapai_spec(best_pai)
		self.score=self.caculate_score()
		return self.da

	def peng(self,pai):
		index = 0
		if self.nenpeng.count(pai) > 0:
			self.nenpeng.remove(pai)
			self.have_peng.append(pai)
			self.remove_spec(pai)
			self.remove_spec(pai)
			self.caculate_score()
			if len(self.nenpeng) > 0:	
				return pai
			elif self.xia_jiao == 0:
				best_pai,max_score,max_score_pai_num = self.think(1)
				if max_score >= 14:
					return pai
				else:
					self.nenpeng.append(pai)
					self.have_peng.remove(pai)
					self.mopai(pai)
					self.mopai(pai)
					return 0
		return 0

	def zi_gang(self,pai):
		self.have_gang.append(pai)
		self.remove_spec(pai)
		self.remove_spec(pai)
		self.remove_spec(pai)
		self.remove_spec(pai)
	def dian_gang(self,pai):
		if self.nengang.count(pai) > 0:
			self.nengang.remove(pai)
			self.have_gang.append(pai)
			self.remove_spec(pai)
			self.remove_spec(pai)
			self.remove_spec(pai)
			return pai
		else:
			return 0

	def think(self,level):
		max_score_pai = 0;max_score_pai_num = 0; tmp_pai = 0;max_score = 0; tmp_score = 0;
		the_best_pai = 0; tmp_player = None; tmp_best_pai = 0; tmp_max_score = 0; one_xiang_ting = []
		one_xiang_best_pai =0; one_xiang_max_num = 0; last_think_pai = 100; last_think_score = 0
		one_xiang_total_num = 0;one_xiang_max_total_num = 0
		self.list_hope_pai.clear()
		if self.ding == 't':
			for i in range(0, len(self.list_w)):
				last_think_score = self.score
				if last_think_pai == self.list_w[i] + 10:
					continue
				tmp_pai = self.dapai_spec(self.list_w[i] + 10)
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0
				for j in range(11, 30):
					if j == 20:
						continue
					if self.if_nengmo(j):
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
							one_xiang_total_num = one_xiang_total_num + max_score_pai_num
					else:
						if tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
					self.dapai_spec(j)
				self.mopai(tmp_pai)
#				if len(self.list_hope_pai) == 0:
#					continue
				if level > 1:
					print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting)
					if len(one_xiang_ting) > one_xiang_max_num:
						one_xiang_max_num = len(one_xiang_ting)
						the_best_pai = tmp_pai
						one_xiang_max_total_num = one_xiang_total_num
					elif len(one_xiang_ting) == one_xiang_max_num:
						if one_xiang_total_num > one_xiang_max_total_num:
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif one_xiang_total_num == one_xiang_max_total_num and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					elif len(self.list_hope_pai) == max_score_pai_num and max_score_pai_num !=0:
						if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
							the_best_pai = tmp_pai

					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()
			for i in range(0, len(self.list_b)):
				last_think_score = self.score
				if last_think_pai == self.list_b[i] + 20:
					continue
				tmp_pai = self.dapai_spec(self.list_b[i] + 20)
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0
				for j in range(11, 30):
					if j == 20:
						continue
					if self.if_nengmo(j):
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
							one_xiang_total_num = one_xiang_total_num + max_score_pai_num

					else:
						if tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
					self.dapai_spec(j)
				self.mopai(tmp_pai)
#				if len(self.list_hope_pai) == 0:
#					continue
				if level > 1:
					print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting)
					if len(one_xiang_ting) > one_xiang_max_num:
						one_xiang_max_num = len(one_xiang_ting)
						the_best_pai = tmp_pai
						one_xiang_max_total_num = one_xiang_total_num
					elif len(one_xiang_ting) == one_xiang_max_num:
						if one_xiang_total_num > one_xiang_max_total_num:
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif one_xiang_total_num == one_xiang_max_total_num and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					elif len(self.list_hope_pai) == max_score_pai_num and max_score_pai_num !=0:
						if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
							the_best_pai = tmp_pai
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()

		if self.ding == 'w':
			for i in range(0, len(self.list_t)):
				last_think_score = self.score
				if last_think_pai == self.list_t[i]:
					continue
				tmp_pai = self.dapai_spec(self.list_t[i])
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0
				for j in range(1, 30):
					if j > 9 and j < 21:
						continue
					if self.if_nengmo(j):
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
							one_xiang_total_num = one_xiang_total_num + max_score_pai_num
					else:
						if tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
					self.dapai_spec(j)
				self.mopai(tmp_pai)
#				if len(self.list_hope_pai) == 0:
#					continue
				if level > 1:
					print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting)
					if len(one_xiang_ting) > one_xiang_max_num:
						one_xiang_max_num = len(one_xiang_ting)
						the_best_pai = tmp_pai
						one_xiang_max_total_num = one_xiang_total_num
					elif len(one_xiang_ting) == one_xiang_max_num:
						if one_xiang_total_num > one_xiang_max_total_num:
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif one_xiang_total_num == one_xiang_max_total_num and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					elif len(self.list_hope_pai) == max_score_pai_num and max_score_pai_num !=0:
						if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
							the_best_pai = tmp_pai
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()
			for i in range(0, len(self.list_b)):
				last_think_score = self.score
				if last_think_pai == self.list_b[i] + 20:
					continue
				tmp_pai = self.dapai_spec(self.list_b[i] + 20)
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0

				for j in range(1, 30):
					if j > 9 and j < 21:
						continue
					if self.if_nengmo(j):
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
							one_xiang_total_num = one_xiang_total_num + max_score_pai_num
					else:
						if tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
					self.dapai_spec(j)
				self.mopai(tmp_pai)
#				if len(self.list_hope_pai) == 0:
#					continue
				if level > 1:
					print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting)
					if len(one_xiang_ting) > one_xiang_max_num:
						one_xiang_max_num = len(one_xiang_ting)
						the_best_pai = tmp_pai
						one_xiang_max_total_num = one_xiang_total_num
					elif len(one_xiang_ting) == one_xiang_max_num:
						if one_xiang_total_num > one_xiang_max_total_num:
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif one_xiang_total_num == one_xiang_max_total_num and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					elif len(self.list_hope_pai) == max_score_pai_num and max_score_pai_num !=0:
						if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
							the_best_pai = tmp_pai
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()

		if self.ding == 'b':
			for i in range(0, len(self.list_t)):
				last_think_score = self.score
				if last_think_pai == self.list_t[i]:
					continue
				tmp_pai = self.dapai_spec(self.list_t[i])
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0
				for j in range(1, 20):
					if j == 10:
						continue
					if self.if_nengmo(j):
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
							one_xiang_total_num = one_xiang_total_num + max_score_pai_num
					else:
						if tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
					self.dapai_spec(j)
				self.mopai(tmp_pai)
#				if len(self.list_hope_pai) == 0:
#					continue
				if level > 1:
					print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting)
					if len(one_xiang_ting) > one_xiang_max_num:
						one_xiang_max_num = len(one_xiang_ting)
						the_best_pai = tmp_pai
						one_xiang_max_total_num = one_xiang_total_num
					elif len(one_xiang_ting) == one_xiang_max_num:
						if one_xiang_total_num > one_xiang_max_total_num:
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif one_xiang_total_num == one_xiang_max_total_num and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					elif len(self.list_hope_pai) == max_score_pai_num and max_score_pai_num !=0:
						if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
							the_best_pai = tmp_pai
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()
			for i in range(0, len(self.list_w)):
				last_think_score = self.score
				if last_think_pai == self.list_w[i] + 10:
					continue
				tmp_pai = self.dapai_spec(self.list_w[i] + 10)
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0
				for j in range(1, 20):
					if j == 10:
						continue
					if self.if_nengmo(j):
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
							one_xiang_total_num = one_xiang_total_num + max_score_pai_num
					else:
						if tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
					self.dapai_spec(j)
				self.mopai(tmp_pai)
#				if len(self.list_hope_pai) == 0:
#					continue
				if level > 1:
					print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting)
					if len(one_xiang_ting) > one_xiang_max_num:
						one_xiang_max_num = len(one_xiang_ting)
						the_best_pai = tmp_pai
						one_xiang_max_total_num = one_xiang_total_num
					elif len(one_xiang_ting) == one_xiang_max_num:
						if one_xiang_total_num > one_xiang_max_total_num:
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif one_xiang_total_num == one_xiang_max_total_num and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					elif len(self.list_hope_pai) == max_score_pai_num and max_score_pai_num !=0:
						if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
							the_best_pai = tmp_pai
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()
		return the_best_pai,max_score,max_score_pai_num


	def group_shunzi(self, list_y):
		list_x = copy.copy(list_y)
		total1 = 0;
		if len(list_x) < 3:
			return 0
		total = 0
		i = 0
		while i < len(list_y):
			if list_y.count(list_y[i]) >= 3:
				list_x.remove(list_y[i])
				list_x.remove(list_y[i])
				list_x.remove(list_y[i])
				total = total + 1
				if list_y.count(list_y[i])==3:
					i = i+3
				else:
					i = i+4
			else:
				i = i + 1

		while len(list_x)>2:
			
			index = 0;index2 = 0;
			try:
				index = list_x.index(list_x[0] + 1)
			except Exception:
				list_x.pop(0)
				continue
			try:
				index2 = list_x.index(list_x[0] + 2)
			except Exception:
				list_x.pop(0)
				continue
			else:
				list_x.pop(index2);list_x.pop(index);list_x.pop(0)
				total = total +1
		total1 = self.group_shunzi_deep(copy.copy(list_y))
		if total1 > total:
			return total1
		else:
			return total
	def group_shunzi_deep(self,list_x):
		total = 0;
		i = 0
		while len(list_x)>2:
			
			index = 0;index2 = 0;
			try:
				index = list_x.index(list_x[0] + 1)
			except Exception:
				list_x.pop(0)
				continue
			try:
				index2 = list_x.index(list_x[0] + 2)
			except Exception:
				list_x.pop(0)
				continue
			else:
				list_x.pop(index2);list_x.pop(index);list_x.pop(0)
				total = total +1
		return total


	def ding_sure(self):
		len_t = len(self.list_t)
		len_w = len(self.list_w)
		len_b = len(self.list_b)
		if len_t <= len_w and len_t <= len_b and self.cal_dui2(self.list_t) == 0 and self.group_shunzi(self.list_t) == 0:
			self.ding = 't'
		elif len_w <= len_t and len_w <= len_b and self.cal_dui2(self.list_w) == 0 and self.group_shunzi(self.list_w) == 0:
			self.ding = 'w'
		elif len_b <= len_t and len_b <= len_w and self.cal_dui2(self.list_b) == 0 and self.group_shunzi(self.list_b) == 0:
			self.ding = 'b'
		elif len_t <= len_w and len_t <= len_b:
			self.ding = 't'
		elif len_w <= len_t and len_w <= len_b:
			self.ding = 'w'
		elif len_b <= len_t and len_b <= len_w:
			self.ding = 'b'

	#def think(self):
		

	def caculate_score(self):
		score = 0;
		if self.ding == 't':
			nodui_score = self.group_shunzi(self.list_w)*3 + self.group_shunzi(self.list_b)*3
			num_nen_peng = self.find_nen_peng(nodui_score)
			nodui_score = nodui_score + len(self.have_peng)*3 + len(self.have_gang)*3
			if num_nen_peng > 0:
				score = nodui_score + num_nen_peng + 1   #计算分数
			else:
				score = nodui_score
		if self.ding == 'w':
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_b)*3
			num_nen_peng = self.find_nen_peng(nodui_score)
			nodui_score = nodui_score + len(self.have_peng)*3 + len(self.have_gang)*3
			if num_nen_peng > 0:
				score = nodui_score + num_nen_peng + 1   #计算分数
			else:
				score = nodui_score
		if self.ding == 'b':
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_w)*3
			num_nen_peng = self.find_nen_peng(nodui_score)
			nodui_score = nodui_score + len(self.have_peng)*3 + len(self.have_gang)*3
			if num_nen_peng > 0:
				score = nodui_score + num_nen_peng + 1   #计算分数
			else:
				score = nodui_score
		self.score = score
		return score

	def find_nen_gang(self):
		self.nengang.clear()
		gang_pai = 0;
		tmp_player = copy.deepcopy(self)
		i = 0;
		if tmp_player.ding == 't':
			while i < len(tmp_player.list_w) - 1:
				if tmp_player.list_w.count(self.list_w[i]) == 3:
					data = tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);tmp_player.list_w.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(self.list_w[i] + 10)
					tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data)
					i = i + 3
				elif tmp_player.list_w.count(self.list_w[i]) == 4:
					data = tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = self.list_w[i] + 10
					tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data)
					i = i + 4
				else:
					i = i + 1
			i = 0;

			while i < len(tmp_player.list_b) - 1:
				if tmp_player.list_b.count(self.list_b[i]) == 3:
					data = tmp_player.list_b.pop(i);tmp_player.list_b.pop(i);tmp_player.list_b.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(self.list_b[i] + 20)
					tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data)
					i = i + 3
				elif tmp_player.list_b.count(self.list_b[i]) == 4:
					data = tmp_player.list_b.pop(i);tmp_player.list_b.pop(i);tmp_player.list_b.pop(i);tmp_player.list_b.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = self.list_b[i] + 20
					tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data)
					i = i + 4
				else:
					i = i + 1
		elif tmp_player.ding == 'w':
			while i < len(tmp_player.list_t) - 1:
				if tmp_player.list_t.count(self.list_t[i]) == 3:
					data = tmp_player.list_t.pop(i);tmp_player.list_t.pop(i);tmp_player.list_t.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(self.list_t[i])
					tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data)
					i = i + 3
				elif tmp_player.list_t.count(self.list_t[i]) == 4:
					data = tmp_player.list_t.pop(i);tmp_player.list_t.pop(i);tmp_player.list_t.pop(i);tmp_player.list_t.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = self.list_t[i]
					tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data)
					
					i = i + 4
				else:
					i = i + 1
			i = 0;

			while i < len(tmp_player.list_b) - 1:
				if tmp_player.list_b.count(self.list_b[i]) == 3:
					data = tmp_player.list_b.pop(i);tmp_player.list_b.pop(i);tmp_player.list_b.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(self.list_b[i] + 20)
					tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data)
					i = i + 3
				elif tmp_player.list_b.count(self.list_b[i]) == 4:
					data = tmp_player.list_b.pop(i);tmp_player.list_b.pop(i);tmp_player.list_b.pop(i);tmp_player.list_b.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = self.list_b[i] + 20
					tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data);tmp_player.list_b.insert(i,data)
					
					i = i + 4
				else:
					i = i + 1
		else:
			while i < len(tmp_player.list_w) - 1:
				if tmp_player.list_w.count(self.list_w[i]) == 3:
					data = tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);tmp_player.list_w.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(self.list_w[i] + 10)
					tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data)
					i = i + 3
				elif tmp_player.list_w.count(self.list_w[i]) == 4:
					data = tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);tmp_player.list_w.pop(i);tmp_player.list_w.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = self.list_w[i] + 10
					tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data);tmp_player.list_w.insert(i,data)
					
					i = i + 4
				else:
					i = i + 1
			i = 0;

			while i < len(tmp_player.list_t) - 1:
				if tmp_player.list_t.count(self.list_t[i]) == 3:
					data = tmp_player.list_t.pop(i);tmp_player.list_t.pop(i);tmp_player.list_t.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(self.list_t[i])
					tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data)
					i = i + 3
				elif tmp_player.list_t.count(self.list_t[i]) == 4:
					data = tmp_player.list_t.pop(i);tmp_player.list_t.pop(i);tmp_player.list_t.pop(i);tmp_player.list_t.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = self.list_t[i]
					tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data);tmp_player.list_t.insert(i,data)
					
					i = i + 4
				else:
					i = i + 1
		return gang_pai



	def find_nen_peng(self,nodui_score):
		self.nenpeng.clear()
		score = 0;
		nenpeng_num = 0;
		tmp_score = 0
		if self.ding == 't':
			num_dui = self.cal_dui(self.list_w,self.list_b)
#			nodui_score = self.group_shunzi(self.list_w)*3 + self.group_shunzi(self.list_b)*3
			if num_dui > 0:
				list_tmp_w = self.list_w; list_tmp_b = self.list_b
				i = 0;
				while i < len(list_tmp_w)-1:
					if list_tmp_w[i] == list_tmp_w[i+1]:
						data = list_tmp_w.pop(i);list_tmp_w.pop(i)
						tmp_score = self.group_shunzi(list_tmp_w)*3+self.group_shunzi(list_tmp_b)*3
						if tmp_score == nodui_score:
							self.nenpeng.append(data+10)
							nenpeng_num = nenpeng_num + 1
						list_tmp_w.insert(i, data);list_tmp_w.insert(i, data);
						i = i+1
					i=i+1
				i = 0
				while i < len(list_tmp_b)-1:
					if list_tmp_b[i] == list_tmp_b[i+1]:
						data = list_tmp_b.pop(i);list_tmp_b.pop(i)
						tmp_score = self.group_shunzi(list_tmp_w)*3 + self.group_shunzi(list_tmp_b)*3
						if tmp_score == nodui_score:
							self.nenpeng.append(data+20)
							nenpeng_num = nenpeng_num + 1
						list_tmp_b.insert(i, data); list_tmp_b.insert(i,data);
						i = i+1
					i=i+1
				return nenpeng_num
			else:
				return 0;

		if self.ding == 'w':
			num_dui = self.cal_dui(self.list_t,self.list_b)
#			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_b)*3
			if num_dui > 0:
				list_tmp_t = self.list_t; list_tmp_b = self.list_b
				i = 0;
				while i < len(list_tmp_t)-1:
					if list_tmp_t[i] == list_tmp_t[i+1]:
						data = list_tmp_t.pop(i);list_tmp_t.pop(i)
						tmp_score = self.group_shunzi(list_tmp_t)*3+self.group_shunzi(list_tmp_b)*3
						if tmp_score == nodui_score:
							self.nenpeng.append(data)
							nenpeng_num = nenpeng_num + 1
						list_tmp_t.insert(i, data);list_tmp_t.insert(i, data);
						i = i+1
					i=i+1
				i = 0
				while i < len(list_tmp_b)-1:
					if list_tmp_b[i] == list_tmp_b[i+1]:
						data = list_tmp_b.pop(i);list_tmp_b.pop(i)
						tmp_score = self.group_shunzi(list_tmp_t)*3 + self.group_shunzi(list_tmp_b)*3
						if tmp_score == nodui_score:
							self.nenpeng.append(data+20)
							nenpeng_num = nenpeng_num + 1
						list_tmp_b.insert(i, data); list_tmp_b.insert(i,data);
						i = i+1
					i=i+1
				return nenpeng_num
			else:
				return 0;
		
		if self.ding == 'b':
			num_dui = self.cal_dui(self.list_t,self.list_w)
#			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_w)*3
			if num_dui > 0:
				list_tmp_t = self.list_t; list_tmp_w = self.list_w
				i = 0;
				while i < len(list_tmp_t)-1:
					if list_tmp_t[i] == list_tmp_t[i+1]:
						data = list_tmp_t.pop(i);list_tmp_t.pop(i)
						tmp_score = self.group_shunzi(list_tmp_t)*3+self.group_shunzi(list_tmp_w)*3
						if tmp_score == nodui_score:
							self.nenpeng.append(data)
							nenpeng_num = nenpeng_num + 1
						list_tmp_t.insert(i, data);list_tmp_t.insert(i, data);
						i = i+1
					i=i+1
				i = 0
				while i < len(list_tmp_w)-1:
					if list_tmp_w[i] == list_tmp_w[i+1]:
						data = list_tmp_w.pop(i);list_tmp_w.pop(i)
						tmp_score = self.group_shunzi(list_tmp_t)*3 + self.group_shunzi(list_tmp_w)*3
						if tmp_score == nodui_score:
							self.nenpeng.append(data+10)
							nenpeng_num = nenpeng_num + 1
						list_tmp_w.insert(i, data); list_tmp_w.insert(i,data);
						i = i+1
					i=i+1
				return nenpeng_num
			else:
				return 0;
	

	def cal_dui(self, list_x, list_y):
		num_dui = 0;i=0
		while i<len(list_x) -1:
			if list_x[i] == list_x[i+1]:
				num_dui = num_dui + 1
				i = i + 1
			i = i + 1 
		i=0
		while i<len(list_y) -1:
			if list_y[i] == list_y[i+1]:
				num_dui = num_dui + 1
				i = i + 1
			i = i + 1
		return num_dui

	def cal_dui2(self, list_x):
		num_dui = 0;i=0
		while i<len(list_x) -1:
			if list_x[i] == list_x[i+1]:
				num_dui = num_dui + 1
				i = i + 1
			i = i + 1 
		return num_dui

	def pai_value(self,pai):
		if pai < 10:
			if pai > 5:
				return 10 - pai
			else:
				return pai
		elif pai < 20:
			if pai > 15:
				return 20 - pai
			else:
				return pai - 10
		else:
			if pai > 25:
				return 30 - pai
			else:
				return pai - 20

class desk:
	list_tuple = []; list_river = []
	def show(self):
		return
		print("tuple: ",self.list_tuple)
		print("river: ",self.list_river)
	def __init__(self):
		self.list_tuple = []; self.list_river = []

def test_spec():
	p1 = player();
	p1.name = 'pa'
	p1.list_t=[3,5,6,7,7,8,8,9]
	p1.list_w=[8,8,9,9,9]
	p1.ding='b'
	p1.mopai(9)
	
	p1.dapai()
	p1.show()

	p2 = player();
	p2.name = 'p2'
	p2.list_t = [1,1,3,4,4,6,7,9]
	p2.list_w = [5,6,7,7,8,9]
	p2.ding='b'
	p2.caculate_score()
	p2.show()
	p2.dapai()
	p2.show()
	print("################################")




test_spec()


play_times = 100;
hu_user1 = 0;
hu_user2 = 0
hu_user3 = 0
hu_user4 = 0
no_user_hu = 0
err_start =0

ticks1 = time.time()
desk1 = desk()
list_tmp_tuple = []
total_hu = []
for x in range(0, 100):

	p1 = player()
	p1.name = "p1"
	p2 = player()
	p2.name = "p2"
	p3 = player()
	p3.name = "p3"
	p4 = player()
	p4.name = "p4"
	list_player = [p1,p2,p3,p4]
	list_tmp_tuple.clear()
	desk1.list_tuple.clear()
	desk1.list_river.clear()
	for i in range(0,27):
		for j in range(0,4):
			if i<9:
				list_tmp_tuple.append(i+1)
			elif i<18:
				list_tmp_tuple.append(i+2)
			elif i<27:
				list_tmp_tuple.append(i+3)


	while len(list_tmp_tuple)>0:
		index = random.randint(0,len(list_tmp_tuple)-1)
		desk1.list_tuple.append(list_tmp_tuple.pop(index))
	if len(desk1.list_tuple) != 108:
		err_start = err_start + 1
		continue
	print(len(desk1.list_tuple))
	for i in range(1,10):
		print(desk1.list_tuple.count(i))
	for i in range(11,20):
		print(desk1.list_tuple.count(i))
	for i in range(21,30):
		print(desk1.list_tuple.count(i))
	print("\n\n")

	for i in range(0,13):
		for j in range(0,4):
			list_player[j].mopai(desk1.list_tuple.pop())

	for i in range(0,4):
		list_player[i].ding_sure()
		for j in range(0, 4):
			list_player[j].list_ding.append(list_player[i].ding)





	index = 0
	count_player = 4
	while len(desk1.list_tuple)>0 and len(list_player) > 0:

		list_player[index].mopai(desk1.list_tuple.pop())
		list_player[index].show()
		if list_player[index].score >= 14:
			print(list_player[index].name," hu le ####################################")
			list_player.pop(index)
			count_player = count_player -1
			index = index - 1
		else:
			#str = input("\n")
			pai = list_player[index].find_nen_gang()
			if pai > 0:
				list_player[index].zi_gang(pai)
				index = index - 1
			else:
				go_out = 0
				while 1 == 1:
					pai = list_player[index].dapai()
					list_player[index].find_nen_gang()
					desk1.list_river.append(pai)
					list_player[index].show()
					desk1.show()
					if len(list_player) > 1:
						total_hu.clear()
						for i in range(0,count_player):
							if index == i:
								continue
							list_player[i].mopai(pai)
							if list_player[i].score >= 14:
								print("pai:",pai,"dian pao le #############################",list_player[i].name)
								list_player[i].show()
								total_hu.append(i)
								
							list_player[i].dapai_spec(pai)
							list_player[i].caculate_score()
						while len(total_hu) > 0:
							total_hu.sort()
							index_tmp = total_hu.pop()
							list_player.pop(index_tmp)
							count_player = count_player -1
							index = index_tmp - 1
							go_out = 1
					
					if go_out == 1:
						break
					go_out = 1
					if len(list_player) > 1:
						for i in range(0, count_player):
							if index == i:
								continue
							if pai == list_player[i].dian_gang(pai):
								print("pai:",pai,"bei gang le **************************",list_player[i].name)
								list_player[i].show()
								go_out = 1
								index = i - 1
								break
							if pai == list_player[i].peng(pai):
								print("pai:",pai,"bei peng le **************************",list_player[i].name)
								list_player[i].show()
								index = i	
								go_out = 0
								break
					if go_out == 1:
						break

		index = index +1
		if index >= count_player:
			index = 0
		#str = input("\n")

	if len(list_player) == 0:
		hu_user4 = hu_user4 + 1
	elif len(list_player) == 1:
		hu_user3 = hu_user3 + 1
	elif len(list_player) == 2:
		hu_user2 = hu_user2 + 1
	elif len(list_player) == 3:
		hu_user1 = hu_user1 + 1
	elif len(list_player) == 4:
		no_user_hu = no_user_hu + 1

ticks2 = time.time()
print("play_times:",play_times,"no_user_hu:",no_user_hu,"hu_user1:",hu_user1,"hu_user2:",
	hu_user2,"hu_user3:",hu_user3,"hu_user4:",hu_user4,"use_time:",ticks2-ticks1,"err_start:",err_start)
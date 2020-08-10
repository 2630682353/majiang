import copy
import time
import os
import sys
import random

class player:
	list_t = [];list_w = [];list_b= []; list_hope_pai = [];
	yipeng = 0; yipeng_score = 0; nenpeng = []; hope_score = 0; have_peng = []
	one_xiang_ting = []
	score = 0; ding = 't'; value = 100; mo = 0; da = 0
	dui = 0; name = ""
	def __init__(self):
		self.list_t=[];self.list_w=[];self.list_b=[];self.list_hope_pai=[];self.nenpeng=[]
		self.have_peng=[];one_xiang_ting = []
	def sort_pai(self):
		self.list_t.sort(); self.list_w.sort(); self.list_b.sort()
	def show(self):
		#return
		print(self.name,self.list_t,"t",self.list_w,"w",self.list_b,"b")
		print("score:",self.score, "mo:", self.mo, "ding:",self.ding,"da:",self.da,"  nengpeng:",self.nenpeng,"  have_peng", self.have_peng)

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
		self.find_nen_peng()
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
	def guzhang(self):
		if self.ding == 't':
			if self.list_w.count(1) == 1 and self.list_w.count(2) == 0 and self.list_w.count(3) == 0:
				return 11
			if self.list_w.count(9) == 1 and self.list_w.count(8) == 0 and self.list_w.count(7) == 0:
				return 19
			if self.list_b.count(1) == 1 and self.list_b.count(2) == 0 and self.list_b.count(3) == 0:
				return 21
			if self.list_b.count(9) == 1 and self.list_b.count(8) == 0 and self.list_b.count(7) == 0:
				return 29

			if self.list_w.count(1) == 0 and self.list_w.count(2) == 1 and self.list_w.count(3) == 0 and self.list_w.count(4) == 0:
				return 12
			if self.list_w.count(9) == 0 and self.list_w.count(8) == 1 and self.list_w.count(7) == 0 and self.list_w.count(6) == 0:
				return 18
			if self.list_b.count(1) == 0 and self.list_b.count(2) == 1 and self.list_b.count(3) == 0 and self.list_b.count(4) == 0:
				return 22
			if self.list_b.count(9) == 0 and self.list_b.count(8) == 1 and self.list_b.count(7) == 0 and self.list_b.count(6) == 0:
				return 28

		if self.ding == 'w':
			if self.list_t.count(1) == 1 and self.list_t.count(2) == 0 and self.list_t.count(3) == 0:
				return 1
			if self.list_t.count(9) == 1 and self.list_t.count(8) == 0 and self.list_t.count(7) == 0:
				return 9
			if self.list_b.count(1) == 1 and self.list_b.count(2) == 0 and self.list_b.count(3) == 0:
				return 21
			if self.list_b.count(9) == 1 and self.list_b.count(8) == 0 and self.list_b.count(7) == 0:
				return 29

			if self.list_t.count(1) == 0 and self.list_t.count(2) == 1 and self.list_t.count(3) == 0 and self.list_t.count(4) == 0:
				return 2
			if self.list_t.count(9) == 0 and self.list_t.count(8) == 1 and self.list_t.count(7) == 0 and self.list_t.count(6) == 0:
				return 8
			if self.list_b.count(1) == 0 and self.list_b.count(2) == 1 and self.list_b.count(3) == 0 and self.list_b.count(4) == 0:
				return 22
			if self.list_b.count(9) == 0 and self.list_b.count(8) == 1 and self.list_b.count(7) == 0 and self.list_b.count(6) == 0:
				return 28

		if self.ding == 'b':
			if self.list_w.count(1) == 1 and self.list_w.count(2) == 0 and self.list_w.count(3) == 0:
				return 11
			if self.list_w.count(9) == 1 and self.list_w.count(8) == 0 and self.list_w.count(7) == 0:
				return 19
			if self.list_t.count(1) == 1 and self.list_t.count(2) == 0 and self.list_t.count(3) == 0:
				return 1
			if self.list_t.count(9) == 1 and self.list_t.count(8) == 0 and self.list_t.count(7) == 0:
				return 9

			if self.list_w.count(1) == 0 and self.list_w.count(2) == 1 and self.list_w.count(3) == 0 and self.list_w.count(4) == 0:
				return 12
			if self.list_w.count(9) == 0 and self.list_w.count(8) == 1 and self.list_w.count(7) == 0 and self.list_w.count(6) == 0:
				return 18
			if self.list_t.count(1) == 0 and self.list_t.count(2) == 1 and self.list_t.count(3) == 0 and self.list_t.count(4) == 0:
				return 2
			if self.list_t.count(9) == 0 and self.list_t.count(8) == 1 and self.list_t.count(7) == 0 and self.list_t.count(6) == 0:
				return 8

		return 0

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
				best_pai,max_score = self.think(2)
				if best_pai == 0:
					gupai = self.guzhang2()
					if gupai > 0:
						best_pai = gupai
					else:
						best_pai,max_score = self.think(1)
				self.da = self.dapai_spec(best_pai)
			else:
				best_pai,max_score = self.think(1)
				self.da = self.dapai_spec(best_pai)
		self.score=self.caculate_score()
		self.find_nen_peng()
		return self.da

	def peng(self,pai):
		index = 0
		if len(self.nenpeng) > 1:
			if self.nenpeng.count(pai) > 0:
				self.nenpeng.remove(pai)
				self.have_peng.append(pai)
				self.remove_spec(pai)
				self.remove_spec(pai)
				self.caculate_score()
				return pai
		return 0

			



	def think(self,level):
		max_score_pai = 0;max_score_pai_num = 0; tmp_pai = 0;max_score = 0; tmp_score = 0;
		the_best_pai = 0; tmp_player = None; tmp_best_pai = 0; tmp_max_score = 0; one_xiang_ting = []
		one_xiang_best_pai =0; one_xiang_max_num = 0; last_think_pai = 100; last_think_score = 0
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
				for j in range(11, 30):
					if j == 20:
						continue
					self.mopai(j)
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
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
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
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
				for j in range(11, 30):
					if j == 20:
						continue
					self.mopai(j)
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)

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
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
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
				for j in range(1, 30):
					if j > 9 and j < 21:
						continue
					self.mopai(j)
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
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
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
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

				for j in range(1, 30):
					if j > 9 and j < 21:
						continue
					self.mopai(j)
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
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
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
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
				for j in range(1, 20):
					if j == 10:
						continue
					self.mopai(j)
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
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
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
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
				for j in range(1, 20):
					if j == 10:
						continue
					self.mopai(j)
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score = tmp_player.think(1)
						if tmp_max_score >= 14:
							one_xiang_ting.append(j)
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
				else:
					if len(self.list_hope_pai) > max_score_pai_num:
						max_score_pai_num = len(self.list_hope_pai)
						the_best_pai = max_score_pai
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()
		return the_best_pai,max_score


	def group_shunzi(self, list_y):
		list_x = copy.copy(list_y)
		if len(list_x) < 3:
			return 0
		total = 0
		while len(list_x)>2:
			if list_x[0] == list_x[1] and list_x[1] == list_x[2]:
				list_x.pop(0); list_x.pop(0); list_x.pop(0)
				total = total +1
			else:
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
			nodui_score = self.group_shunzi(self.list_w)*3 + self.group_shunzi(self.list_b)*3+ len(self.have_peng)*3
			num_nen_peng = self.find_nen_peng()
			if num_nen_peng > 0:
				score = nodui_score + num_nen_peng + 1   #计算分数
			else:
				score = nodui_score
		if self.ding == 'w':
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_b)*3+ len(self.have_peng)*3
			num_nen_peng = self.find_nen_peng()
			if num_nen_peng > 0:
				score = nodui_score + num_nen_peng + 1   #计算分数
			else:
				score = nodui_score
		if self.ding == 'b':
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_w)*3+ len(self.have_peng)*3
			num_nen_peng = self.find_nen_peng()
			if num_nen_peng > 0:
				score = nodui_score + num_nen_peng + 1   #计算分数
			else:
				score = nodui_score
		self.score = score
		return score

	def find_nen_peng(self):
		self.nenpeng.clear()
		score = 0;
		nenpeng_num = 0;
		nodui_score = 0;
		tmp_score = 0
		if self.ding == 't':
			num_dui = self.cal_dui(self.list_w,self.list_b)
			nodui_score = self.group_shunzi(self.list_w)*3 + self.group_shunzi(self.list_b)*3
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
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_b)*3
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
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_w)*3
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

class desk:
	list_tuple = []; list_river = []
	def show(self):
		return
		print("tuple: ",self.list_tuple)
		print("river: ",self.list_river)

def test_spec():
	p1 = player();
	p1.name = 'pa'
	p1.list_t=[2,3,7,8,9]
	p1.list_w=[1,1,3,3,4,6,7,8,9]
	p1.ding='b'
	p1.caculate_score()
	p1.show()
	p1.dapai()
	p1.show()

	p2 = player();
	p2.name = 'p2'
	p2.list_t = [1,3,4,6,6,7,9,9]
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

ticks1 = time.time()

for x in range(0, 100):

	p1 = player()
	p1.name = "p1"
	p2 = player()
	p2.name = "p2"
	p3 = player()
	p3.name = "p3"
	p4 = player()
	p4.name = "p4"
	desk1 = desk()
	list_player = [p1,p2,p3,p4]

	list_tmp_tuple = []
	for i in range(0,27):
		for j in range(0,4):
			if i<9:
				list_tmp_tuple.append(i+1)
			elif i<18:
				list_tmp_tuple.append(i+1-9+10)
			elif i<27:
				list_tmp_tuple.append(i+1-18+20)

	while len(list_tmp_tuple)>0:
		index = random.randint(0,len(list_tmp_tuple)-1)
		desk1.list_tuple.append(list_tmp_tuple.pop(index))
	print(desk1.list_tuple)
	print("\n\n")


	for i in range(0,13):
		for j in range(0,4):
			list_player[j].mopai(desk1.list_tuple.pop())

	for i in range(0,4):
		list_player[i].ding_sure()


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
			go_out = 0
			while 1 == 1:
				pai = list_player[index].dapai()
				desk1.list_river.append(pai)
				list_player[index].show()
				desk1.show()
				if len(list_player) > 1:
					for i in range(0,count_player):
						if index == i:
							continue
						list_player[i].mopai(pai)
						if list_player[i].score >= 14:
							print("pai:",pai,"dian pao le #############################",list_player[i].name)
							list_player[i].show()
							list_player.pop(i)
							count_player = count_player -1
							index = i - 1
							go_out = 1
							break
						list_player[i].dapai_spec(pai)
				
				if go_out == 1:
					break
				go_out = 1
				if len(list_player) > 1:
					for i in range(0, count_player):
						if index == i:
							continue
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
	hu_user2,"hu_user3:",hu_user3,"hu_user4:",hu_user4,"use_time:",ticks2-ticks1)
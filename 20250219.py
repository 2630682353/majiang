import copy
import time
import os
import sys
import random

class desk:
	list_tuple = []; list_river = []
	list_ding = []; list_player = []
	phase = 1;list_total_player = []
	def show(self):
		return
		print("tuple: ",self.list_tuple)
		print("river: ",self.list_river)
	def __init__(self):
		self.list_tuple = []; self.list_river = []
		self.list_ding = []; self.list_player = []
		self.phase = 1;self.list_total_player = []
		
def item_to_spec(list_val, type):
	if (type == 't'):
		return list_val
	elif (type == 'w'):
		return list_val + 10
	elif (type == 'b'):
		return list_val + 20


class player:
	list_t = [];list_w = [];list_b= []; list_hope_pai = []; secend_list_hope_pai = []; list_river = [];
	yipeng = 0; yipeng_score = 0; nenpeng = [];left_pai_peng = []; hope_score = 0; have_peng = []
	one_xiang_ting = [];xia_jiao = 0; list_ding = []; nengang = []; have_gang = []
	score = 0; ding = 't'; value = 100; mo = 0; da = 0;user_desk = desk();max_score_pai_num = 0
	dui = 0; name = "";hu_pai_left_num = 0;list_dui = [];win_score = 100; money = 1000; human = 0;
	def __init__(self):
		self.list_t=[];self.list_w=[];self.list_b=[];self.list_hope_pai=[];self.secend_list_hope_pai = []; self.nenpeng=[]
		self.have_peng=[];self.one_xiang_ting = [];self.list_ding= [];self.nengang = []; self.have_gang = []
		self.list_dui = [];self.left_pai_peng = []; self.list_river = [];
	def sort_pai(self):
		self.list_t.sort(); self.list_w.sort(); self.list_b.sort()
	def show(self):
		#return
		print(self.name,self.list_t,"t",self.list_w,"w",self.list_b,"b","ding_list:",self.list_ding)
		print("score:",self.score, "mo:", self.mo, "ding:",self.ding,"da:",self.da,"  nengpeng:",self.nenpeng,"  have_peng", self.have_peng,
				"nengang:",self.nengang,"have_gang:",self.have_gang,"hu_left_num:",self.hu_pai_left_num)

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

	def havepai(self,pai):
		if pai < 10:
			return self.list_t.count(pai)
		elif pai < 20:
			return self.list_w.count(pai-10)
		elif pai < 30:
			return self.list_b.count(pai-20)
		else:
			return 0

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

	def guzhang_smart(self):
		list_guzhang = []
		for pai in self.list_t:
			if pai>=3 and pai<=7 or self.list_ding.count('t') > 1:
				continue
			if self.list_t.count(pai) == 1 and self.list_t.count(pai-1) == 0 and self.list_t.count(pai-2) == 0 and \
			self.list_t.count(pai+1) == 0 and self.list_t.count(pai+2) == 0:
				list_guzhang.append(pai)

		for pai in self.list_w:
			if pai>=3 and pai<=7 or self.list_ding.count('w') > 1:
				continue
			if self.list_w.count(pai) == 1 and self.list_w.count(pai-1) == 0 and self.list_w.count(pai-2) == 0 and \
			self.list_w.count(pai+1) == 0 and self.list_w.count(pai+2) == 0:
				list_guzhang.append(pai+10)
		
		for pai in self.list_b:
			if pai>=3 and pai<=7 or self.list_ding.count('b') > 1:
				continue
			if self.list_b.count(pai) == 1 and self.list_b.count(pai-1) == 0 and self.list_b.count(pai-2) == 0 and \
			self.list_b.count(pai+1) == 0 and self.list_b.count(pai+2) == 0:
				list_guzhang.append(pai+20)
		return list_guzhang
	
	def check_special_model(self):
		if self.list_t.count(1) == 1 and self.list_t.count(2) == 1 and self.list_t.count(3) == 0 and self.cant_see_left(3) == 0:
			if self.cant_see_left(2) <= 1:
				return 2
			else:
				return 1
		if self.list_w.count(1) == 1 and self.list_w.count(2) == 1 and self.list_w.count(3) == 0 and self.cant_see_left(13) == 0:
			if self.cant_see_left(12) <= 1:
				return 12
			else:
				return 11
		if self.list_b.count(1) == 1 and self.list_b.count(2) == 1 and self.list_b.count(3) == 0 and self.cant_see_left(23) == 0:
			if self.cant_see_left(22) <= 1:
				return 22
			else:
				return 21
		if self.list_t.count(9) == 1 and self.list_t.count(8) == 1 and self.list_t.count(7) == 0 and self.cant_see_left(7) == 0:
			if self.cant_see_left(8) <= 1:
				return 8
			else:
				return 9
		if self.list_w.count(9) == 1 and self.list_w.count(8) == 1 and self.list_w.count(7) == 0 and self.cant_see_left(17) == 0:
			if self.cant_see_left(18) <= 1:
				return 18
			else:
				return 19
		if self.list_b.count(9) == 1 and self.list_b.count(8) == 1 and self.list_b.count(7) == 0 and self.cant_see_left(27) == 0:
			if self.cant_see_left(28) <= 1:
				return 28
			else:
				return 29
		return 0
	def if_nengmo(self,pai):
		if pai < 10:
			if self.cant_see_left(pai):
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
			gupai_list = self.guzhang_smart()
			da_gupai = 0; gupai_value = 100;
			if len(gupai_list) > 0:
				for gupai in gupai_list:
					self.pai_value(gupai) < gupai_value
					da_gupai = gupai; gupai_value = self.pai_value(gupai)
				self.da = self.dapai_spec(da_gupai)
		
			elif self.score >= 8 and self.score < 11 and len(self.nenpeng) < 4 or self.xia_jiao == 0 and self.score >= 11:
				best_pai,max_score,max_score_pai_num = self.think(2)
				if best_pai == 0:
#					gupai = self.guzhang2()
#					if gupai > 0:
#						best_pai = gupai
#					else:
					best_pai,max_score,max_score_pai_num = self.think(1)
				self.da = self.dapai_spec(best_pai)
				self.xia_jiao = self.check_xiajiao()
			else:
				best_pai,max_score,max_score_pai_num = self.think(1)
				if max_score >=14:
					self.xia_jiao = 1
					self.max_score_pai_num = max_score_pai_num
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
				elif len(self.guzhang_smart()) > 0:
					return pai
				else:
#					self.nenpeng.append(pai)
#					self.have_peng.remove(pai)
#					self.mopai(pai)
#					self.mopai(pai)
#					return 0
					return pai
			elif self.xia_jiao == 1:
				hu_pai_left_num = self.hu_pai_left_num
				best_pai,max_score,max_score_pai_num = self.think(1)
				if max_score >= 14:
					if self.list_ding.count(self.ding)>=3 and self.hu_pai_left_num > hu_pai_left_num + 0.8:
						print("before_hu_left_num:", hu_pai_left_num, " after_hu_left_num:", self.hu_pai_left_num)
						return pai
					elif self.hu_pai_left_num > hu_pai_left_num + 1.2:
						print("before_hu_left_num:", hu_pai_left_num, " after_hu_left_num:", self.hu_pai_left_num)
						return pai
					else:
						self.nenpeng.append(pai)
						self.have_peng.remove(pai)
						self.mopai(pai)
						self.mopai(pai)
						return 0
				else:
					self.nenpeng.append(pai)
					self.have_peng.remove(pai)
					self.mopai(pai)
					self.mopai(pai)
					return 0
		elif self.list_dui.count(pai) > 0:
			tmp_score = self.score
			self.have_peng.append(pai)
			self.remove_spec(pai)
			self.remove_spec(pai)
			self.caculate_score()
			if self.xia_jiao == 1:
				hu_pai_left_num = self.hu_pai_left_num
				best_pai,max_score,max_score_pai_num = self.think(1)
				if max_score >= 14:
					if self.list_ding.count(self.ding)>=3 and self.hu_pai_left_num > hu_pai_left_num + 0.8:
						return pai
					elif self.hu_pai_left_num > hu_pai_left_num + 1.2:
						return pai
					else:
						self.have_peng.remove(pai)
						self.mopai(pai)
						self.mopai(pai)
						return 0
				else:
					self.have_peng.remove(pai)
					self.mopai(pai)
					self.mopai(pai)
					return 0

			elif self.xia_jiao == 0:
				best_pai,max_score,max_score_pai_num = self.think(1)
				if max_score >= 14:
					return pai
				else:
					self.caculate_score()
					if self.score > tmp_score and self.user_desk.phase == 1 and tmp_score < 11:
						return pai
					elif self.score > tmp_score + 1 and self.user_desk.phase == 2:
						return pai
					else:
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

	def check_xiajiao(self):
		tmp_player = copy.deepcopy(self)
		max_score = 0
		if tmp_player.ding == 't':
			for j in range(11, 30):
				if j == 20:
					continue
				if self.cant_see_left(j) > 0:
					tmp_player.mopai(j)
					if tmp_player.score > max_score:
						max_score = tmp_player.score;
					tmp_player.dapai_spec(j)
		elif tmp_player.ding == 'w':
			for j in range(1, 30):
				if j > 9 and j < 21:
					continue
				if self.cant_see_left(j) > 0:
					tmp_player.mopai(j)
					if tmp_player.score > max_score:
						max_score = tmp_player.score;
					tmp_player.dapai_spec(j)
		elif tmp_player.ding == 'b':
			for j in range(1, 20):
				if j == 10:
					continue
				if self.cant_see_left(j) > 0:
					tmp_player.mopai(j)
					if tmp_player.score > max_score:
						max_score = tmp_player.score;
					tmp_player.dapai_spec(j)
		del tmp_player
		if max_score >= 14:
			return 1
		else:
			return 0

	def think(self,level):
		max_score_pai = 0;max_score_pai_num = 0; tmp_pai = 0;max_score = 0; tmp_score = 0; tmp_max_score = 0;
		the_best_pai = 0; tmp_player = None; tmp_best_pai = 0; tmp_max_score = 0; one_xiang_ting = []
		one_xiang_best_pai =0; one_xiang_max_num = 0; last_think_pai = 100; last_think_score = 0
		one_xiang_total_num = 0;one_xiang_max_total_num = 0; secend_max_score_pai_num = 0; tmp_secend_max_score_pai_num = 0;
		secend_max_score_pai = 0; tmp_secend_max_score_pai = 0; send_max_score = 0; tmp_secend_max_score = 0;
		think_total_info = {}; tmp_pai_info = \
		{'max_score':0, 'secend_max_score':0, 'list_max_hope_pai':[], 'list_secend_hope_pai':[], 'max_score_num':0, 'send_score_num':0};
		self.list_hope_pai.clear()
		self.hu_pai_left_num = 0
		cal_list1 = []; cal_list2 = [];
		list1_type = 'n'; list2_type = 'n';
		if self.ding == 't':
			cal_list1 = self.list_w; cal_list2 = self.list_b;
			list1_type = 'w'; list2_type = 'b'
		elif (self.ding == 'w'):
			cal_list1 = self.list_t; cal_list2 = self.list_b;
			list1_type = 't'; list2_type = 'b'
		elif (self.ding == 'b'):
			cal_list1 = self.list_t; cal_list2 = self.list_w;
			list1_type = 't'; list2_type = 'w'
		step_min = 1; step_max = 30;
		for x in range(0, 2):
			if x == 1:
				cal_list1 = cal_list2; list1_type = list2_type
			for i in range(0, len(cal_list1)):
				last_think_score = self.score
				if last_think_pai == item_to_spec(cal_list1[i], list1_type):
					continue
				tmp_pai = self.dapai_spec(item_to_spec(cal_list1[i], list1_type))
				tmp_score = 0; max_score = 0; secend_max_score = 0; 
	
				last_think_pai = tmp_pai
				tmp_score = self.caculate_score()
				if last_think_score > tmp_score + 1 and last_think_score < 13:
					self.mopai(tmp_pai)
					continue
				one_xiang_ting.clear()
				one_xiang_total_num = 0
				for j in range(step_min, step_max):
					if (j < 11 or j == 20) and self.ding == 't':
						continue
					elif j > 9 and j < 21 and self.ding == 'w':
						continue
					elif (j == 10 or j > 19) and self.ding == 'b':
						continue
					
					if self.cant_see_left(j) > 0:
						self.mopai(j)
					else:
						continue
					tmp_score = self.caculate_score()
					if level > 1:
						tmp_player = copy.deepcopy(self)
						tmp_best_pai,tmp_max_score,max_score_pai_num = tmp_player.think(1)
						del tmp_player
						if tmp_max_score >= 14:
							if self.list_ding.count(self.ding)>=3 and max_score_pai_num > 0.9:
								one_xiang_ting.append(j)
								one_xiang_total_num = one_xiang_total_num + max_score_pai_num
							elif max_score_pai_num >= 1.4:
								one_xiang_ting.append(j)
								one_xiang_total_num = one_xiang_total_num + max_score_pai_num
					else:
						
						if tmp_score > max_score:
							tmp_pai_info['max_score'] = tmp_score; tmp_pai_info['secend_max_score'] = max_score;
	
							secend_max_score = max_score;
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							tmp_pai_info['list_secend_hope_pai'].clear()
							tmp_pai_info['list_secend_hope_pai'].extend(tmp_pai_info['list_max_hope_pai'])
							tmp_pai_info['list_max_hope_pai'].clear()
							tmp_pai_info['list_max_hope_pai'].append(j);
							think_total_info[tmp_pai]=copy.deepcopy(tmp_pai_info)
							
						elif tmp_score == max_score:
							#if tmp_pai in think_total_info:
							think_total_info[tmp_pai]['list_max_hope_pai'].append(j)
							
						elif tmp_score == secend_max_score:
							think_total_info[tmp_pai]['list_secend_hope_pai'].append(j)
						'''
						if last_think_score <= 8 and tmp_score < 11 and tmp_score > 8:
							if max_score < 10:
								self.list_hope_pai.clear()
								max_score_pai_num = 0
							self.list_hope_pai.append(j)
							max_score_pai = tmp_pai
							max_score = 10
	
						elif tmp_score > max_score:
							max_score = tmp_score; max_score_pai = tmp_pai;max_score_pai_num = 0
							self.list_hope_pai.clear()
							self.list_hope_pai.append(j)
						elif tmp_score == max_score:
							self.list_hope_pai.append(j);max_score_pai = tmp_pai
						'''
					self.dapai_spec(j)
				self.mopai(tmp_pai)
	#				if len(self.list_hope_pai) == 0:
	#					continue
				if level > 1:
					
					if len(one_xiang_ting) > 0:
						tmp_one_xiang_max_num = self.list_cant_see_left(one_xiang_ting)
						print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai,"one_xiang_ting",one_xiang_ting,
							"tmp_one_xiang_max_num:",tmp_one_xiang_max_num,"one_xiang_total_num:",one_xiang_total_num)
						if tmp_one_xiang_max_num > one_xiang_max_num + 0.5:
							one_xiang_max_num = tmp_one_xiang_max_num
							the_best_pai = tmp_pai
							one_xiang_max_total_num = one_xiang_total_num
						elif tmp_one_xiang_max_num >= one_xiang_max_num - 0.5 and tmp_one_xiang_max_num <= one_xiang_max_num + 0.5:
							if one_xiang_total_num > one_xiang_max_total_num + 1.5:
								the_best_pai = tmp_pai
								one_xiang_max_total_num = one_xiang_total_num
						elif tmp_one_xiang_max_num >= one_xiang_max_num - 0.1 and tmp_one_xiang_max_num <= one_xiang_max_num + 0.1 and \
						one_xiang_total_num >= one_xiang_max_total_num - 0.1 and one_xiang_total_num <= one_xiang_max_total_num + 0.1 and one_xiang_max_num != 0:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
				else:
					'''
					if len(self.list_hope_pai) > 0:
						tmp_max_score_pai_num = self.list_cant_see_left(self.list_hope_pai)
	
						if tmp_max_score_pai_num > max_score_pai_num + 0.1 and max_score >= tmp_max_score:
							tmp_max_score = max_score
							max_score_pai_num = tmp_max_score_pai_num
							the_best_pai = tmp_pai
							if max_score >= 14:
								self.hu_pai_left_num = max_score_pai_num
						elif tmp_max_score_pai_num >= max_score_pai_num - 0.1 and tmp_max_score_pai_num <= max_score_pai_num + 0.1 and max_score_pai_num !=0 and max_score >= tmp_max_score:
							if self.pai_value(tmp_pai) < self.pai_value(the_best_pai):
								the_best_pai = tmp_pai
					if the_best_pai == 0:
						the_best_pai = max_score_pai
						max_score_pai_num = 0
					#print("da:",tmp_pai,"max_score:",max_score,"list_hope_pai",self.list_hope_pai)
					self.list_hope_pai.clear()
					'''
		if level == 1:
			tmp_total_info = {}; max_score = 0; max_score_pai_num = 0;

			for key in think_total_info:
				if think_total_info[key]['max_score'] > max_score:
					tmp_total_info.clear();
					tmp_total_info[key]= think_total_info[key];
					max_score = think_total_info[key]['max_score']
				elif think_total_info[key]['max_score'] == max_score:
					tmp_total_info[key]= think_total_info[key];
			for key in tmp_total_info:
				tmp_total_info[key]['max_score_num'] = self.list_cant_see_left(tmp_total_info[key]['list_max_hope_pai'])
				if tmp_total_info[key]['max_score_num'] > max_score_pai_num + 0.1:
					max_score_pai_num = tmp_total_info[key]['max_score_num']
					secend_max_score = tmp_total_info[key]['secend_max_score']
					secend_max_score_pai_num = self.list_cant_see_left(tmp_total_info[key]['list_secend_hope_pai'])
					the_best_pai = key
					if max_score >= 14:
						self.hu_pai_left_num = max_score_pai_num
				elif tmp_total_info[key]['max_score_num'] >= max_score_pai_num - 0.1 and \
				tmp_total_info[key]['max_score_num'] <= max_score_pai_num + 0.1 and max_score_pai_num !=0 and max_score < 14:
					if tmp_total_info[key]['secend_max_score'] > secend_max_score:
						the_best_pai = key; 
					elif tmp_total_info[key]['secend_max_score'] == secend_max_score:
						tmp_secend_max_score_pai_num = self.list_cant_see_left(tmp_total_info[key]['list_secend_hope_pai'])
						if tmp_secend_max_score_pai_num > secend_max_score_pai_num + 0.1:
							the_best_pai = key;

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
		del list_x
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

	def ding_score(self,list_x):
		score = len(list_x)*10
		i=0
		while i<len(list_x) -1:
			if list_x[i] == list_x[i+1]:
				i = i + 1
				if list_x[i] < 3 or list_x[i] > 7:
					score += 5
				else:
					score += 3
			elif list_x[i] + 1 == list_x[i+1] and list_x[i] != 1 and list_x[i] != 8:
				score +=3
			i += 1 

		score += self.group_shunzi(list_x) * 5
		if list_x.count(1) == 1 and list_x.count(2) == 0 and self.list_t.count(3) == 0:
			score -= 2
		if list_x.count(9) == 1 and list_x.count(8) == 0 and self.list_t.count(7) == 0:
			score -= 2
		return score


	def ding_sure(self):
		list_score = []
		score_t = self.ding_score(self.list_t)
		score_w = self.ding_score(self.list_w)
		score_b = self.ding_score(self.list_b)
		list_score.append(score_t)
		list_score.append(score_w)
		list_score.append(score_b)
		if score_t == min(list_score):
			self.ding = 't'
		elif score_w == min(list_score):
			self.ding = 'w'
		elif score_b == min(list_score):
			self.ding = 'b'


	#def think(self):
		

	def caculate_score(self):
		score = 0;
		nodui_score = 0;
		num_nen_peng = 0;
		if self.ding == 't':
			if self.cal_dui(self.list_w, self.list_b) == 7:
				return 14
			nodui_score = self.group_shunzi(self.list_w)*3 + self.group_shunzi(self.list_b)*3
			num_nen_peng = self.find_nen_peng(nodui_score)
			nodui_score = nodui_score + len(self.have_peng)*3 + len(self.have_gang)*3	
		elif self.ding == 'w':
			if self.cal_dui(self.list_t, self.list_b) == 7:
				return 14
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_b)*3
			num_nen_peng = self.find_nen_peng(nodui_score)
			nodui_score = nodui_score + len(self.have_peng)*3 + len(self.have_gang)*3	
		elif self.ding == 'b':
			if self.cal_dui(self.list_t, self.list_w) == 7:
				return 14
			nodui_score = self.group_shunzi(self.list_t)*3 + self.group_shunzi(self.list_w)*3
			num_nen_peng = self.find_nen_peng(nodui_score)
			nodui_score = nodui_score + len(self.have_peng)*3 + len(self.have_gang)*3
			
		if num_nen_peng > 0 and num_nen_peng <= 3:
				score = nodui_score + num_nen_peng + 1   #计算分数
		elif num_nen_peng > 3:
				score = nodui_score + num_nen_peng
		else:
			score = nodui_score
		self.score = score
		return score

	def find_nen_gang(self):
		self.nengang.clear()
		gang_pai = 0;
		tmp_player = copy.deepcopy(self)
		i = 0;
		cal_list1 = []; cal_list2 = [];
		list1_type = 'n'; list2_type = 'n';
		if tmp_player.ding == 't':
			cal_list1 = tmp_player.list_w; cal_list2 = tmp_player.list_b;
			list1_type = 'w'; list2_type = 'b'
		elif (self.ding == 'w'):
			cal_list1 = tmp_player.list_t; cal_list2 = tmp_player.list_b;
			list1_type = 't'; list2_type = 'b'
		elif (self.ding == 'b'):
			cal_list1 = tmp_player.list_t; cal_list2 = tmp_player.list_w;
			list1_type = 't'; list2_type = 'w'
		for x in range(0, 2):
			i = 0
			if x == 1:
				cal_list1 = cal_list2; list1_type = list2_type
			while i < len(cal_list1) - 1:
				if cal_list1.count(cal_list1[i]) == 3:
					data = cal_list1.pop(i);cal_list1.pop(i);cal_list1.pop(i)
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 3:
						self.nengang.append(item_to_spec(data, list1_type))
					cal_list1.insert(i,data);cal_list1.insert(i,data);cal_list1.insert(i,data)
					i = i + 3
				elif cal_list1.count(cal_list1[i]) == 4:
					data = cal_list1.pop(i);cal_list1.pop(i);cal_list1.pop(i);cal_list1.pop(i);
					tmp_player.caculate_score()
					if self.score - tmp_player.score <= 5:
						gang_pai = item_to_spec(data, list1_type)
					cal_list1.insert(i,data);cal_list1.insert(i,data);cal_list1.insert(i,data);cal_list1.insert(i,data)
					i = i + 4
				else:
					i = i + 1
		del tmp_player
		return gang_pai

	def find_nen_peng(self,nodui_score):
		self.nenpeng.clear()
		self.list_dui.clear()
		self.left_pai_peng.clear()
		score = 0;nenpeng_num = 0;tmp_score = 0
		cal_list1 = []; cal_list2 = [];
		list1_type = 'n'; list2_type = 'n';
		if self.ding == 't':
			cal_list1 = self.list_w; cal_list2 = self.list_b;
			list1_type = 'w'; list2_type = 'b'
		elif (self.ding == 'w'):
			cal_list1 = self.list_t; cal_list2 = self.list_b;
			list1_type = 't'; list2_type = 'b'
		elif (self.ding == 'b'):
			cal_list1 = self.list_t; cal_list2 = self.list_w;
			list1_type = 't'; list2_type = 'w'
		
		num_dui = self.cal_dui(cal_list1, cal_list2)
		i = 0
		if num_dui > 0:
			while i < len(cal_list1)-1:
				if cal_list1[i] == cal_list1[i+1]:
					self.list_dui.append(item_to_spec(cal_list1[i], list1_type))
					data = cal_list1.pop(i);cal_list1.pop(i)
					tmp_score = self.group_shunzi(cal_list1)*3+self.group_shunzi(cal_list2)*3
					if tmp_score == nodui_score:
						self.nenpeng.append(item_to_spec(data, list1_type))
						nenpeng_num = nenpeng_num + 1
						if self.cant_see_left(item_to_spec(data, list1_type)) > 0:
							self.left_pai_peng.append(item_to_spec(data, list1_type));
					cal_list1.insert(i, data);cal_list1.insert(i, data);
					i = i+1
				i=i+1
			i = 0
			while i < len(cal_list2)-1:
				if cal_list2[i] == cal_list2[i+1]:
					self.list_dui.append(item_to_spec(cal_list2[i], list2_type))
					data = cal_list2.pop(i);cal_list2.pop(i)
					tmp_score = self.group_shunzi(cal_list1)*3 + self.group_shunzi(cal_list2)*3
					if tmp_score == nodui_score:
						self.nenpeng.append(item_to_spec(data, list2_type))
						nenpeng_num = nenpeng_num + 1
						if self.cant_see_left(item_to_spec(data, list2_type)) > 0:
							self.left_pai_peng.append(item_to_spec(data, list2_type));
					cal_list2.insert(i, data); cal_list2.insert(i,data);
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

	def pai_value_deep(self,pai):
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
	def pai_value(self,pai):
		if self.list_ding.count(self.get_pai_attr(pai))>=2:
			return 10+self.pai_value_deep(pai)
		else:
			return self.pai_value_deep(pai)

	def get_pai_attr(self,pai):
		if pai < 10:
			return 't'
		elif pai < 20:
			return 'w'
		elif pai <30:
			return 'b'

	def duan_zhang_pai(self,pai):
		left1 = 0; left2 = 0; right1 = 0; right2 = 0
		left_pai = self.cant_see_left(pai)
		if  left_pai<=2:
			if pai == 1 or pai == 11 or pai == 21:
				if self.cant_see_left(pai + 1) == 0:
					return 1
				if self.cant_see_left(pai + 2) == 0:
					return 1
			elif pai == 9 or pai == 19 or pai == 29:
				if self.cant_see_left(pai -1) == 0:
					return 1
				if self.cant_see_left(pai - 2) == 0:
					return 1
			elif pai == 2 or pai == 12 or pai == 22:
				if self.cant_see_left(pai + 1) == 0:
					return 1
			elif pai == 8 or pai == 18 or pai == 28:
				if self.cant_see_left(pai -1) == 0:
					return 1
			else:
				left1 = self.cant_see_left(pai - 1)
				left2 = self.cant_see_left(pai - 2)
				right1 = self.cant_see_left(pai + 1)
				right2 = self.cant_see_left(pai + 2)
				if left1 == 0:
					if right1 == 0 or right2 == 0:
						return 1
				elif right1 == 0:
					if left1 == 0 or left2 == 0:
						return 1
		return 0



	def cant_see_left(self,pai):
		list_pai = copy.copy(self.list_t)
		for i in range(0, len(self.list_w)):
			list_pai.append(self.list_w[i] + 10)
		for i in range(0, len(self.list_b)):
			list_pai.append(self.list_b[i] + 20)
		num = 0
		for i in range(0,len(self.user_desk.list_total_player)):
			num = num + self.user_desk.list_total_player[i].have_peng.count(pai) * 2 + self.user_desk.list_total_player[i].have_gang.count(pai) * 3
		num = num + list_pai.count(pai) + self.user_desk.list_river.count(pai)
		return 4 - num

	def list_cant_see_left(self,list_x):
		num = 0
		for i in range(0, len(list_x)):
			ding_num = self.list_ding.count(self.get_pai_attr(list_x[i]))
			tmp_num = self.cant_see_left(list_x[i])
			duan_zhang = self.duan_zhang_pai(list_x[i])
			if ding_num == 2:
				if duan_zhang:
					if tmp_num >= 3:
						tmp_num = tmp_num - 2
					tmp_num = tmp_num * 1.6

				elif len(self.user_desk.list_tuple) <= 25:
					if tmp_num >= 3:
						tmp_num = tmp_num *0.8
					else:
						tmp_num = tmp_num * 1
				else:
					if tmp_num >= 3:
						tmp_num = tmp_num * 1
					else:
						tmp_num = tmp_num * 1.3

				
			elif ding_num == 3:
				if self.user_desk.phase == 1:
					tmp_num = tmp_num * 1.5
				else:
					tmp_num = tmp_num * 2
			elif ding_num == 1:

				if duan_zhang:
					if tmp_num >= 3:
						tmp_num = tmp_num - 2
					tmp_num = tmp_num * 1.5
				else:
					if len(self.user_desk.list_tuple) <= 25:
						if tmp_num >= 3:
							tmp_num = tmp_num * 0.4
						else:
							tmp_num = tmp_num * 0.6
					else:
						if tmp_num >= 3:
							tmp_num = tmp_num * 0.6
						else:
							tmp_num = tmp_num *0.8

			elif ding_num == 0:
				if duan_zhang:
					if tmp_num >= 3:
						tmp_num = tmp_num - 2
					tmp_num = tmp_num * 1.5
				else:
					if len(self.user_desk.list_tuple) <= 25:
						if tmp_num >= 3:
							tmp_num = tmp_num * 0.3
						else:
							tmp_num = tmp_num *0.5
					else:
						if tmp_num >= 3:
							tmp_num = tmp_num * 0.5
						else:
							tmp_num = tmp_num *0.7

				
				
			num = num + tmp_num
		return num


def test_spec():
	p1 = player();
	p1.name = 'pa'
	p1.list_t=[3,3,4,5,7,9]
	p1.list_b=[1,1,3,3,3,8,8,9]
	p1.list_ding = ['t','b','w','w']
	#p1.have_peng.append(18)
	#p1.have_peng.append(19)
	'''p1.user_desk.list_river.append(22)
	p1.user_desk.list_river.append(27)
	p1.user_desk.list_river.append(27)
	p1.user_desk.list_river.append(28)
	p1.user_desk.list_river.append(9)
	p1.user_desk.list_river.append(9)
	p1.user_desk.list_river.append(9)
	p1.user_desk.list_river.append(9)'''
	for i in range(0,21):
		p1.user_desk.list_tuple.append(11)
	p1.ding='w'
	#p1.caculate_score()
	#p1.mopai(22)
	print(p1.caculate_score())
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

#test_spec()


play_times = 5;
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
hu_state = [[]]
hu_one_state = []
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
	desk1.list_total_player = [p1,p2,p3,p4]
	desk1.list_player = [p1,p2,p3,p4]

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
		list_player[i].user_desk = desk1
		for j in range(0, 4):
			list_player[j].list_ding.append(list_player[i].ding)




	p1.human = 1
	index = 0
	count_player = 4
	hu_one_state.clear()
	while len(desk1.list_tuple)>0 and len(list_player) > 0:
		if len(desk1.list_tuple) >= 28:
			desk1.phase = 1
		else:
			desk1.phase = 2
	
		list_player[index].mopai(desk1.list_tuple.pop())
		list_player[index].show()
		if list_player[index].score >= 14:
			print(list_player[index].name," hu le ####################################")
			hu_one_state.append(list_player[index].name)
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
								hu_one_state.append(list_player[i].name)
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

	print("no_user_hu:",no_user_hu,"hu_user1:",hu_user1,"hu_user2:",hu_user2,"hu_user3:",hu_user3,"hu_user4:",hu_user4)
	hu_state.append(hu_one_state)

ticks2 = time.time()
print("play_times:",play_times,"no_user_hu:",no_user_hu,"hu_user1:",hu_user1,"hu_user2:",
	hu_user2,"hu_user3:",hu_user3,"hu_user4:",hu_user4,"use_time:",ticks2-ticks1,"err_start:",err_start)

#for i in range(0, len(hu_state)):
#	print(hu_state[i])
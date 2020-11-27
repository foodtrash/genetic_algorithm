import random


class Algorithm(object):
	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b 
		self.c = c
		self.d = d
		self.f_min_classic = 0
		self.f_max_classic = 0
	
	
	def algorithm_classic(self):
		f_min = 0
		f_max = 0
		f_min_iter = 0
		f_max_iter = 0
		iteration = 1
		for x in range(-10, 54):
			result = self.a + self.b * x + self.c * x**2 + self.d * x ** 3
			if(result < f_min):
				f_min = result
				f_min_iter = iteration
			if(result > f_max):
				f_max = result
				f_max_iter = iteration
			iteration += 1
		print("max: ", f_max, "  bin: ", bin(f_max), "iter:  ", f_max_iter)
		print("min: ", f_min, "  bin: ", bin(f_min), "iter:  ", f_min_iter)
		self.f_min_classic = f_min
		self.f_max_classic = f_max


	def algorithm_genetic(self):
		chromosome = self.make_chromosomes()
		f_min = 0
		f_min_iter = 0
		f_max = 0
		f_max_iter = 0
		f_min_flag = 0
		f_max_flag = 0
		iteration = 1
		while(True):
			decode = self.decode_decimal(chromosome)
			f_min, f_max = self.func(decode, f_min, f_max)
			before_mutation = self.select_couples(chromosome)
			chromosome = self.mutation(before_mutation)
			if f_min == self.f_min_classic and f_min_flag != 1:
				f_min_iter, f_min_flag = self.sumbit_max_or_min(f_min, f_min_iter, iteration)
			if f_max == self.f_max_classic and f_max_flag != 1:
				f_max_iter, f_max_flag = self.sumbit_max_or_min(f_max, f_max_iter, iteration)
			if (f_max == self.f_max_classic and f_min == self.f_min_classic):
				break
			iteration += 1
		print("max: ", f_max, "  bin: ", bin(f_max), "  iteration:  ", f_max_iter)
		print("min: ", f_min, "  bin: ", bin(f_min), "  iteration:  ", f_min_iter)


	def sumbit_max_or_min(self, value, current_iteration, iteration):
		if (value == self.f_min_classic or value == self.f_max_classic ):
			flag = 1
			return iteration, flag
		else:
			flag = 0
			return current_iteration, flag


	def mutation(self, before_mutation):
		random_choice = random.choice(before_mutation)
		before_mutation.remove(random_choice)
		number = (random.randint(0, 5))
		these_number = random_choice[number]
		new_value = '0' if these_number == '1' else '1'
		new_number = random_choice[:number]
		new_number += new_value
		new_number += random_choice[number+1:]
		before_mutation.append(new_number)
		return before_mutation


	def select_couples(self, chromosome):
		pair_1_1 = random.choice(chromosome)
		chromosome.remove(pair_1_1)
		pair_1_2 = random.choice(chromosome)
		chromosome.remove(pair_1_2)
		pair_2_1 = random.choice(chromosome)
		chromosome.remove(pair_2_1)
		pair_2_2 = random.choice(chromosome)
		chromosome.remove(pair_2_2)
		return self.crossing(pair_1_1,pair_1_2,pair_2_1,pair_2_2)


	def crossing(self, pair_1_1, pair_1_2, pair_2_1, pair_2_2):
		random_choice = [1, 2]
		random_pair = [1, 2]
		new_person = list()
		for i in range (2):
			choice = random.choice(random_choice)
			pair = random.choice(random_pair)
			if pair == 1:
				if(choice==1):
					buff1_1 = pair_1_1[0:2]
					buff1_1 += pair_1_2[2:]
					buff1_2 = pair_1_2[0:2]
					buff1_2 += pair_1_1[2:]
				if(choice==2):
					buff1_1 = pair_1_1[0:4]
					buff1_1 += pair_1_2[4:]
					buff1_2 = pair_1_2[0:4]
					buff1_2 += pair_1_1[4:]
			if pair == 2:
				if(choice == 1):
					buff2_1 = pair_2_1[0:2]
					buff2_1 += pair_2_2[2:]
					buff2_2 = pair_2_2[0:2]
					buff2_2 += pair_2_1[2:]
				if(choice == 2):
					buff2_1 = pair_2_1[0:4]
					buff2_1 += pair_2_2[4:]
					buff2_2 = pair_2_2[0:4]
					buff2_2 += pair_2_1[4:]
			random_choice.remove(choice)
			random_pair.remove(pair)
		new_person.append(buff1_1)
		new_person.append(buff1_2)
		new_person.append(buff2_1)
		new_person.append(buff2_2)
		return(new_person)


	def func(self, array, f_min, f_max):
		for x in array:
			#f(x) = a + bx + cx 2  + dx 3
			result=self.a + self.b * (x - 10) + self.c * (x - 10)** 2 + self.d * (x - 10)** 3
			if result < f_min:
				f_min = result
			if result > f_max:
				f_max = result
		return f_min, f_max


	def decode_decimal(self, array_binary):
		array_decimal = array_binary[::-1]
		for z in range(0,len(array_decimal)):
			array_decimal[z] = int(array_decimal[z], 2)
		return array_decimal


	def make_chromosomes(self):
		array_of_chromosomes=list()
		for i in range (4):
			new_chromosome = ""
			for z in range(6):
				new_chromosome += str(random.randint(0, 1))
			array_of_chromosomes.append(new_chromosome)
		return array_of_chromosomes


	
if __name__ == "__main__":
	a=Algorithm(2,-5,47,-3)
	print("			classic alghoritm\n")
	a.algorithm_classic()
	print("\n")
	print("			genetic alghoritm\n")
	a.algorithm_genetic()
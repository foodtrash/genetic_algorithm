import random


class Algorithm(object):
	def __init__(self, a, b, c, d, number_of_chromosomes, mutation):
		self.a = a
		self.b = b 
		self.c = c
		self.d = d
		self.f_min_classic = 0
		self.f_max_classic = 0
		self.number_of_chromosomes = number_of_chromosomes
		self.mutation = mutation

	
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
			couples = self.select_couples(chromosome)
			couples = self.unpack_pairs(couples)
			chromosome = self.mutation_func(couples)
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


	def mutation_func(self, array_of_chromosomes):
		mutation_list=list()
		while self.mutation:
			random_choice = random.choice(array_of_chromosomes)
			array_of_chromosomes.remove(random_choice)
			number = (random.randint(0, 5))
			these_number = random_choice[number]
			new_value = '0' if these_number == '1' else '1'
			new_chromosome = random_choice[:number]
			new_chromosome += new_value
			new_chromosome += random_choice[number+1:]
			mutation_list.append(new_chromosome)
			self.mutation -=1
		all_list_of_chromosomes = self.add_non_mutable_chromosomes(array_of_chromosomes,mutation_list)
		return array_of_chromosomes


	def add_non_mutable_chromosomes(self,non_mutable,mutable):
		for i in non_mutable:
			mutable.append(i)
		return mutable


	def unpack_pairs(self,pairs):
		new_array=list()
		for couples in pairs:
			for single in couples:
				new_array.append(single)
		return new_array

	def select_couples(self, chromosome):
		new_chromosome = list()
		generate_slice = self.generate_slice()
		while True:
			if not generate_slice:
					generate_slice = self.generate_slice()
			first_gene = random.choice(chromosome)
			chromosome.remove(first_gene)
			second_gene = random.choice(chromosome)
			chromosome.remove(second_gene)
			number = random.choice(generate_slice)
			generate_slice.remove(number)
			new_genes = self.crossing(first_gene, second_gene, number)
			new_chromosome.append(new_genes)
			if not chromosome:
				return new_chromosome



	def generate_slice(self):
		return [x for x in range (1,6)]


	def crossing(self, chromosome_1,chromosome_2,randomnumber):
		buf1=chromosome_1
		chromosome_1 = chromosome_1[:randomnumber]
		chromosome_1 += chromosome_2[randomnumber:]
		chromosome_2 = chromosome_2[:randomnumber]
		chromosome_2 += buf1[randomnumber:]
		return [chromosome_1, chromosome_2]


		
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
		for i in range (self.number_of_chromosomes):
			new_chromosome = ""
			for z in range(6):
				new_chromosome += str(random.randint(0, 1))
			array_of_chromosomes.append(new_chromosome)
		return array_of_chromosomes



if __name__ == "__main__":
	a=Algorithm(2,-5,47,-3,40,4)
	print("			classic alghoritm\n")
	a.algorithm_classic()
	print("\n")
	print("			genetic alghoritm\n")
	a.algorithm_genetic()
from stack import LRUstack

def FIFO(number_of_frames, acess_sequence):
	acess_sequence_tmp = list(acess_sequence)
	frames = [None] * number_of_frames
	last_index_acessed = 0
	missing_pages = 0
	
	for i in acess_sequence_tmp:	
		if(i not in frames):
			frames[last_index_acessed] = i
			last_index_acessed = (last_index_acessed+1) % number_of_frames
			missing_pages += 1

	print("FIFO", missing_pages)

def OTM(number_of_frames, acess_sequence):
	acess_sequence_tmp = list(acess_sequence)
	frames = [None] * number_of_frames
	index = 0
	index_acess = 0
	missing_pages = 0
	
	for i in acess_sequence_tmp:

		if(i not in frames):

			#Caso onde ainda existe espaço nos quadros e apenas precisamos inserir no quadro vazio
			if(index < number_of_frames):
				frames[index] = i
				index += 1
				missing_pages += 1

			else:
				tmp = 0
				gap = 0
				large_gap = 0
	
				for f in frames:
					for j in range(index_acess, len(acess_sequence_tmp)):
						if(acess_sequence_tmp[j] == f): break
						gap += 1

					if(gap > large_gap):
						large_gap = gap
						tmp = f

					gap = 0	
						
				frames[frames.index(tmp)] = i
				missing_pages += 1
				
		index_acess += 1
							

	print("OTM", missing_pages)

def LRU(number_of_frames, acess_sequence):
	acess_sequence_tmp = list(acess_sequence)
	frames = [None] * number_of_frames
	index = 0
	missing_pages = 0
	count = 0
	stack = LRUstack()

	for i in acess_sequence_tmp:
		stack.push(i)
		if(i not in frames):
			
			if(count < number_of_frames):
				frames[index] = i
				index += 1
				missing_pages += 1
				count += 1
			else:
				lru = stack.take_base()
				while(lru not in frames):
					stack.remove(lru)
					lru = stack.take_base()

				index = frames.index(lru)
				frames[index] = i
				missing_pages += 1


	print("LRU", missing_pages)

def main():
	file = open("input.txt", "r")

	number_of_frames = int(file.readline())
	acess_sequence = []

	for line in file:
		acess_sequence.append(int(line))

	FIFO(number_of_frames, acess_sequence)
	OTM(number_of_frames, acess_sequence)
	LRU(number_of_frames, acess_sequence)

	file.close()

if __name__ == '__main__':
	main()
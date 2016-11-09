from stack import Stack

def FIFO(number_of_frames, acess_sequence):
	acess_sequence_tmp = list(acess_sequence)
	frames = [None] * number_of_frames
	last_index_acessed = 0
	count = 0
	
	for i in acess_sequence_tmp:	
		if(i not in frames):
			frames[last_index_acessed] = i
			last_index_acessed = (last_index_acessed+1) % number_of_frames
			count+=1

	print("FIFO", count)

def OTM(number_of_frames, acess_sequence):
	pass

def LRU(number_of_frames, acess_sequence):
	acess_sequence_tmp = list(acess_sequence)
	frames = [None] * number_of_frames
	last_index_acessed = 0
	count = 0
	aux = 0
	stack = Stack()

	for i in acess_sequence_tmp:
		stack.push(i)
		if(i not in frames):
			
			if(aux < number_of_frames):
				frames[last_index_acessed] = i
				last_index_acessed = last_index_acessed+1
				count+=1
				aux+=1
			else:
				lru = stack.take_base()
				while(lru not in frames):
					stack.pop(lru)
					lru = stack.take_base()

				last_index_acessed = frames.index(lru)
				frames[last_index_acessed] = i
				count+=1

	print("LRU", count)


def main():
	file = open("../inputs/input.txt", "r")

	number_of_frames = int(file.readline())
	acess_sequence = []

	for line in file:
		acess_sequence.append(int(line))

	FIFO(number_of_frames, acess_sequence)
	LRU(number_of_frames, acess_sequence)

	file.close()


if __name__ == '__main__':
	main()

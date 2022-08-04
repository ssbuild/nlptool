
import os

def get_file_list(data_dir):
	fs = []
	for root ,dirs,files in os.walk(data_dir):
		for file in files:
			fs.append(os.path.join(root,file))
	return fs

if __name__ == '__main__':
	baselist = [
		"datasets/nlpcc2016-word-seg-train.dat",
		"datasets/nlpcc2016-wordseg-dev.dat",
		"datasets/nlpcc2016-wordseg-test.dat"
	]

	#baselist = get_file_list(r'F:\nlpdata_2022\分词\icwb2-data\training')
	baselist = get_file_list(r'F:\nlpdata_2022\词性\People_Daily_1998_01_06')


	totsent = 0  	#计算句子数
	totword = 0 	#计算词数
	totchars = 0 	# 计算字符数

	for file in baselist:
		with open(file,mode='r',encoding='utf-8',newline='\n') as f:
			lines = f.readlines()

			sent = 0
			word = 0
			chars = 0

			for line in lines:
				sent +=1
				totsent += 1

				words = line.split("\\s");
				word +=  len(words)
				totword += len(words)

				for c in words:
					chars += len(c)
					totchars += len(c)

			print()
			print(file , ":")
			print("句子数：" , sent)
			print("词数：" , word)
			print("字符数：" , chars)

	print()
	print("总句子数：", totsent)
	print("总词数：", totword)
	print("字符数：", totchars)


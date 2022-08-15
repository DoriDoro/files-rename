import os

def main():
	i = 1
	path = '/ update your path /folder_renaming/images/'
	for filename in os.listdir(path):
		my_images = 'img' + str(i) + '.jpg'
		my_source = path + filename
		my_destination = path + my_images
		os.rename(my_source, my_destination)
		i += 1

if __name__ == '__main__':
	main()


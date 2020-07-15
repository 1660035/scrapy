from urllib.parse import unquote, urlparse
from pathlib import PurePosixPath

url = 'https://www.news.com.au/travel/australian-holidays/queensland/annastacia-palaszczuk-urges-qld-travellers-to-visit-whitsundays-not-bali/news-story/317f32614a48b19890e6bfc4e512a782'

domain_name = urlparse(url).path
#if(len(domain_name) == 0):
	#print(str(1))

#print(str(domain_name))
sample =PurePosixPath(
	unquote (
			urlparse(
					url
				).path
		)
	).parts[0]


#print(str(sample))



sample_de = PurePosixPath(
	unquote (
			urlparse(
					url
				).path
		)
	).parts

print(len(sample_de))


for i in range(len(sample_de)):
	print(str(i))




print(str(url))
i = 0
while(True):
	sample =PurePosixPath(
	unquote (
			urlparse(
					url
				).path
		)
	).parts[i]

	print("i=" +str(i ) + "        " + str(sample))
	i  = i + 1

	
	print("\n")









def checkAnagram(s1, s2):

	s2hash = [0 for i in range(26)]


	s1hash = [0 for i in range(26)]
	s1len = len(s1)
	s2len = len(s2)

	
	if (s1len > s2len):
		return False

	left = 0
	right = 0

	
	while (right < s1len):
		s1hash[ord(s1[right]) - 97] += 1
		s2hash[ord(s2[right]) - 97] += 1
		right += 1

	right -= 1

	
	while (right < s2len):
		if (s1hash == s2hash):
			return True
		right += 1

		if (right != s2len):
			s2hash[ord(s2[right]) - 97] += 1

		s2hash[ord(s2[left]) - 97] -= 1
		left += 1

	return False

tc=int(input())
i=0
fin=[]
while(i<tc):
	s1 = input()
	s2 = input()
	if (checkAnagram(s1, s2)):
		fin.append("YES")
	else:
		fin.append("NO")
	i=i+1
for i in fin:
    print(i)

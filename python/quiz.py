

p=open('quiz.html', 'w')
for x in range(0,10):
	
	x = str(x)



	p.write('<br><input type= "checkbox" name = "quiz" value = "1.'+x+'">Quiz 1.'+x)

p.write('</form>')	

p.close
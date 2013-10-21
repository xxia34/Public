# Michael Hartle & Xiaojing Xia
# 902973320 / 902999067
# mhartle@gatech.edu/xxia34@gatech.edu
# Section B03
# We worked on this assignment alone, using only this semester's course materials.

from Myro import *

def makeWebPage(numberOfPictures):
    lightlist = []
    for i in range(numberOfPictures):
        p = takePicture()
        l = sum(getLight())/3
        lightlist.append(l)
        savePicture(p,"pic"+str(i)+".jpg")
        turnLeft(1,.5)


    html = open("myPage.html","w")
    html.write("""<!DOCTYPE html>\n<html>\n<head>\n<title>Michael and Xiaojing's Webpage</title>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\n</head>\n<body>\n<h1>Welcome to Michael and Xiaojing's Picture Page!</h1>\n<p>Made by Michael Hartle and Xiaojing Xia</p>""")
    html.write("<table>\n  ")

    html.write("<tr>\n")
    for i in range(numberOfPictures):
        if i%4==0 and i!=0:
            html.write("</tr>\n<tr>")
        html.write("""\t<td><img src="pic{}.jpg" width="320" height="200" alt="Picx"/>{}</td>""".format(i,str(lightlist[i])))

    html.write("  </tr>")

    html.write("</table>")
    html.write("<p>Pictures taken by "+ getName() + ".</p>\n</body>\n</html>")
    html.close()

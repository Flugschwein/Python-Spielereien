html = open('hey.html', 'a')
html.write('<TABLE BORDER=0 CELLPADDING=10 CELLSPACING=0>\n')
atm = 0
for i in range(16):
    html.write('    <TR>\n')
    for j in range(16):
        string = str(hex(atm)[2:])
        if len(string) != 8:
            for i in range(8-len(string)):
                string = "0"+string
        atm += 0xffffff//256
        html.write('      <TD WIDTH="10" HEIGHT="10" BGCOLOR=#')
        html.write(string)
        html.write('>\n      &nbsp;\n      </TD>\n')
    html.write('    </TR>\n')
html.write('</TABLE>')
html.close()

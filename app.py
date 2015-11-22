from BeautifulSoup import BeautifulSoup
from colour import Color
import mimetypes
from flask import Flask, render_template,send_file,request
from markupsafe import Markup
from jsonQuery import analysis
import cairosvg

mimetypes.add_type('image/svg+xml', '.svg')

def createPng(dictionary):
    print dictionary
    #dictionary = {u'HI':0,u'WA': 0.11640154287441533, u'DE': 0.10653245699693925, u'DC': 0.0041999218375667908, u'WI': 0.04177312011442888, u'WV': 0.044655479867581796, u'FL': 0.0145210401703301, u'WY': 0.0083883931524397631, u'NH': 0.013325407353239786, u'NJ': 0.0022909522192498233, u'NM': 0.045981546101387376, u'TX': 0.37338386680563035, u'LA': 0.0055753859680801555, u'NC': 0.05631382783926054, u'ND': 0.0024310450918256063, u'NE': 0.0050522372216981254, u'TN': 0.11086195089846941, u'NY': 0.015144044310735185, u'PA': 0.014369790728777414, u'CT': 0.0083071183677789779, u'AK': 0.0094143873303377656, u'NV': 0.026699002607654933, u'VA': 0.035906849853128003, u'GU': 0.053507608934921805, u'CO': 0.15141854013737513, u'CA': 0.47255912028907099, u'AL': 0.4881142007657831, u'AR': 0.014430365702860956, u'VT': 0.00019083748747501843, u'IL': 0.093519577133844733, u'GA': 0.29313095413457285, u'IN': 0.18011246989907964, u'IA': 0.0076042066693034135, u'MA': 0.01480640770425893, u'AZ': 0.16582270977876581, u'ID': 0.029387810928551077, u'PR': 0.01542957591185485, u'ME': 0.017373840484600587, u'MD': 0.0035692407198571344, u'OK': 0.005896157834564977, u'OH': 0.30339268698038618, u'UT': 0.024269509318009322, u'MO': 0.13195694464937613, u'MN': 0.003030122766900322, u'MI': 0.20199045380985614, u'RI': 0.040445884901888586, u'KS': 0.0020843095923908589, u'MT': 0.011052564050178576, u'MS': 0.0081120356417410562, u'SC': 0.053881203600723133, u'KY': 0.10614887474089574, u'OR': 0.020659682476818934, u'SD': 0.0065830661458009991}
    svg = open('/home/ms/PycharmProjects/A.R.M.Y2/USA_STATES_Labels.svg', 'r').read()
    soup = BeautifulSoup(svg)
    paths = soup.findAll('path')

    path_style = 'font-size:12px;fill-rule:nonzero;stroke:#000000;stroke-opacity:1;stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
    for p in paths:

        if p['id'] not in ["State_Lines", "separator","path4148","MI-","SP-"]:
            #print str(p['id'])
            if str(p['id']).startswith("path"):
                continue
            color = Color("blue", saturation= dictionary[str(p['id'])])
            p['style'] = path_style + color.hex

    #print soup.prettify()
    f=open('static/output.png','w')
    cairosvg.svg2png(bytestring=soup.prettify(),write_to=f)
    f.close()
    return soup.prettify()

app = Flask(__name__)


@app.route('/',methods=['POST'])
def getOutput():
    l=[]
    _range = request.form['Range']
    _input1 = request.form['Input1']
    print _input1
    if int(_input1)==3:
        l.append('housing')
        l.append('military')
    elif int(_input1)==1:
        l.append('housing')
    else:
        l.append('military')

    l.append(int(_range))

    print l
    data= analysis(l)
    createPng(data)
    return render_template('input.html')

@app.route("/input")
def main():
    return render_template('input.html')


if __name__ == "__main__":
    app.run()

import flask
import time

app = flask.Flask(__name__)

@app.route('/sort', methods=['GET', 'POST'])
def sort():
    
    def bubbleSort(UnsortedList):
        print(str(UnsortedList))
        html="""<div style="width:100%" align="center"><h1>Bubble Sort, Quick Sort, Selection Sort and Insertion Sort</h1><form action="sort" method="POST">
    <input type="text" name="numbers" value="{0}"/>
    <select name="algorithm" id="algorithm">
        <option selected>Bubble Sort</option>
        <option>Selection Sort</option>
        <option>Insertion Sort</option>
        <option>Quick Sort</option>
    </select>
    <input type="submit" value="Submit"/>
    <input type="button" value="Jumble" onclick="document.getElementById('myContent').innerHTML='{1}'"/>
</form>""".format(str(UnsortedList).strip('[]'), str(UnsortedList).strip('[]'))

        for j in range(len(UnsortedList)-1,0,-1):
            if j==len(UnsortedList)-1:
                yield html
                yield '<div id="myContent"></div></div>'
                yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList
            for i in range(j):
                time.sleep(1)
                if UnsortedList[i]>UnsortedList[i+1]:
                    temp = UnsortedList[i]
                    UnsortedList[i] = UnsortedList[i+1]
                    UnsortedList[i+1] = temp
                    yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList	
	
    def insertionSort(UnsortedList):
        
        html="""<div style="width:100%" align="center"><h1>Bubble Sort, Quick Sort, Selection Sort and Insertion Sort</h1><form action="sort" method="POST">
    <input type="text" name="numbers" value="{0}"/>
    <select name="algorithm" id="algorithm">
        <option>Bubble Sort</option>
        <option>Selection Sort</option>
        <option selected>Insertion Sort</option>
        <option>Quick Sort</option>
    </select>
    <input type="submit" value="Submit"/>
    <input type="button" value="Jumble" onclick="document.getElementById('myContent').innerHTML='{1}'"/>
</form>""".format(str(UnsortedList).strip('[]'), str(UnsortedList).strip('[]'))

        for i in range( 1, len( UnsortedList ) ):
            temp = UnsortedList[i]
            j = i
            if i == 1:
                yield html
                yield '<div id="myContent"></div></div>'
                yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList
                time.sleep(1)
            while j > 0 and temp < UnsortedList[j - 1]:
                UnsortedList[j] = UnsortedList[j - 1]
                j -= 1
                time.sleep(1)
                yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList
            UnsortedList[j] = temp
            time.sleep(1)
            yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList

    def quickSort(UnsortedList, flag):



        html="""<div style="width:100%" align="center"><h1>Bubble Sort, Quick Sort, Selection Sort and Insertion Sort</h1><form action="sort" method="POST">
    <input type="text" name="numbers" value="{0}"/>
    <select name="algorithm" id="algorithm">
        <option>Bubble Sort</option>
        <option>Selection Sort</option>
        <option>Insertion Sort</option>
        <option selected>Quick Sort</option>
    </select>
    <input type="submit" value="Submit"/>
    <input type="button" value="Jumble" onclick="document.getElementById('myContent').innerHTML='{1}'"/>
</form>""".format(str(UnsortedList).strip('[]'), str(UnsortedList).strip('[]'))

        if(flag == 1):
            time.sleep(1)
            yield html
            yield '<div id="myContent"></div></div>'
            yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList

        time.sleep(1)                        
        yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList


        if len(UnsortedList) > 1:
            pivot_index = int(len(UnsortedList) / 2)
            smaller_items = []
            larger_items = []

            for i in range(len(UnsortedList)):

                if i != pivot_index:
                    if UnsortedList[i] < UnsortedList[pivot_index]:
                        smaller_items.append(UnsortedList[i])
                    else:
                        larger_items.append(UnsortedList[i])

            yield from quickSort(smaller_items, 2)
            yield from quickSort(larger_items, 2)
            UnsortedList[:] = smaller_items + [UnsortedList[pivot_index]] + larger_items
                
            time.sleep(1)                        
            yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList       


    def selectionSort(UnsortedList):

        html="""<div style="width:100%" align="center"><h1>Bubble Sort, Quick Sort, Selection Sort and Insertion Sort</h1><form action="sort" method="POST">
    <input type="text" name="numbers" value="{0}"/>
    <select name="algorithm" id="algorithm">
        <option>Bubble Sort</option>
        <option selected>Selection Sort</option>
        <option>Insertion Sort</option>
        <option>Quick Sort</option>
    </select>
    <input type="submit" value="Submit"/>
    <input type="button" value="Jumble" onclick="document.getElementById('myContent').innerHTML='{1}'"/>
</form>""".format(str(UnsortedList).strip('[]'), str(UnsortedList).strip('[]'))

        for i in range (len(UnsortedList)):
            if i == 0:
                yield html
                yield '<div id="myContent"></div></div>'
                yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList
            minNumberIndex = i
            j=i+1
            for j in range (j,len(UnsortedList)):
                if UnsortedList[j]<UnsortedList[minNumberIndex]:
                    minNumberIndex=j
                    time.sleep(1)
                    yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList
            temp = UnsortedList[i]
            UnsortedList[i] = UnsortedList[minNumberIndex]
            UnsortedList[minNumberIndex]=temp   
            time.sleep(1)
            yield '<script>document.getElementById("myContent").innerHTML=%s;</script>' % UnsortedList 


    if(flask.request.method == 'POST'):
        UnsortedList=flask.request.form['numbers'].split(',');
        UnsortedList = list(map(int, UnsortedList))
        if(flask.request.form['algorithm'] == 'Bubble Sort'):
            return flask.Response(bubbleSort(UnsortedList), mimetype='text/html')  
        elif(flask.request.form['algorithm'] == 'Insertion Sort'):
            return flask.Response(insertionSort(UnsortedList), mimetype='text/html') 
        elif(flask.request.form['algorithm'] == 'Selection Sort'):
            return flask.Response(selectionSort(UnsortedList), mimetype='text/html')
        elif(flask.request.form['algorithm'] == 'Quick Sort'):
            return flask.Response(quickSort(UnsortedList, 1), mimetype='text/html')  
    else:
        html="""<div style="width:100%" align="center"><h1>Bubble Sort, Quick Sort, Selection Sort and Insertion Sort</h1><form action="sort" method="POST">
    <input type="text" name="numbers"/>
    <select name="algorithm" id="algorithm">
        <option>Bubble Sort</option>
        <option>Selection Sort</option>
        <option>Insertion Sort</option>
        <option>Quick Sort</option>
    </select>
    <input type="submit" value="Submit"/>
</form></div>"""
        return flask.Response(html, mimetype='text/html')
	

	
if __name__ == "__main__":
    app.run(debug=True)
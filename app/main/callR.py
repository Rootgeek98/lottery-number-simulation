import io
import json
import random
import sys

import numpy
import pyRserve
from flask import request, render_template, send_file
from PIL import Image

from . import main
from . import model

rConn = pyRserve.connect(host='localhost', port=6311)

model = model.Lottery()

@main.route('/histogram/')
def serve_diagram():
    duration = request.args.get('duration')

    d = None
    if duration == '3m':
        d = '2017-02-01'
    elif duration == '6m':
        d = '2016-11-01'
    elif duration == '1y':
        d = '2016-05-01'
    elif duration == '2y':
        d = '2015-05-01'

    arr = None
    if duration == 'all':
        arr = [int(n.lstrip('0'), base=10) for row in model.getAllNumbers() for n in row]
    else:
        arr = [int(n.lstrip('0'), base=10) for row in model.getNumberAfter(d) for n in row]

    rConn.r.num = numpy.array(arr).astype(int)

    rawImage = rConn.r('drawHistogram(num)')

    stream = io.BytesIO(rawImage)

    img = Image.open(stream)

    imgIO = io.BytesIO()
    img.save(imgIO, 'PNG')
    imgIO.seek(0)

    return send_file(imgIO, mimetype='image/png')

@main.route('/event/')
def serve_event():
    duration = request.args.get('duration')

    d = None
    if duration == '3m':
        d = '2017-02-01'
    elif duration == '6m':
        d = '2016-11-01'
    elif duration == '1y':
        d = '2016-05-01'
    elif duration == '2y':
        d = '2015-05-01'

    arr = None
    if duration == 'all':
        arr = [[int(n.lstrip('0'), base=10) for n in row] for row in model.getAllNumbers()]
    else:
        arr = [[int(n.lstrip('0'), base=10) for n in row] for row in model.getNumberAfter(d)]

    rConn.r.num = numpy.array(arr)

    rawImage = rConn.r('drawEventDiagram(num)')

    stream = io.BytesIO(rawImage)

    img = Image.open(stream)

    imgIO = io.BytesIO()
    img.save(imgIO, 'PNG')
    imgIO.seek(0)

    return send_file(imgIO, mimetype='image/png')

@main.route('/random/', methods=['POST'])
def serve_random():
    numArray = rConn.r('predictByRandom()')
    arr = [int(n) for n in numArray]
    return json.dumps(arr)

@main.route('/high-freq/', methods=['POST'])
def serve_high_freq():
    duration = request.form.get('duration')

    # Re-implmenet it later.
    n = 0
    if duration == '3m':
        n = 13
    elif duration == '6m':
        n = 26
    elif duration == '1y':
        n = 52
    elif duration == '2y':
        n = 104
    elif duration == 'all':
        n = 156

    arr = []
    i = 0
    while i < n:
        j = 0
        row = []

        while j < 6:
            num = random.randint(1, 48)
            if num not in row:
                row.append(num)
                j = j + 1

        arr.append(row)
        i = i + 1

    rConn.r.num = numpy.array(arr)
    numArray = rConn.r('predictByHighFreq(num)')
    numArray = [int(n) for n in numArray]

    return json.dumps(numArray)

@main.route('/low-freq/', methods=['POST'])
def serve_low_freq():
    duration = request.form.get('duration')

    # Re-implmenet it later.
    n = 0
    if duration == '3m':
        n = 13
    elif duration == '6m':
        n = 26
    elif duration == '1y':
        n = 52
    elif duration == '2y':
        n = 104
    elif duration == 'all':
        n = 156

    arr = []
    i = 0
    while i < n:
        j = 0
        row = []

        while j < 6:
            num = random.randint(1, 48)
            if num not in row:
                row.append(num)
                j = j + 1

        arr.append(row)
        i = i + 1

    rConn.r.num = numpy.array(arr)
    numArray = rConn.r('predictByLowFreq(num)')
    numArray = [int(n) for n in numArray]

    return json.dumps(numArray)

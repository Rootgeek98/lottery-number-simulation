import io
import random

import numpy
import pyRserve
from flask import request, render_template, send_file
from PIL import Image

from . import main


rConn = pyRserve.connect(host='localhost', port=6311)



@main.route('/histogram/')
def serve_diagram():
    duration = request.args.get('duration')

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

        while j < 6:
            num = random.randint(1, 48)
            if num not in row:
                arr += num
                j = j + 1

        i = i + 1

    rConn.r.num = numpy.array(arr)

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
                row += num
                j = j + 1

        arr += row
        i = i + 1

    rConn.r.num = numpy.array(arr)

    rawImage = rConn.r('drawEventDiagram(num)')

    stream = io.BytesIO(rawImage)

    img = Image.open(stream)

    imgIO = io.BytesIO()
    img.save(imgIO, 'PNG')
    imgIO.seek(0)

    return send_file(imgIO, mimetype='image/png')

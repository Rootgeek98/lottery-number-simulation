import io
import numpy
import pyRserve
import random

from flask import render_template, send_file
from PIL import Image

from . import main


rConn = pyRserve.connect(host='localhost', port=6311)

@main.route('/histogram/')
def serve_diagram():
    rConn.r.num = numpy.array([random.randint(1, 48) for i in range(100)])

    rawImage = rConn.r('drawHistogram(num)')

    stream = io.BytesIO(rawImage)

    img = Image.open(stream)

    imgIO = io.BytesIO()
    img.save(imgIO, 'PNG')
    imgIO.seek(0)

    return send_file(imgIO, mimetype='image/png')

@main.route('/event/')
def serve_event():
    rConn.r.num = numpy.array([[random.randint(1, 48) for i in range(6)]
        for j in range(50)])

    rawImage = rConn.r('drawEventDiagram(num)')

    stream = io.BytesIO(rawImage)

    img = Image.open(stream)

    imgIO = io.BytesIO()
    img.save(imgIO, 'PNG')
    imgIO.seek(0)

    return send_file(imgIO, mimetype='image/png')

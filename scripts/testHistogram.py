import random
from PIL import Image
import io
import numpy
import pyRserve

rConn = pyRserve.connect(host='localhost', port=6311)

rConn.r.num = numpy.array([random.randint(1, 48) for i in range(100)])

rawImage = rConn.r('drawHistogram(num)')

stream = io.BytesIO(rawImage)

img = Image.open(stream)
img.save('output.png')

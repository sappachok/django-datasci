import random
import io
import urllib, base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64

numPts = 50
x = [random.random() for n in range(numPts)]
y = [random.random() for n in range(numPts)]
sz = 2 ** (10 * np.random.rand(numPts))

# plt.figure(figsize=(32, 18))

plt.scatter(x, y, s=sz, alpha=0.5)

fig = plt.gcf()
buf = io.BytesIO()
fig.savefig(buf, format='png')
buf.seek(0)
string = base64.b64encode(buf.read())
output = 'data:image/png;base64,' + urllib.parse.quote(string)
print(output)
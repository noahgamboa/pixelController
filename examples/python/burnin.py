#!/usr/bin/env python

# Burn-in test: Keep LEDs at full brightness most of the time, but dim periodically
# so it's clear when there's a problem.

import opc, time, math

numLEDs = 3*8*30
ADDRESS = '10.31.73.158:7890'
ADDRESS = 'localhost:7890'
client = opc.Client(ADDRESS)

# Test if it can connect (optional)
if client.can_connect():
    print('connected to %s' % ADDRESS)
else:
    # We could exit here, but instead let's just print a warning
    # and then keep trying to send pixels in case the server
    # appears later
    print('WARNING: could not connect to %s' % ADDRESS)
choose = 1
if choose == 0:
    t = 0
    while True:
        t += 0.4
        brightness = int(min(1, 1.25 + math.sin(t)) * 255)
        brightness2 = int(min(1, 1.25 + math.sin(3*t)) * 255)
        brightness3 = int(min(1, 1.25 + math.sin(2*t)) * 255)
        frame = [ (brightness3 , brightness2, brightness) ] * numLEDs
        client.put_pixels(frame)
        time.sleep(0.5)
        frame = [ (brightness3 , brightness2, 0) ] * numLEDs
        client.put_pixels(frame)
        time.sleep(0.5)
        frame = [ (brightness3 , 0, brightness) ] * numLEDs
        client.put_pixels(frame)
        time.sleep(0.5)
if choose == 1:
    colors = [(0,0,0)] * 23
    for i,e in enumerate(colors):
        color = i / 2
        if color == 0:
            colors[i] = (255, 0, 0)
        if color == 1:
            colors[i] = (255, 128, 0)
        if color == 2:
            colors[i] = (255, 255, 0)
        if color == 3:
            colors[i] = (128, 255, 0)
        if color == 4:
            colors[i] = (0, 255, 0)
        if color == 5:
            colors[i] = (0, 255, 128)
        if color == 6:
            colors[i] = (0, 255, 255)
        if color == 7:
            colors[i] = (0, 128, 255)
        if color == 8:
            colors[i] = (0, 0, 255)
        if color == 9:
            colors[i] = (128, 0, 255)
        if color == 10:
            colors[i] = (255, 0, 255)
        if color == 11:
            colors[i] = (255, 0, 127)

        r,g,b = colors[i]
        colors[i] = (r + 51 if r + 51 < 255 else 255, g + 51 if g + 51 < 255 else 255, b + 51 if b + 51 < 255 else 255)

        #colors[i] = (i*12 % 255, 0, i*6 % 255)
    pixels = [ (0,0,0) ] * numLEDs
    while True:
        for i in range(numLEDs):
            #pixels = [ (0,0,0) ] * numLEDs
            pixels[i] = colors[0]
            pixels[(i + 30) % numLEDs] = colors[1]
            pixels[(i + 60) % numLEDs] = colors[2]
            pixels[(i + 120) % numLEDs] = colors[3]
            pixels[(i + 150) % numLEDs] = colors[4]
            pixels[(i + 180) % numLEDs] = colors[5]
            pixels[(i + 210) % numLEDs] = colors[6]
            pixels[(i + 240) % numLEDs] = colors[7]
            pixels[(i + 270) % numLEDs] = colors[8]
            pixels[(i + 300) % numLEDs] = colors[9]
            pixels[(i + 330) % numLEDs] = colors[10]
            pixels[(i + 360) % numLEDs] = colors[11]
            pixels[(i + 390) % numLEDs] = colors[12]
            pixels[(i + 420) % numLEDs] = colors[13]
            pixels[(i + 450) % numLEDs] = colors[14]
            pixels[(i + 480) % numLEDs] = colors[15]
            pixels[(i + 510) % numLEDs] = colors[16]
            pixels[(i + 540) % numLEDs] = colors[17]
            pixels[(i + 570) % numLEDs] = colors[18]
            pixels[(i + 600) % numLEDs] = colors[19]
            pixels[(i + 630) % numLEDs] = colors[20]
            pixels[(i + 660) % numLEDs] = colors[21]
            pixels[(i + 690) % numLEDs] = colors[22]
            client.put_pixels(pixels)
            time.sleep(0.003)

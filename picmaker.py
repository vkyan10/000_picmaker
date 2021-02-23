file = open('pic.ppm', 'w')
file.write('P3 \n800 500 \n255\n')

for i in range(500):
    y = -(i-250)
    for j in range(800):
        x = j-400
        if y <= int(x/-5) - 315:
            file.write('255 0 0 ')  # lower left red corner
        elif 90*((x+90)**2) + (y-90)**2 <= 5000 and 450*((x+90)**2) + (y-90)**2 >= 4000:
            file.write('255 255 0 ')  # yellow ellipse
        elif 70*((x-120)**2) + (y-80)**2 <= 5000 and 300*((x-120)**2) + (y-80)**2 >= 4000:
            file.write('0 255 0 ')  # green ellipse
        elif x > -255 and x < 345 and y >= x/6 - 170 and y <= x/5.9 - 163:
            file.write('5 110 230 ')  # blue line
        elif y < -94 and y > -105 and y >= (x**3 - 25*(x**2))/1000 - 100 and y <= (x**3 - 25*(x**2))/1000 - 96:
            file.write('255 135 0 ')  # orange squiggly
        elif y > int(10 * x / 3 - 95):
            file.write('170 170 170 ')  # gray background
        else:
            file.write('255 0 0 ')  # red background
    file.write('\n')

file.close()

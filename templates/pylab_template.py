from pylab import *

# 1. Create input data
x = linspace(0, 10, 100)  # 100 points between 0 and 10
y = x                     # y = x

# 2. Plot the data
plot(x, y)                # draw a line graph of y = x

# 3. Add labels and title
xlabel("x values")        # label for x-axis
ylabel("y values")        # label for y-axis
title("Basic Line Plot")  # plot title

# 4. Show the plot
show()                    # display the graph window

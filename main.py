"""The main script which starts the ball clock working"""

from calculate import Clock

inputs = []
check_0 = True

while check_0:
  check_input = True
  while check_input:
    print("Enter number of balls in range 27-127:")
    num_balls = int(input())
    if num_balls == 0:
      check_0 = False
      check_input = False
    elif num_balls >= 27 and num_balls <= 127:
      inputs.append(num_balls)
      check_input = False
    else:
      print("Entered number of balls is not supported.")

for i in inputs:
  clocks = Clock(i)
  result_cycles = clocks.simulate()
  print("With number of balls: ", i)
  print("Cycles to revert in previous state: ", Clock.cycles_to_time(result_cycles))
  print("-------------------------------------")

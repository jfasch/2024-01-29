import sys
import uniq

input_list = [int(elem) for elem in sys.argv[1:]]

output_list = uniq.uniq(input_list)
for element in output_list:
    print(element)

from collections import OrderedDict
uniq_string = raw_input()
print "".join(OrderedDict.fromkeys(uniq_string))

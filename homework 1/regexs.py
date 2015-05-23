# #!/usr/bin/python
# import re
# import sys
#
# #print 'regex', sys.argv[1]
# #print 'files', sys.argv[2:]
#
# r = re.compile(sys.argv[1])
#
# for filename in sys.argv[2:]:
#     file = open(filename,'r')
#     for line in file.xreadlines():
#         m  = r.search(line)
#         if m:
#             print filename, "\t", line,
#!/usr/bin/python
import re
import sys
import os
import glob


print('regex', sys.argv[1])
print('hardcoding regex here!')
# sys.argv[1] = '[.ed|.ing|.ng|.ize]'
sys.argv[1] = ' [a-zA-Z]{20,} '
print('regex', sys.argv[1])


print('files', sys.argv[2:])
print('working dir - absolute = ' + os.path.abspath(sys.argv[2]))

r = re.compile(sys.argv[1])
print('***starts***')
for filename in glob.glob(sys.argv[2]):#sys.argv[2:]:
    print(filename)
    file = open(filename,'r')
    for line in file.readlines():
        #print('line', line.strip())
        m = r.search(line)
        #print(m)
        if m:# is not None:
            print('** ' ,filename, "\t", m.group(0), "\t", line)
        # print(filename, "\t", line)

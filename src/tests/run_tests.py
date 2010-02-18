#!/usr/bin/env python
import os
os.environ['PATH'] = ':'.join(['.', os.environ['PATH']])

tests = ['wtest',
         'ftest > ftest.dat && cmp ftest.dat ftestok.dat',
         'halftest']

if not os.environ.has_key('PRMAN_15_COMPATIBLE_PTEX'):
    tests.append('rtest > rtest.dat && cmp rtest.dat rtestok.dat')

failed = 0
for test in tests:
    print 'Running:', test
    status = os.system(test)
    if status != 0:
        print 'FAILED'
        failed += 1
    else:
        print 'Passed'
    print

print 'Finished', len(tests), 'tests,'
if failed == 0:
    print 'All tests passed'
else:
    print failed, 'tests FAILED'
    exit(1)

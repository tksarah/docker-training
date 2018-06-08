import os
print '***** Docker Secrets ******'
print 'USERNAME: {0}'.format(os.environ['USERNAME'])
fname = os.environ['PASSWORD_FILE']
with open(fname) as f:
  content = f.readlines()
print 'PASSWORD_FILE: {0}'.format(fname)
print 'PASSWORD: {0}'.format(content[0])

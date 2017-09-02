#https://martin-thoma.com/configuration-files-in-python/
import myconfig1 as cfg

# print cfg.mysql['host']
# print cfg.mysql['db']
# print cfg.mysql['user']
# print cfg.mysql['password']

print 'Here we get the configuration content:'
print 'Host:{}, db Name:{}, user:{}, pass word:{}'.format(cfg.mysql['host'],cfg.mysql['db'],cfg.mysql['user'],cfg.mysql['passwd'])
print 'all user anonymous:{}'.format(cfg.use_anonymous)

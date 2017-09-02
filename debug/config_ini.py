import ConfigParser
import io

#load the configration file
file_name='config.ini'
with open(file_name) as f:
    ini_conf=f.read()
config=ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(ini_conf))

# #List all contents
# print 'list all contents'
# for section in config.sections():
#     print 'Section : %s '  % section
#     for options in config.options(section):
#         print "Options:{}, Optoin Values:{}, type:{}".format(options,config.get(section,options),
#                         str(type(options)))

#print some contents
print '\n Print some contents for samples'
print config.get('other','use_anonymous')
print config.get('mysql','db')


#add or set the config property.
config.set('mysql', 'host', 'my customerlocalhost')
config.set('mysql', 'add_element', 'element one&one')
print config.get('mysql','host')
print config.get('mysql','add_element')

import yaml


f = open('./params.yaml', 'r')
params = yaml.load(f, Loader=yaml.SafeLoader)
f.close()

model = params['MODEL']

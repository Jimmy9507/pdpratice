import yaml
def default_conf():
    import os
    return os.path.join(os.path.dirname(__file__),'PlotterConfig.yaml')

def default_color_conf():
    import os
    return os.path.join(os.path.dirname(__file__),'PlotterConfig.yaml')

class PlotterConfig:
    def __init__(self,config_file=None):
        if config_file is None:
            config_file=default_conf()
        self._conf=yaml.load(open(config_file,"r"))

    def get(self,path):
        conf=self._conf
        elements=path.split('.')
        for i in range(len(elements)):
            conf=conf[elements[i]]
        return conf

class ColorConfig:
    def __init__(self,config_file=None):
        if config_file is None:
            config_file=default_conf()
        self._conf=yaml.load(open(config_file,"r"))

    def get(self,path):
        elements=path.split('.')
        conf=self._conf
        for i in range(len(elements)):
            conf=conf[elements[i]]
        return conf
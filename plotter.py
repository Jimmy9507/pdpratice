from bokeh.plotting import figure,ColumnDataSource
from plotter_config import PlotterConfig,ColorConfig
from bokeh.models import *


_conf=None
_color_conf=None

def get_conf():
    global _conf
    if _conf is not None:
        return _conf
    _conf=PlotterConfig()
    return _conf

def get_color_conf():
    global _color_conf
    if _color_conf is not None:
        return _color_conf
    _color_conf=ColorConfig()
    return _color_conf

def set_axises(p,yaxis_label=None,yaxis_formatter=None,xaxis_label=None,
               xaxis_formatter=None,yaxis_label_text_font_style=None):
    p.yaxis.axis_label=yaxis_label
    p.xaxis.axis_label=xaxis_label
    p.yaxis.axis_label_text_font_style=yaxis_label_text_font_style
    p.xaxis.axis_line_alpha=p.yaxis.axis_line_alpha=0
    p.xaxis.minor_tick_line_alpha=p.yaxis.minor_tick_line_alpha=0
    p.xaxis.major_tick_line_alpha=p.yaxis.major_tick_line_alpha=0.1
    if yaxis_formatter is not None:
        p.yaxis.formatter=yaxis_formatter
    if xaxis_formatter is not None:
        p.xaxis.formatter=xaxis_formatter
    p. add_tools(CrosshairTool())
    return p
# 折线图
def line_graph_plot(returns,y_axis_type='linear',mark='plot_1'):
    _conf=get_conf()
    _color_conf=get_color_conf()
    p=figure(title=_conf.get('%s.title'%mark),width=_conf.get('%s.width'%mark),
             height=_conf.get('%s.height'%mark),x_axis_type='datetime',y_axis_type=y_axis_type)

    source=ColumnDataSource(data=dict(returns_index=returns.index,returns=returns))

    #cum_render=p.line('return_index','returns',color=_color_conf.get('%s.color' % mark),line_width=2,line_join='round',source=source)

    return set_axises(p,yaxis_formatter=NumeralTickFormatter(format='0%'),
                      xaxis_formatter=DatetimeTickFormatter(months='%Y-%m'))


def distagram_graph_plot():
    pass


def heatmap_graph_plot():
    pass
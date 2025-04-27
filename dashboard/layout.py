from dash import html, dcc    # ✅ 加上 dcc
from dashboard.charts import generate_bar_chart
from dashboard.table import generate_table

# 初始数据
initial_data = [
    {"项目名称": "水果分拣", "采集时间": "2025.04.03-2025.04.20", "采集数量": "23618", "状态": "已完成", "上传": "进行中"},
    {"项目名称": "扫码枪扫货", "采集时间": "2025.04.21-2025.04.22", "采集数量": "6792", "状态": "已完成", "上传": "进行中"},
    {"项目名称": "桌面垃圾清理", "采集时间": "2025.04.23-2025.04.25", "采集数量": "4727", "状态": "进行中", "上传": "进行中"},
]

layout = html.Div([
    html.Div(id='chart-container', children=[generate_bar_chart(initial_data)]),
    html.Hr(),
    html.Div(id='table-container', children=[generate_table(initial_data)]),
    dcc.Store(id='stored-data', data=initial_data),
])

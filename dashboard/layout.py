from dash import dcc, html, dash_table
import pandas as pd

# 初始数据
initial_data = [
    {"项目名称": "水果分拣 (fruit sort)", "采集时间": "2025.04.03-2025.04.20", "采集数量": 23618, "状态": "已完成"},
    {"项目名称": "扫码枪扫货 (scanning gun)", "采集时间": "2025.04.21-2025.04.22", "采集数量": 6792, "状态": "已完成"},
    {"项目名称": "桌面垃圾清理 (cleaning)", "采集时间": "2025.04.23-", "采集数量": 1111, "状态": "进行中"},
]

df = pd.DataFrame(initial_data)

layout = html.Div([
    dcc.Store(id='stored-data', data=initial_data),

    html.H1("智元A2 项目看板", className="title"),

    html.Div([
        html.Button("➕ 添加新行", id="add-row-btn", n_clicks=0, className="add-btn"),
    ], className="button-area"),

    html.Div([
        dcc.Graph(id="bar-chart"),
    ], className="chart-area"),

    html.Div([
        dash_table.DataTable(
            id='data-table',
            columns=[
                {"name": "项目名称", "id": "项目名称", "editable": True},
                {"name": "采集时间", "id": "采集时间", "editable": True},
                {"name": "采集数量", "id": "采集数量", "editable": True, "type": "numeric"},
                {"name": "状态", "id": "状态", "editable": True},
                {"name": "操作", "id": "操作", "presentation": "markdown"}
            ],
            style_table={"overflowX": "auto"},
            style_cell={
                "textAlign": "left",
                "padding": "10px",
                "backgroundColor": "rgba(0,0,0,0.3)",
                "color": "#FFFFFF",
                "border": "1px solid #444"
            },
            style_header={
                "backgroundColor": "rgba(255,255,255,0.1)",
                "fontWeight": "bold",
                "color": "#00FFFF"
            },
            row_deletable=False,
            editable=True,
            markdown_options={"html": True},
            page_size=10
        )
    ], className="table-area")
], className="container")

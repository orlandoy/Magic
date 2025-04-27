from dash import dash_table, dcc, html

columns = [
    {'name': '项目名称', 'id': '项目名称', 'editable': True},
    {'name': '采集时间', 'id': '采集时间', 'editable': True},
    {'name': '采集数量', 'id': '采集数量', 'editable': True},
    {'name': '状态', 'id': '状态', 'editable': True},
    {'name': '上传', 'id': '上传', 'editable': True},
]

def generate_table(data):
    return html.Div([
        html.Button('➕ 添加新行', id='add-row-btn', n_clicks=0, className="add-btn"),
        dash_table.DataTable(
            id='data-table',
            columns=columns,
            data=data,
            editable=True,
            row_deletable=True,
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'center', 'padding': '5px'},
            style_header={'backgroundColor': '#3498db', 'color': 'white', 'fontWeight': 'bold'},
        )
    ])

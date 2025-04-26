from dash import Dash, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from dashboard.layout import layout
from dashboard.charts import generate_bar_chart
from dashboard.table import generate_table

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "动态增删改查 Dash 示例"
app.layout = layout

# 更新图表和表格
@app.callback(
    Output('chart-container', 'children'),
    Output('table-container', 'children'),
    Output('stored-data', 'data'),
    Input('data-table', 'data'),
    Input('add-row-btn', 'n_clicks'),
    State('stored-data', 'data'),
)
def update_output(table_data, n_clicks, stored_data):
    trigger = ctx.triggered_id

    if trigger == 'add-row-btn':
        stored_data.append({"项目名称": "", "采集时间": "", "采集数量": "0", "状态": "", "上传": ""})
    else:
        stored_data = table_data

    return generate_bar_chart(stored_data), generate_table(stored_data), stored_data
if __name__ == "__main__":
    app.run(debug=True)

import dash_echarts

def generate_bar_chart(data):
    x_data = [row['项目名称'] for row in data]
    y_data = [int(row['采集数量']) if row['采集数量'] else 0 for row in data]

    option = {
        "xAxis": {
            "type": "category",
            "data": x_data,
            "axisLabel": {"rotate": 45}
        },
        "yAxis": {"type": "value"},
        "series": [{
            "data": y_data,
            "type": "bar",
            "itemStyle": {"color": "#4CAF50"}
        }]
    }

    return dash_echarts.DashECharts(
        option=option,
        style={"height": "400px", "width": "100%"},
        id='bar-chart'
    )

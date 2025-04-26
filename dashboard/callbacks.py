from dash import Output, Input, State, callback
import dash_table
import pandas as pd
import plotly.graph_objects as go

@callback(
    Output('data-table', 'data'),
    Input('add-row-btn', 'n_clicks'),
    State('data-table', 'data'),
    prevent_initial_call=True
)
def add_row(n_clicks, data):
    data.append({"项目名称": "", "采集时间": "", "采集数量": 0, "状态": "", "操作": ""})
    return data

@callback(
    Output('data-table', 'data'),
    Input('data-table', 'active_cell'),
    State('data-table', 'data'),
    prevent_initial_call=True
)
def delete_row(active_cell, data):
    if active_cell and active_cell['column_id'] == '操作':
        data.pop(active_cell['row'])
    return data

@callback(
    Output('bar-chart', 'figure'),
    Input('data-table', 'data')
)
def update_bar_chart(data):
    df = pd.DataFrame(data)
    if df.empty:
        return go.Figure()

    fig = go.Figure()

    for status in df['状态'].unique():
        filtered = df[df['状态'] == status]
        fig.add_trace(go.Bar(
            x=filtered['项目名称'],
            y=filtered['采集数量'],
            name=status,
            marker=dict(line=dict(width=1)),
            hoverinfo='x+y'
        ))

    fig.update_layout(
        plot_bgcolor="#0F0F0F",
        paper_bgcolor="#0F0F0F",
        font=dict(color="#00FFFF", family="Orbitron, Roboto"),
        xaxis=dict(gridcolor="#333"),
        yaxis=dict(gridcolor="#333"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#FFFFFF")),
        margin=dict(t=40, l=40, r=40, b=40)
    )
    return fig

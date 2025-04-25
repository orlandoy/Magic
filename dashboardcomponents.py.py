from dash import html, dash_table, dcc
import plotly.graph_objects as go
from dashboard.color_scheme import COLOR_SCHEME
import pandas as pd

def create_project_card(project):
    return html.Div([
        html.Img(src=project["图片"], style={
            "width": "100%", "height": "180px", "objectFit": "cover",
            "borderRadius": "12px"
        }),
        html.H3(project["项目名称"], style={"color": COLOR_SCHEME["text"], "marginTop": "12px"}),
        html.P(f"{project['采集时间']} | 状态: {project['状态']} | 数量: {project['采集数量']}", style={
            "color": COLOR_SCHEME["highlight"]
        })
    ], style={
        "backgroundColor": COLOR_SCHEME["card"],
        "padding": "16px",
        "borderRadius": "16px",
        "boxShadow": "0 6px 16px rgba(0,0,0,0.3)",
        "margin": "10px",
        "width": "280px"
    })

def create_summary_card(title, value, icon, color):
    return html.Div(
        style={
            "backgroundColor": COLOR_SCHEME["card"],
            "borderRadius": "16px",
            "padding": "20px",
            "boxShadow": "0 8px 20px rgba(0,0,0,0.3)",
            "margin": "10px",
            "flex": 1,
            "minWidth": "220px"
        },
        children=[
            html.Div([
                html.I(className=f"fas fa-{icon}", style={"color": color, "fontSize": "26px"}),
                html.H3(title, style={"marginLeft": "12px", "color": COLOR_SCHEME["text"]})
            ], style={"display": "flex", "alignItems": "center"}),
            html.H2(f"{value:,}", style={"color": color, "marginTop": "10px", "fontSize": "30px"})
        ]
    )

def create_bar_chart(df):
    fig = go.Figure()
    for status in df["状态"].unique():
        sub = df[df["状态"] == status]
        fig.add_trace(go.Bar(
            x=sub["项目名称"],
            y=sub["采集数量"],
            name=status,
            marker=dict(color=COLOR_SCHEME[status][0], line=dict(color=COLOR_SCHEME[status][1], width=2.5)),
            text=[f"{x:,}" for x in sub["采集数量"]],
            textposition="outside",
            opacity=0.95
        ))

    avg = df["采集数量"].mean()
    fig.add_hline(y=avg, line_dash="dot", line_color="#BDC3C7",
                  annotation_text=f"平均值: {avg:,.0f}",
                  annotation_font_color=COLOR_SCHEME["text"])

    fig.update_layout(
        plot_bgcolor=COLOR_SCHEME["card"],
        paper_bgcolor=COLOR_SCHEME["background"],
        font=dict(family="Roboto", size=13, color=COLOR_SCHEME["text"]),
        xaxis=dict(tickangle=-20, gridcolor="#34495E"),
        yaxis=dict(gridcolor="#34495E", tickformat=","),
        margin=dict(t=40),
        transition={"duration": 500},
        legend=dict(orientation="h", y=1.1, font=dict(color=COLOR_SCHEME["text"]))
    )
    return fig

def create_data_table(df):
    return dash_table.DataTable(
        id="data-table",
        columns=[
            {"name": "项目名称", "id": "项目名称"},
            {"name": "采集时间", "id": "采集时间"},
            {"name": "采集数量", "id": "采集数量"},
            {"name": "状态", "id": "状态"},
            {"name": "上传", "id": "上传"}
        ],
        data=df.to_dict("records"),
        style_table={"overflowX": "auto", "borderRadius": "12px"},
        style_header={
            "backgroundColor": COLOR_SCHEME["highlight"],
            "color": "white", "fontWeight": "bold", "fontSize": "16px"
        },
        style_cell={
            "textAlign": "left", "padding": "14px", "fontFamily": "Roboto",
            "backgroundColor": COLOR_SCHEME["card"], "color": COLOR_SCHEME["text"]
        },
        style_data_conditional=[
            {"if": {"row_index": "odd"}, "backgroundColor": "#243447"},
            {"if": {"filter_query": "{状态} = '已完成'"}, "color": COLOR_SCHEME["已完成"][0]},
            {"if": {"filter_query": "{状态} = '进行中'"}, "color": COLOR_SCHEME["进行中"][0]}
        ],
        filter_action="native", sort_action="native", page_size=10, style_as_list_view=True
    )


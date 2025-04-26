# dashboard/callbacks.py

from dash import Input, Output, State, callback, ctx
from .charts import create_chart_figure
from .table import generate_table_data
from .image import get_image_src

def register_callbacks(app):
    @app.callback(
        Output('main-chart', 'figure'),
        Input('chart-dropdown', 'value')
    )
    def update_chart(selected_value):
        if not selected_value:
            return create_chart_figure(default=True)
        return create_chart_figure(selected_value)

    @app.callback(
        Output('data-table', 'data'),
        Input('refresh-table-button', 'n_clicks'),
        prevent_initial_call=True
    )
    def refresh_table(n_clicks):
        return generate_table_data()

    @app.callback(
        Output('project-image', 'src'),
        Input('image-dropdown', 'value')
    )
    def update_image(selected_image):
        if not selected_image:
            return get_image_src(default=True)
        return get_image_src(selected_image)

    @app.callback(
        Output('notification', 'children'),
        Input('main-chart', 'clickData'),
        prevent_initial_call=True
    )
    def show_click_notification(click_data):
        if click_data:
            point_info = click_data['points'][0]
            return f"您点击了：{point_info['label']} - {point_info['value']}"
        return ""


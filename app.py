from dash import Dash
from dashboard.layout import layout
from dashboard.callbacks import register_callbacks

app = Dash(__name__, external_stylesheets=["/assets/style.css"])
app.title = "智元A2项目看板"
app.layout = layout

register_callbacks(app)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=True)

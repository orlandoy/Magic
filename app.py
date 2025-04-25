from dashboard.layout import create_layout
from data.manager import load_projects
from dashboard.color_scheme import COLOR_SCHEME
import dash

app = dash.Dash(__name__, external_stylesheets=[
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css',
    'https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap'
])
app.title = "智元A2项目"

projects = load_projects()
app.layout = create_layout(projects)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=True, host="0.0.0.0", port=port)


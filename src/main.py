from falcon import App

from search import Search

app = App()
app.add_route("/search", Search())

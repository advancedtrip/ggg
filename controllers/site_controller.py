from views.view import View


class SiteController:
    def __init__(self):
        self.layout="default"
        self.view=View(self.layout)


    def index(self, request, response):
        response.text = self.view.render_html(
            'site/index.html', {'title': 'MVC фрамеворке', 'h1': 'Главная страница'}
        )



    def about(self, request, response):
        response.text = self.view.render_html(
            'site/about.html', {'title': 'MVC фрамеворке - о  нас', 'h1': 'Cтраница о нас'}
        )

    def hello(self, request, response):
        response.text = self.view.render_html('site/hello.html', {'title': 'helloPage', 'h1': 'hello', 'user': user_name})

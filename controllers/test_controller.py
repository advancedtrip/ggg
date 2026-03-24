from views.view import View


class TestController:
    def __init__(self):
        self.layout="default"
        self.view=View(self.layout)


    def test(self, request, response):
        response.text = self.view.render_html(
            'test/test.html', {'title': 'MVC фрамеворке', 'h1': 'Тестовая страница'}
        )



    def test_action(self, request, response):
        response.text = self.view.render_html(
            'test/action.html', {'title': 'MVC фрамеворке - о  нас', 'h1': 'Информация о действии'}
        )
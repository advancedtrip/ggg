from controllers.site_controller import SiteController
from controllers.test_controller import TestController

routes = {
    r"^/home/(.*)$": [SiteController, SiteController.index],
    '/about': [SiteController, SiteController.about],
    '/test-action': [TestController, TestController.test_action],
    '/test': [TestController, TestController.test],
    r"^/hello/(.*)$": [SiteController, SiteController.index]
    # '/articles': articles,
}

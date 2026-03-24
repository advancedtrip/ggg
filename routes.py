from controllers.site_controller import SiteController
from controllers.test_controller import TestController

routes = {
    '/home': [SiteController, SiteController.index],
    '/about': [SiteController, SiteController.about],
    '/test-action': [TestController, TestController.test_action],
    '/test': [TestController, TestController.test],

    # '/articles': articles,
}

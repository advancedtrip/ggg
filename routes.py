from controllers.site_controller import SiteController

site_controller = SiteController()

routes = {
    '/home': site_controller.index,
    '/about': site_controller.about,
    # '/articles': articles,
}

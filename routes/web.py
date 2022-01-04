from masonite.routes import Route

ROUTES = [
    Route.get("/", "HomeController@home"),
    Route.get("/faq", "HomeController@faq"),
    # packages handling
    Route.get("/packages", "PackagesController@index").name("packages"),
    Route.get("/packages/@slug", "PackagesController@details").name("packages.details"),
]

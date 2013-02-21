class __Routes:
    __routes = []
    @classmethod
    def Routes(self, routes):
        print "HERERERE"
        print "Routes", routes
        self.__routes += routes
        print "server.Route", self.__routes

    @classmethod
    def getRoutes(self):
        return self.__routes

# public function for import
Routes = __Routes.Routes
routes = __Routes.getRoutes

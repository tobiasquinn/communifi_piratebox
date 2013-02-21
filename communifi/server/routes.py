class __Routes:
    __routes = []
    @classmethod
    def Routes(self, routes):
        self.__routes += routes

    @classmethod
    def getRoutes(self):
        return self.__routes

# public function for import
Routes = __Routes.Routes
routes = __Routes.getRoutes

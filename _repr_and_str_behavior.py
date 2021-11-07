class Navigator(): 
      _args = []

    def __init__(self):
      super(Navigator, self).__init__()
       #super(Navigator, self).__init__()


  
  def __str__(self):
        return '{}({})'.format(type(self).__name__, ', '.join(repr(getattr(self, a)) for a in self._args)) ## guidelines for repr 

       # return self.__stringify(str)

    def __repr__(self):
       #return self.__stringify(repr)
        return '{}({})'.format(type(self).__name__,
                               ', '.join(str(getattr(self, a)) for a in self._args))

      

import UnitOP

class Mixer(UnitOP.UnitOP):
    def __init__(self,**kwargs):
        super(Mixer, self).__init__(**kwargs)
        self.size2 = (60, 115.75)
        self.size = (52, 87)
        self.background_normal = 'Mixer1.png'
        self.PropertyList = ['INPUT 1','INPUT 2','OUTPUT']
        self.connected_to = []
        self.Connecting_Points = []
        self.line_nos = []
        self.OM_Model = 'Mixer'
        self.PropertyVal = ['', '', '']

    def Update_Conn_Pnts(self):
        self.Connecting_Points = [[self.x, self.y + 4], [self.x, self.y + 83], [self.x + 52, self.y + (87 / 2)]]

    def on_submit(self, instance):
        self.Connecting_Points = [[self.x, self.y + 4], [self.x, self.y + 83], [self.x + 52, self.y + (87 / 2)]]
        self.name = self.name_ob.text
        self.text_label.text = self.name
        UnitOP.UnitOP.drop_connections[self.name] = UnitOP.UnitOP.drop_connections[self.bef_name]
        for Property in self.MainButton:
            self.connected_to.append(self.drop_connections[Property.text])
            self.PropertyVal.append(self.drop_connections[Property.text])
            print self.connected_to
        if self.connected == False:
            self.connect = self.connect + 1






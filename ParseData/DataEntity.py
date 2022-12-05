
class DataEntity:
    def __init__(self, datalist):
        self.year = int(datalist[0])
        self.month = int(datalist[1])
        self.day = int(datalist[2])
        self.hour = int(datalist[3])
        self.minute = int(datalist[4])
        self.second = int(datalist[5])
        self.citycode=datalist[6]
        self.province = datalist[7]
        self.city = datalist[8]
        self.stationid = datalist[9]
        self.longitude = float(datalist[10])
        self.latitude = float(datalist[11])
        self.PMvalue = int(datalist[12])

    def print(self):
        print('year:{},month:{},day:{},hour:{},minute:{},second:{},citycode:{},province:{},city:{},stationid:{},longitude:{},' \
              'latitude:{},PM:{}'.format(self.year, self.month, self.day, self.hour, self.minute, self.second,self.citycode,
                                         self.province, self.city, self.stationid, self.longitude,
                                         self.latitude, self.PMvalue))

    def __str__(self):
        return  'year:{},month:{},day:{},hour:{},minute:{},second:{},citycode:{},province:{},city:{},stationid:{},longitude:{},' \
              'latitude:{},PM:{}'.format(self.year, self.month, self.day, self.hour, self.minute, self.second,self.citycode,
                                         self.province, self.city, self.stationid, self.longitude,
                                         self.latitude, self.PMvalue)

    # year = 0, day = 0, month = 0, hour = 0, minute = 0, second = 0, province = '', city = '', stationid = '', longitude = 0, latitude = 0, pm = 0

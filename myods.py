# -*- coding: utf-8 -*-
import collections
from odslib import ODS

class stigma():
    """A gps point class"""
    def __init__(self, id, valid, time, latitude, longtitude, altitude, speed, course, power,address):
        self.id = id
        self.valid = valid
        self.time = time
        self.latitude = latitude
        self.longtitude = longtitude
        self.altitude = altitude
        self.speed = speed
        self.course = course
        self.power = power
        self.address = address

class myroute():
    """A route class"""
    def __init__(self, device_name, startdate, enddate, route_length, points):
        self.ods = ODS()
        self.device_name=device_name
        self.startdate=startdate
        self.enddate=enddate
        self.route_length=route_length
        self.points=points
        
        # sheet title
        sheet = self.ods.content.getSheet(0)
        sheet.setSheetName(self.device_name)
        # title
        sheet.getCell(0, 0).stringValue(u"Συσκευή").setFontSize('12pt').setBold(True)
        sheet.getCell(1, 0).stringValue(self.device_name).setFontSize('12pt').setBold(True)
        sheet.getRow(0).setHeight('18pt')
        #sheet.getColumn(0).setWidth('10cm')

        # Start date
        cell =sheet.getCell(0, 1).stringValue(u"Από:").setAlignHorizontal("right")
        sheet.getCell(1, 1).stringValue(self.startdate).setAlignHorizontal("right")
        #cell.setAlignHorizontal("right")

        # End date
        sheet.getCell(0, 2).stringValue(u"Εώς:").setAlignHorizontal("right")
        sheet.getCell(1, 2).stringValue(self.enddate).setAlignHorizontal("right")

        # Route Length 
        sheet.getCell(0, 3).stringValue(u"Μήκος διαδρομής (km):").setAlignHorizontal("right")
        sheet.getCell(1, 3).floatValue(self.route_length).setAlignHorizontal("right")
        
        # Label for point s 
        sheet.getCell(0, 5).stringValue(u'Δεδομένα στιγμάτων').setAlignHorizontal("right")

        # Headers for points
        settings_header_points=(("id", "left"),
                                ("Valid", "left"),
                                ("Time","left"),
                                ("Latitude","left"),
                                ("Longitude","left"),
                                ("Altitude","left"),
                                ("Speed","left"),
                                ("Course","left"),
                                ("Power","left"),
                                ("Altitude","left"))

        settings = collections.OrderedDict(settings_header_points)
        row = 6  # row of the headers for points
        index = 0
        for k, v in settings_header_points:
            # set header value and alignment
            sheet.getCell(index, row).stringValue(k).setAlignHorizontal(v)
            index += 1

        self.rowoffset = 8 # row offset from top (0)
        for (index, point) in enumerate(self.points):
            row=index+self.rowoffset  # row to write
            cellvalues= [point.id,
                         point.valid,
                         point.time,
                         point.latitude,
                         point.longtitude,
                         point.altitude,
                         point.speed,
                         point.course,
                         point.power,
                         point.address
                         ]
            for (i, value) in enumerate(cellvalues):
                # set value (i=cell)
                sheet.getCell(i, row).stringValue(value).setAlignHorizontal("left")

    def save(self, path):
        """Save save ods object on disk"""
        self.ods.save(path)

    def __setcellvalue(self):
        """Private method to set cell value"""
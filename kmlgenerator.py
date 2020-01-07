# -*- coding: utf-8 -*-
from lxml import etree
from pykml.factory import KML_ElementMaker as KML


class Position():
    def __init__(self,name,lat,lon,altitude,timestamp):
        self.name=name
        self.lat=lat
        self.lon=lon
        self.altitude=altitude
        self.timestamp=timestamp


class kmlobj():

    def __init__(self,positions):
        self.positions=positions #list with Position objects
        doc = KML.kml(
        KML.Document(
        KML.Folder(
        KML.name(u"Στίγματα"),



        KML.Style(
             KML.IconStyle(
                    KML.Icon(
                        KML.href('http://maps.google.com/mapfiles/kml/paddle/A.png')
                    )
             ),

             id = 'paddle-a'
),#End of Style



        KML.Style(
           KML.IconStyle(
                    KML.Icon(
                        KML.href('http://maps.google.com/mapfiles/kml/paddle/B.png')
                            )
                        ),
             id = 'paddle-b'
        ),#End of Style


        KML.Style(
           KML.IconStyle(
                    KML.Icon(
                        KML.href('http://maps.google.com/mapfiles/ms/icons/hiker.png')
                            )
                        ),
             id = 'hiker-icon'
        ),#End of Style


            *[
                KML.Placemark(
                    KML.name(position.name),
                    KML.TimeStamp(
                                 KML.when(position.timestamp)
                                 ),
                    KML.styleUrl("#hiker-icon"),
                    KML.Point(
                        KML.coordinates('%s,%s,%s' % (position.lat,position.lon,position.altitude))
                    )
                ) for position in positions
            ]


    )#End of Folder
    )#End of doc
    )#End of kml

        self.kmlobj=etree.tostring(doc, pretty_print=True)
        #return etree.tostring(doc, pretty_print=True)

    def writekml2disk(self,path):
        f = open(path,"w") #opens filewith write mode
        f.write(self.kmlobj)
        f.close()
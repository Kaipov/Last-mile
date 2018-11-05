from __future__ import print_function

import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

api_instance = swagger_client.MatrixApi()
KEY = 'd297f285-9782-4f17-990a-fe9f0e71757c'  # str | Get your key at graphhopper.com

#POINT = ['34.225239,-118.441814',
#         '34.149773,-118.595022',
#         '34.251001,-118.586668',
#         '34.230391,-118.582597']

OUT_ARRAY = ['distances', 'times']
VEHICLE = 'car'


def dist_matr():
    pts_f = open("Data/geo100.txt", "r")
    l = pts_f.readline()[:-1]

    point = []

    while l:
        point.append(str(l))
        l = pts_f.readline()[:-1]

    pts_f.close()

    try:
        # Matrix API
        api_response = api_instance.matrix_get(KEY, point=point, out_array=OUT_ARRAY, vehicle=VEHICLE)
        if api_response.distances is not None:
            #f = open("Data/matr.out", "w")
            f = open("Data/times", "w")
            for t in api_response.distances:
                f.write(str(t))
            f.close()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MatrixApi->matrix_get: %s\n" % e)


dist_matr()


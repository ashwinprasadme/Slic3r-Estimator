#!/usr/bin/env python
import os, sys
from settings import APP_STATIC,APP_UPLOAD,APP_SLIC3R
from subprocess import call, Popen
import gcoder
import rounder
import time
import send_email

#system arguments
UPLOAD_FOLDER = APP_UPLOAD
def start_slice(name, email, filename, quality, speed, support, order_id):
    #name, email, filename, quality, speed, support

    #Construct Command
    slicer_settings = [os.path.join(APP_SLIC3R, "./slic3r"),"--load","cfg.ini",os.path.join(UPLOAD_FOLDER, filename)]
    #From Form
    slicer_settings.append("--layer-height")
    slicer_settings.append(quality)
    slicer_settings.append("--infill-speed")
    slicer_settings.append(speed)
    print support
    if support == 'Yes' :
        slicer_settings.append("--support-material")


    #Slic3r from filename
    print slicer_settings

    slicer = call(slicer_settings) #Blocking
    print "\n"

    first, file_extension = os.path.splitext(filename)
    gcode_Sliced = first + '.gcode'

    print gcode_Sliced

    fname = os.path.join(UPLOAD_FOLDER, gcode_Sliced)

    # Gcode file analysis
    gcode = gcoder.GCode(open(fname, "rU"))
    print gcode

    print "Dimensions:"
    xdims = (gcode.xmin, gcode.xmax, gcode.width)
    print "\tX: %0.02f - %0.02f (%0.02f)" % xdims
    ydims = (gcode.ymin, gcode.ymax, gcode.depth)
    print "\tY: %0.02f - %0.02f (%0.02f)" % ydims
    zdims = (gcode.zmin, gcode.zmax, gcode.height)
    print "\tZ: %0.02f - %0.02f (%0.02f)" % zdims
    print "Filament used: %0.02fmm" % gcode.filament_length
    print "Number of layers: %d" % gcode.layers_count
    print "Estimated duration: %s" % gcode.estimate_duration()[1]
    print "Estimated duration Hours: %s" % gcode.duration_hours
    #round to 0.5
    dur_in_hours = rounder.round_to_5(gcode.duration_hours)
    if dur_in_hours == 0:
        dur_in_hours = 0.5
    #Multiply per hour cost
    cost = dur_in_hours*300
    print "\n"

    # Mail
    send_email.send_estimation(email,gcode.estimate_duration()[1],cost,name,filename,order_id)

if __name__ == "__main__":
    #name, email, filename, quality, speed, support
   start_slice(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])

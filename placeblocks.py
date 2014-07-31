import mcpi.minecraft as minecraft
import mcpi.block as block
#import datapoint_access as dba
import json
import urllib2
import time

def placeRain(mc, pos):
	mc.setBlock(pos.x-1,pos.y+5,pos.z, block.DIAMOND_BLOCK)
	mc.setBlock(pos.x,pos.y+5,pos.z, block.DIAMOND_BLOCK)	

def placeSun(mc, pos):
	mc.setBlock(pos.x,pos.y+5,pos.z, block.GOLD_BLOCK)
        mc.setBlock(pos.x+1,pos.y+6,pos.z, block.GOLD_BLOCK)
        mc.setBlock(pos.x,pos.y+7,pos.z, block.GOLD_BLOCK)
        mc.setBlock(pos.x-1,pos.y+6,pos.z, block.GOLD_BLOCK)
        mc.setBlock(pos.x,pos.y+6,pos.z, block.GOLD_BLOCK)
  
def placelighting(mc, pos):
        mc.setBlock(pos.x,pos.y+7,pos.z, block.GLOWSTONE_BLOCK)
        mc.setBlock(pos.x,pos.y+6,pos.z, block.GLOWSTONE_BLOCK)
        mc.setBlock(pos.x-1,pos.y+6,pos.z, block.GLOWSTONE_BLOCK)
        mc.setBlock(pos.x-1,pos.y+5,pos.z, block.GLOWSTONE_BLOCK)
      
def placesnow(mc, pos):
	#bottom row
        mc.setBlock(pos.x-2,pos.y+5,pos.z, block.SNOW_BLOCK)
        mc.setBlock(pos.x+3,pos.y+5,pos.z, block.SNOW_BLOCK)
        # row 2
	mc.setBlock(pos.x-1,pos.y+6,pos.z, block.SNOW_BLOCK)
        mc.setBlock(pos.x+2,pos.y+6,pos.z, block.SNOW_BLOCK)
        # row 3
        mc.setBlock(pos.x,pos.y+7,pos.z, block.SNOW_BLOCK)   
        mc.setBlock(pos.x+1,pos.y+7,pos.z, block.SNOW_BLOCK)
        # row 4 
        mc.setBlock(pos.x,pos.y+8,pos.z, block.SNOW_BLOCK)
        mc.setBlock(pos.x+1,pos.y+8,pos.z, block.SNOW_BLOCK)
        # row 5
        mc.setBlock(pos.x-1,pos.y+9,pos.z, block.SNOW_BLOCK)
        mc.setBlock(pos.x+2,pos.y+9,pos.z, block.SNOW_BLOCK)
        # row 6
        mc.setBlock(pos.x-2,pos.y+10,pos.z, block.SNOW_BLOCK)
        mc.setBlock(pos.x+3,pos.y+10,pos.z, block.SNOW_BLOCK)
        
        
def showweather():
	mc = minecraft.Minecraft.create()
	pos = mc.player.getPos()
	api_key = str("5413b147-c54a-412d-8861-3843fe143864")
	rurl = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/3772?res=3hourly&key='+api_key
	req = urllib2.Request(rurl)
	f = urllib2.urlopen(req)
	response = f.read()
	f.close()
	jdata = json.loads(response)
	weather_id = int(jdata['SiteRep']['DV']['Location']['Period'][0]['Rep'][0]['W'])

	

	if weather_id <= 8:
		placeSun(mc, pos)
	elif weather_id >= 9 or weather_id <= 21:
		placeRain(mc, pos)
	elif weather_id >= 22 or weather_id <= 27:
		placesnow(pos)
	else:
		placeLighting(pos) 


def run(runs, timeout=30):
    while runs > 0:
        showweather()
	runs = runs-1
        print "start looping"
	time.sleep(timeout)
    print 'Exited run function.'


run(10, 60*60)

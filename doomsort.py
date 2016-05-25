import omg, sys
import omg.mapedit

def rate_map(wmap):
	med = omg.MapEditor(wmap)
	rating = 0
	for t in med.things:
		if t.type == 3004: rating += 10 #zombieman
		if t.type == 9: rating += 15 #sergeant
		if t.type == 3001: rating += 15 #imp
		if t.type == 3002: rating += 15 #pinky
		if t.type == 58: rating += 18 #spectre
		if t.type == 65: rating += 25 #chaingunner
		if t.type == 69: rating += 40 #hell knight
		if t.type == 3003: rating += 60 #baron of hell
		if t.type == 66: rating += 40 #revenent 
		if t.type == 68: rating += 70 #arachnotron
		if t.type == 67: rating += 70 #mancubus
		if t.type == 3006: rating += 15 #lost soul
		if t.type == 3005: rating += 25 #cacodemon
		if t.type == 71: rating += 50 #pain elemental
		if t.type == 64: rating += 150 #archvile
		if t.type == 7: rating += 200 #spider mastermind
		if t.type == 16: rating += 250 #cyberdemon
		if t.type == 84: rating += 15 #wolf ss
	return rating

class rated_map:
	def __init__(self,wad,wmap):
		self.wmap = wad.maps[wmap]
		self.rating = rate_map(self.wmap)
		self.orig_pos = wmap

def rate_map_list(wad):
	output = []
	for m in wad.maps:
		output.append(rated_map(wad,m))
	return output

def map_index(num):
	n = ""
	if num < 10:
		n = "0"+str(num)
	else:
		n = str(num)
	return "MAP"+n

def print_map_order(sortedlist,wad):
	for m in sortedlist:
		print m.orig_pos

def place_maps_in_wad(sortedlist,wad):
	for i, m in enumerate(sortedlist):
		wad.maps[map_index(i)] = m
	return wad

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Usage:"
		print ""
		print "  doomsort.py [wad]"
	else:
		test_wad_path = sys.argv[1]
		test_wad = omg.WAD(test_wad_path)
		# test_map = omg.MapEditor(test_wad.maps["MAP01"])
		rated_list = rate_map_list(test_wad)
		sorted_rated_list = sorted(rated_list, key=lambda wmap: wmap.rating)
		#output_wad = place_maps_in_wad(sorted_rated_list,test_wad)
		#output_wad.to_file(test_output_path)
		print_map_order(sorted_rated_list,test_wad)

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort(reverse=fastest)
	total_speed = 0
	for i in range(len(redShirtSpeeds)):
		red_rider_speed = redShirtSpeeds[i]
		blue_rider_speed = blueShirtSpeeds[i]
		total_speed += max(red_rider_speed, blue_rider_speed)
	return total_speed

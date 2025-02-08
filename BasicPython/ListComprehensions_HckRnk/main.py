coord_x=int(input())
coord_y=int(input())
coord_z=int(input())
ignoredSummer=int(input())

valuesOf_coord_x=[value for value in range(coord_x+1)]
valuesOf_coord_y=[value for value in range(coord_y+1)]
valuesOf_coord_z=[value for value in range(coord_z+1)]



allCoords=[[x,y,z] for x in valuesOf_coord_x for y in valuesOf_coord_y for z in valuesOf_coord_z]
filteredCoords=[coord for coord in allCoords if (coord[0]+coord[1]+coord[2])!=ignoredSummer]
filteredCoords.sort()
print(filteredCoords)

A = 3 * [25]
print( "A:", A )            # A: ________________________________________

B = 3 * list( "25" )
print( "B:", B )            # B: ________________________________________

C = 3 * list( range(3) )
print( "C:", C )            # C: ________________________________________

D = ["a"] + ["bc"] * 2
print( "D:", D )            # D: ________________________________________

E = ["A","BC"] * 2
print( "E:", E )            # E: ________________________________________

F = "a" in ["aardvark"]
print( "F:", F )            # F: ________________________________________

G = "a" in ["a","n","t"]
print( "G:", G )            # G: ________________________________________

Z = ["Arthur", "King", "of", "the", "Britons"]

H = Z[:4]
print( "H:", H )            # H: ________________________________________

I = Z[-3:]
print( "I:", I )            # I: ________________________________________

J = Z[-6:-2]
print( "J:", J )            # J: ________________________________________

K = Z[1][2]
print( "K:", K )            # K: ________________________________________

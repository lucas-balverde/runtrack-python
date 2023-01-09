def draw_rectangle(a,b):
 c='|'+'-'*(a-2)+'|\n';
 print(c+c.replace(*'- ')*(b-2)+c)

hauteur = int(input("Quelle hauteur souhaitez vous ? "))
largeur = int(input("Quelle largeur souhaitez vous ? "))
 
draw_rectangle(hauteur, largeur)



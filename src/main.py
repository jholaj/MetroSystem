from graph_utils import build_metro_graph, dijkstra_algo

# Lines
# Muzem (C), Můstek (B) 
line_a =    ["Depo Hostivař", "Skalka", "Strašnická", "Želivského", 
            "Flora", "Jiřího z Podebrad", "Náměstí Míru", "Muzeum", 
            "Můstek", "Staroměstská", "Malostranská", "Hradčanská", 
            "Dejvická", "Nádraží Veleslavín", "Petřiny", "Nemocnice Motol"]
# Florenc (C), Můstek (A)
line_b =    ["Černý Most", "Rajská zahrada", "Hloubětín", "Kolbenova", 
            "Vysočanská", "Českomoravská", "Palmovka", "Invalidovna", 
            "Křižíkova", "Florenc", "Náměstí republiky", "Můstek", 
            "Národní třída", "Karlovo náměstí", "Anděl", "Smíchovské nádraží", 
            "Radlická", "Jinonice", "Nové Butovice", "Hůrka", "Lužiny", 
            "Luka", "Stodůlky", "Zličín"]
# Florenc (B), Muzeum (A)
line_c =    ["Letňany", "Prosek", "Střížkov", "Ládví", "Kobylisy", 
            "Nádraží Holešovice", "Vltavská", "Florenc", "Hlavní nádraží", 
            "Muzeum", "I. P. Pavlova", "Vyšehrad", "Pražského povstání", 
            "Pankrác", "Budějovická", "Kačerov", "Roztyly", "Chodov", "Opatov", "Háje"]

metro_lines = {
    "A": line_a,
    "B": line_b,
    "C": line_c
}

graph = build_metro_graph(metro_lines)
start = "Černý Most"
end = "Letňany"
shortest_path, shortest_time = dijkstra_algo(graph, start, end)
print(f"Shortest path between {start} and {end} is: {shortest_path}")
print(f"Shortest time between {start} and {end} is: {shortest_time} minutes.")
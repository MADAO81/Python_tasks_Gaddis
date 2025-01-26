guests = int(input("Enter the number of guests: "))
portions = int(input("Enter the number of portions: "))

sausage_pack_size = 10
buns_pack_size = 8

portions_overall = guests * portions

if portions_overall / sausage_pack_size != 0:
    sausage_packs_needed = portions_overall // sausage_pack_size + 1
    sausage_remains = sausage_packs_needed * sausage_pack_size - portions_overall
    
else:
    sausage_packs_needed = portions_overall // sausage_pack_size
    sausage_remains = 0 

if portions_overall / buns_pack_size != 0:
    buns_packs_needed = portions_overall // buns_pack_size + 1
    buns_remains = buns_packs_needed * buns_pack_size - portions_overall
    
else:
    buns_packs_needed = portions_overall // buns_pack_size
    buns_remains = 0 
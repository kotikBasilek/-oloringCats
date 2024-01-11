import sqlite3

con = sqlite3.connect("db.sqlite")
cur = con.cursor()


# create table if not exists user
# (
#   id integer
#         primary key autoincrement,
#   name text,
#   age integer,
#   birthday blob,
#   'average score' real
# );

def clear_table():
    cur.execute('''drop table coloring_base;''')


def create_table():
    cur.execute('''create table if not exists coloring_base
                (id integer
                   primary key autoincrement,
                img text);
                   ''')
def insert_values():
    cur.execute('''insert into coloring_base values 
            (1, 'гриб.png'),
            (2, 'котенок.png'),
            (3, 'лягушка.png'),
            (4, 'медведь.png'),
            (5, 'домик.png'),
            (6, 'замок.png'),
            (7, 'гусеница.png'),
            (8, 'домик2.png'),
            (9, 'единорог.png'),
            (10, 'мороженое.png'),
            (11, 'поезд.png'),
            (12, 'машина1.png'),
            (13, 'машина2.png'),
            (14, 'машина3.png'),
            (15, 'машина4.png'),
            (16, 'машина5.png'),
            (17, 'машина6.png'),
            (18, 'елка.png'),
            (19, 'динозавр.png'),
            (20, 'гамми.png'),
            (21, 'кот.png'),
            (22, 'кот1.png'),
            (23, 'кот2.png'),
            (24, 'кот3.png'),
            (25, 'кот4.png'),
            (26, 'кот5.png'),
            (27, 'кот6.png'),
            (28, 'кот7.png'),
            (29, 'кот8.png'),
            (30, 'кот9.png'),
            (31, 'кот10.png'),
            (32, 'кот11.png'),
            (33, 'кот12.png'),
            (34, 'котёнок1.png'),
            (35, 'котКлавиатура.png'),
            (36, 'котКоровка.png'),
            (37, 'котМиска.png'),
            (38, 'коты.png'),
            (39, 'коты1.png'),
            (40, 'коты2.png'),
            (41, 'собака.png'),
            (42, 'кот13.png'),
            (43, 'кот14.png'),
            (44, 'кот15.png'),
            (45, 'кот16.png'),
            (46, 'кот17.png'),
            (47, 'кот18.png'),
            (48, 'кот19.png'),
            (49, 'кот20.png'),
            (50, 'волк.png'),
            (51, 'волк1.png'),
            (52, 'волк2.png'),
            (53, 'волк3.png'),
            (54, '.png'),
            (55, '.png'),
            (56, '.png'),
            (57, '.png'),
            (58, '.png'),
            (59, '.png'),
            (60, '.png'),
            (61, '.png'),
            (62, '.png'),
            (63, '.png'),
            (64, '.png'),
            (65, '.png'),
            (66, '.png'),
            (67, '.png'),
            (68, '.png'),
            (69, '.png'),
            (70, '.png'),
            (71, '.png'),
            (72, '.png'),
            (73, '.png'),
            (74, '.png'),
            (75, '.png'),
            (76, '.png'),
            (77, '.png'),
            (78, '.png'),
            (79, '.png'),
            (80, '.png'),
            (81, '.png'),
            (82, '.png'),
            (83, '.png'),
            (84, '.png'),
            (85, '.png'),
            (86, '.png'),
            (87, '.png'),
            (88, '.png'),
            (89, '.png'),
            (90, '.png'),
            (91, '.png'),
            (92, '.png'),
            (93, '.png'),
            (94, '.png'),
            (95, '.png'),
            (96, '.png'),
            (97, '.png'),
            (98, '.png'),
            (99, '.png'),
            (100, '.png'),
            (101, '.png'),
            (102, '.png'),
            (103, '.png'),
            (104, '.png'),
            (105, '.png'),
            (106, '.png'),
            (107, '.png'),
            (108, '.png'),
            (109, '.png'),
            (110, '.png'),
            (111, '.png'),
            (112, '.png'),
            (113, '.png'),
            (114, '.png'),
            (115, '.png'),
            (116, '.png'),
            (117, '.png'),
            (118, '.png'),
            (119, '.png'),
            (120, '.png'),
            (121, '.png'),
            (122, '.png'),
            (123, '.png'),
            (124, '.png'),
            (125, '.png');
             ''')


clear_table()
create_table()
insert_values()
con.commit()

cur.execute('''select * from coloring_base;''')
for i in cur.fetchall():
    print(i)
# <p>{{ img }}</p> -> <img src={{img}}>

con.close()

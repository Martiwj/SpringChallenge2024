graph = {
    
    'Ada': {'Alfa': (15, 'key1'), 'Beta': (30, 'key2'), 'Chill': (25, None)},
    'Alfa': {'Ada': (15, None), 'Algol': (10, 'key3'), 'C': (20, None)},
    'Algol': {'Alfa': (10, 'key3'), 'Assembler': (20, 'key4'), 'Epsilon': (35, 'key5')},
    'Assembler': {'Algol': (20, 'key4'), 'Awk': (25, None), 'Delta': (30, None)},
    'Awk': {'Assembler': (25, None), 'Beta': (12, 'key2'), 'Fortran': (40, None)},
    'Beta': {'Awk': (12, 'key2'), 'Blackbox': (18, 'key6'), 'FK': (8, None)},
    'Blackbox': {'Beta': (18, 'key6'), 'Bliss': (15, None), 'Euclid': (45, None)},
    'Bliss': {'Blackbox': (15, None), 'Caml': (22, None), 'Gamma': (50, None)},
    'Caml': {'Bliss': (22, None), 'Cobol': (18, None), 'Delta': (25, None)},
    'Cobol': {'Caml': (18, None), 'Eiffel': (12, None), 'Delta': (20, None)},
    'Eiffel': {'Cobol': (12, None), 'Eta': (8, None), 'Euclid': (30, None)},
    'Eta': {'Eiffel': (8, None), 'Euler': (25, None), 'Java': (35, None)},
    'Euler': {'Eta': (25, None), 'FK': (20, None), 'Limbo': (40, None)},
    'FK': {'Beta': (8, None), 'Euler': (20, None), 'Gamma': (15, None)},
    'Gamma': {'FK': (15, None), 'Kappa': (20, None), 'Java': (25, None)},
    'Kappa': {'Gamma': (20, None), 'Limbo': (25, None), 'Lisp': (30, None)},
    'Limbo': {'Kappa': (25, None), 'Logo': (25, None), 'Lisp': (45, None)},
    'Logo': {'Limbo': (25, None), 'Lisp': (30, None)},
    'C': {'Bliss': (20, None), 'Chill': (25, None), 'Delta': (30, None)},
    'Chill': {'C': (25, None), 'Delta': (15, None), 'Epsilon': (20, 'key5')},
    'Delta': {'Chill': (15, None), 'Epsilon': (20, 'key5'), 'Fortran': (25, None)},
    'Epsilon': {'Delta': (20, 'key5'), 'Euclid': (18, None), 'Fortress': (35, None)},
    'Euclid': {'Epsilon': (18, None), 'Fortran': (15, None), 'Fortress': (25, None)},
    'Fortran': {'Euclid': (15, None), 'Fortress': (10, None), 'Gamma': (35, None)},
    'Fortress': {'Fortran': (10, None), 'Java': (12, None), 'Gamma': (40, None)},
    'Java': {'Fortress': (12, None), 'Lambda': (18, None), 'Kappa': (25, None)},
    'Lambda': {'Java': (18, None), 'Lisp': (22, None), 'Prolog': (22, None)},
    'Lisp': {'Lambda': (22, None), 'Prolog': (22, None)},
    'Prolog': {'Lisp': (22, None), 'Blackbox': (50, None)}
}

available_keys = {'key1', 'key2', 'key3', 'key4', 'key5'}
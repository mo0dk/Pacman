# Страшная хренотень, которую я придумал
# чтобы вкусно рендерить матрицу

map_with_sprites = [
        ["c1",   "tt",  "tt",  "tt",  "tt",  "tt", "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "whc2","whc1","tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "c2"],
        ["ll",   "seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","rr" ],
        ["ll",   "seed","sc1", "stt", "stt", "sc2", "seed","sc1", "stt", "stt", "stt", "sc2", "seed","sll", "srr", "seed","sc1", "stt", "stt", "stt", "sc2", "seed","sc1", "stt", "stt", "sc2", "seed","rr" ],
        ["ll",   "nrg", "sll",  5,    5,     "srr", "seed","sll", 5,     5,     5,     "srr", "seed","sll", "srr", "seed","sll", 5,     5,     5,     "srr", "seed","sll",     5,     5, "srr", "nrg", "rr" ],
        ["ll",   "seed","sc4", "sbb", "sbb", "sc3", "seed","sc4", "sbb", "sbb", "sbb", "sc3", "seed","sc4", "sc3", "seed","sc4", "sbb", "sbb", "sbb", "sc3", "seed","sc4", "sbb", "sbb", "sc3", "seed","rr" ],
        ["ll",   "seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","rr" ],
        ["ll",   "seed","sc1", "stt", "stt", "sc2", "seed","sc1", "sc2", "seed","sc1", "stt", "stt", "stt", "stt", "stt", "stt", "sc2", "seed","sc1", "sc2", "seed","sc1", "stt", "stt", "sc2", "seed","rr" ],
        ["ll",   "seed","sc4", "sbb", "sbb", "sc3", "seed","sll", "srr", "seed","sc4", "sbb", "sbb", "sc2", "sc1", "sbb", "sbb", "sc3", "seed","sll", "srr", "seed","sc4", "sbb", "sbb", "sc3", "seed","rr" ],
        ["ll",   "seed","seed","seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","seed","seed","rr" ],
        ["c4",   "bb",  "bb",  "bb",  "bb",  "sc2", "seed","sll", "sc4", "stt", "stt", "sc2", 5,     "sll", "srr", 5,     "sc1", "stt", "stt", "sc3", "srr", "seed","sc1", "bb",  "bb",  "bb",  "bb",  "c3" ],
        [5,      5,     5,     5,     5,     "ll",  "seed","sll", "sc1", "sbb", "sbb", "sc3", 5,     "sc4", "sc3", 5,     "sc4", "sbb", "sbb", "sc2", "srr", "seed","rr",  5,     5,     5,     5,     5    ],
        [5,      5,     5,     5,     5,     "ll",  "seed","sll", "srr", 5,     5,     5,     5,     5,     5,     5,     5,     5,     5,     "sll", "srr", "seed","rr",  5,     5,     5,     5,     5    ],
        [5,      5,     5,     5,     5,     "ll",  "seed","sll", "srr", 5,     "bc1", "bb",  "bb",  "gate","gate","bb",  "bb", "bc2", 5,     "sll", "srr", "seed","rr",  5,     5,     5,     5,     5    ],
        ["tt",   "tt",  "tt",  "tt",  "tt",  "sc3", "seed","sc4", "sc3", 5,     "rr",  5,     5,     5,     5,     5,     5,     "ll",  5,     "sc4", "sc3", "seed","sc4", "tt",  "tt",  "tt",  "tt",  "tt" ],
        [5,      5,     5,      5,    5,     5,     "seed",5,     5,     5,     "rr",  5,     5,     5,     5,     5,     5,     "ll",  5,     5,     5,     "seed",5,     5,     5,     5,     5,     5 ],
        ["bb",   "bb",  "bb",  "bb",  "bb",  "sc2", "seed","sc1", "sc2", 5,     "rr",  5,     5,     5,     5,     5,     5,     "ll",  5,     "sc1", "sc2", "seed","sc1", "bb",  "bb",  "bb",  "bb",  "bb" ],
        [5,      5,     5,     5,     5,     "ll",  "seed","sll", "srr", 5,     "bc4", "tt",  "tt",  "tt",  "tt",  "tt",  "tt",  "bc3", 5,     "sll", "srr", "seed","rr",  5,     5,     5,     5,     5 ],
        [5,      5,     5,     5,     5,     "ll",  "seed","sll", "srr", 5,     5,     5,     5,     5,     5,     5,     5,     5,     5,     "sll", "srr", "seed","rr",  5,     5,     5,     5,     5 ],
        [5,      5,     5,     5,     5,     "ll",  "seed","sll", "srr", 5,     "sc1", "stt", "stt", "stt", "stt", "stt", "stt", "sc2", 5,     "sll", "srr", "seed","rr",  5,     5,     5,     5,     5 ],
        ["c1",   "tt",  "tt",  "tt",  "tt",  "sc3", "seed","sc4", "sc3", 5,     "sc4", "sbb", "sbb", "sc2", "sc1", "sbb", "sbb", "sc3", 5,     "sc4", "sc3", "seed","sc4", "tt",  "tt",  "tt",  "tt",  "c2" ],
        ["ll",   "seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","rr" ],
        ["ll",   "seed","sc1", "stt", "stt", "sc2", "seed","sc1", "stt", "stt", "stt", "sc2", "seed","sll", "srr", "seed","sc1", "stt", "stt", "stt", "sc2", "seed","sc1", "stt", "stt", "sc2", "seed","rr" ],
        ["ll",   "seed","sc4", "sbb", "sc2", "srr", "seed","sc4", "sbb", "sbb", "sbb", "sc3", "seed","sc4", "sc3", "seed","sc4", "sbb", "sbb", "sbb", "sc3", "seed","sll", "sc1", "sbb", "sc3", "seed","rr" ],
        ["ll",   "nrg", "seed","seed","sll", "srr", "seed","seed","seed","seed","seed","seed","seed",    5,     5,"seed","seed","seed","seed","seed","seed","seed","sll", "srr", "seed","seed","nrg", "rr" ],
        ["wvc4", "stt", "sc2", "seed","sll", "srr", "seed","sc1", "sc2", "seed","sc1", "stt", "stt", "stt", "stt", "stt", "stt", "sc2", "seed","sc1", "sc2", "seed","sll", "srr", "seed","sc1", "stt", "wvc3"],
        ["wvc1", "sbb", "sc3", "seed","sc4", "sc3", "seed","sll", "srr", "seed","sc4", "sbb", "sbb", "sc2", "sc1", "sbb", "sbb", "sc3", "seed","sll", "srr", "seed","sc4", "sc3", "seed","sc4", "sbb", "wvc2"],
        ["ll",   "seed","seed","seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","sll", "srr", "seed","seed","seed","seed","seed","seed","rr" ],
        ["ll",   "seed","sc1", "stt", "stt", "stt", "stt", "sc3", "sc4", "stt", "stt", "sc2", "seed","sll", "srr", "seed","sc1", "stt", "stt", "sc3", "sc4","stt", "stt", "stt", "stt", "sc2", "seed","rr" ],
        ["ll",   "seed","sc4", "sbb", "sbb", "sbb", "sbb", "sbb", "sbb", "sbb", "sbb", "sc3", "seed","sc4", "sc3", "seed","sc4", "sbb", "sbb", "sbb", "sbb", "sbb", "sbb", "sbb", "sbb", "sc3", "seed","rr" ],
        ["ll",   "seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","seed","rr" ],
        ["c4",   "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "bb",  "c3" ]
]
# 0 - стена;
# 3 - зерно; 
# 4 - батарейка а.к.а энерджайзер;
# 6 - калитка;
# 5 - пустота / дорожка;

simplified = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 4, 0, 5, 5, 0, 3, 0, 5, 5, 5, 0, 3, 0, 0, 3, 0, 5, 5, 5, 0, 3, 0, 5, 5, 0, 4, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [5, 5, 5, 5, 5, 0, 3, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0, 0, 0, 0, 0, 3, 0, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 0, 3, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 3, 0, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 0, 3, 0, 0, 5, 0, 0, 0, 6, 6, 0, 0, 0, 5, 0, 0, 3, 0, 5, 5, 5, 5, 5],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 5, 0, 5, 5, 5, 5, 5, 5, 0, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [5, 5, 5, 5, 5, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 0, 3, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 3, 0, 5, 5, 5, 5, 5],
        [5, 5, 5, 5, 5, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 5, 5, 5, 5, 5],
        [0, 0, 0, 0, 0, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0],
        [0, 4, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 5, 5, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 4, 0],
        [0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 3, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

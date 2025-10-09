// CSV.g4
grammar CSV;

csvFile : header row* lastRow? ;
header  : row ;
row     : field (',' field)* '\r'? '\n' ;
lastRow : field (',' field)* ;

field   : TEXT   # text
        | STRING # string
        |        # empty
        ;

TEXT    : ~[,\n\r"]+ ;
STRING  : '"' ('""'|~'"')* '"' ;
WS      : [ \t]+ -> skip ;